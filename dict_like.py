import sys
import argparse

parser = argparse.ArgumentParser(description='Take fields from source_data_dict and copy into target_data_dict including Area, wheel base length, front/rear track, reference point, endtime, start avg time, Porous Media coeffs')
parser.add_argument('source_data_dict', action="store")
parser.add_argument('target_data_dict', action="store")
args = parser.parse_args()

orig_dict = args.source_data_dict
copy_dict = args.target_data_dict
VPMS_list = []

#defaults which are necessary if copying from a v1 dataDict that does not have these
run_t = 1.5
start_t = 0.5

with open(orig_dict) as f:
    for line in f:
        line_ar = line.split()
        if("AreaRefTemplate_distRefWBTemplate" in line):
            A_ref = line_ar[-3]
            d_ref = line_ar[-2]
        if("frontTrackTemplate_rearTrackTemplate" in line):
            f_track = line_ar[-3]
            r_track = line_ar[-2]
        if("endTime_startTMeanVars (X_X/0_0,_s_s)" in line):
            run_t   = line_ar[-3]
            start_t = line_ar[-2]
        if("referencePointTemplate (X_X_X,_m)" in line):
            ref_x = line_ar[-4]
            ref_y = line_ar[-3]
            ref_z = line_ar[-2]
        if("TYPEP_P1_P2_VPMS" in line):
            VPMS_list.append((line_ar[-3], line_ar[-2]))

new_lines = []
vpc = 0
with open(copy_dict) as f:
    for line in f:
        if("AreaRefTemplate_distRefWBTemplate" in line):
            numloc = line.find("1 1")
            line = line[:numloc] + ("%s %s" % (A_ref, d_ref)) + line[numloc + 3:]
        if("frontTrackTemplate_rearTrackTemplate" in line):
            numloc = line.find("1 1")
            line = line[:numloc] + ("%s %s" % (f_track, r_track)) + line[numloc + 3:]
        if("referencePointTemplate (X_X_X,_m)" in line):
            numloc = line.find("0 0 0")
            line = line[:numloc] + ("%s %s %s" % (ref_x, ref_y, ref_z)) + line[numloc + 5:]
        if("endTime_startTMeanVars (X_X/0_0,_s_s)" in line):
            numloc = line.find("1.5 0.5")
            line = line[:numloc] + ("%s %s " % (run_t, start_t)) + line[numloc + 7:]
        if("TYPEP_P1_P2_VPMS" in line):
            numloc = line.find("100 100")
            line = line[:numloc] + ("%s %s " % (VPMS_list[vpc][0], VPMS_list[vpc][1])) + line[numloc + 7:]
            vpc+=1
        new_lines.append(line)

with open(copy_dict, "w") as f:
    for line in new_lines:
        f.write(line)
