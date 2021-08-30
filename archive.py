import tarfile
import os
import glob
import argparse

parser = argparse.ArgumentParser(description='Archive an icon case for later rerunning. Run in directory of Case folder. Places dataDict, input, and output from fordcfd-post .tgz archive')
args = parser.parse_args()

archive_paths = ["dataDict", "input"]
cwd = os.getcwd()
tar_name = cwd.split("/")[-1] +  ".tar.gz"
archive_paths.append(glob.glob("*/*.tar.gz")[0])
with tarfile.open(tar_name, "w:gz") as tf:
     for d in archive_paths:
         if os.path.isfile(d) or os.path.isdir(d):
             print("Adding %s to archive" % d)
             an = os.path.join(d)
             tf.add(d, arcname=an)
