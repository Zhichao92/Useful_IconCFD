import os
import shutil
import argparse

parser = argparse.ArgumentParser(description='Remove all prefixes (GOPT, GEOM, VPMS, GRWS) from all files in directory')
args = parser.parse_args()

for f in os.listdir(os.getcwd()):
	if(os.path.isdir(f)): continue
	fsplit = f.split("_")
	prefix = fsplit[0]
	if("GOPT" in prefix or "GEOM" in prefix or "VPMS" in prefix or "GRWS" in prefix):
		fnew = f[len(fsplit[0])+1:]
		shutil.move(f, fnew)
