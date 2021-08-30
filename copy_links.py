import os

parser = argparse.ArgumentParser(description='Make directories ("GOPT0962", "GEOM0960", "VPMS1000", "GRWS0960"). Drag and drop files into these and use copy_stls_up.py to easily name files')
args = parser.parse_args()


dir_names = ["GOPT0962", "GEOM0960", "VPMS1000", "GRWS0960"]
cwd = os.getcwd()

for d in dir_names:
    if(not os.path.exists(d)):
        totd = os.path.join(cwd,d)
        print("Creating dir %s" % totd)
        os.mkdir(totd)
