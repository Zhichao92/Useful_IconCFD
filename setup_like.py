import os
import shutil
import sys
import argparse


parser = argparse.ArgumentParser(description='Give .stls in a directory the name prefixes as those in another directory')
parser.add_argument('source_input_directory', action="store")
parser.add_argument('target_input_directory', action="store")
args = parser.parse_args()

src_dir = args.source_input_directory
target_dir = args.target_input_directory


print("Source directory: %s" % src_dir)
print("Destination directory: %s" % target_dir)


target_files = [f for f in os.listdir(target_dir) if os.path.isfile(os.path.join(target_dir, f))]
src_files = [f for f in os.listdir(src_dir) if os.path.isfile(os.path.join(src_dir,f))]
for df in target_files:
	for sf in src_files:
		if (df in sf):
			df_new = sf.split("_")[0] + "_" + df
			print("moving %s to %s" % (df, df_new))
			shutil.move(os.path.join(target_dir,df), os.path.join(target_dir, df_new))
