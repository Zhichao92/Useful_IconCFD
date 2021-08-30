import argparse
import time
import os

parser = argparse.ArgumentParser(description='Merge all pids in an STL file. May prevent layer collapse at pid boundaries')
parser.add_argument('file_name', action="store", nargs = "*")
parser.add_argument("--new-file-name", help = "New file name (default is file_name_merged.stl)")
parser.add_argument("--delete-original", help = "Deletes original STL file", action = "store_true")
parser.add_argument("--pid-name", help = "Set the pid name within file")
args = parser.parse_args()

if(args.file_name is not None):
    if(len(args.file_name) > 0):
        if(args.new_file_name is not None):
            print("--new-file-name is not a valid option when applying to all files, using _merged.stl postfix")
        if(args.pid_name is not None):
            print("--pid-name is not a valid option when appling to all files, using first pid in file instead")

        for fname in args.file_name:
            write_text = []
            with open(fname) as f:
                ftext = f.readlines()
                for (i, line) in enumerate(ftext):
                    if (i == 0):
                        line_ar = line.split()
                        pid_name = line_ar[1]
                        if(args.pid_name is not None):
                            line = "solid %s \n" % args.pid_name
                    if("solid" in line and (i > 0)):
                        continue
                    write_text.append(line)
            write_text.append("endsolid %s\n" % pid_name)
            fname_ar = fname.split(".")
            new_fname = fname_ar[0] + "_merged.stl"
            print("writing %s" % new_fname)
            fout = open(new_fname, "w")
            for line in write_text:
                fout.write(line)
            if(args.delete_original):
                os.remove(fname)

    else:
        write_text = []
        with open(args.file_name) as f:
            ftext = f.readlines()
            for (i, line) in enumerate(ftext):
                if (i == 0):
                    line_ar = line.split()
                    pid_name = line_ar[1]
                    if(args.pid_name is not None):
                        line = "solid %s \n" % args.pid_name
                if("solid" in line and (i > 0)):
                    continue
                write_text.append(line)

        write_text.append("endsolid %s\n" % pid_name)
        if(args.new_file_name is not None):
            new_fname = args.new_file_name
        else:
            fname_ar = args.file_name.split(".")
            new_fname = fname_ar[0] + "_merged.stl"

        fout = open(new_fname, "w")
        for line in write_text:
            fout.write(line)

        if(args.delete_original):
            os.remove(args.file_name)
