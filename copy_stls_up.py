import glob
import subprocess
import shutil
import os
files = glob.glob("*.obj.gz")

if(not os.path.exists("links")):
	os.mkdir("links")

for f in files:
	link_text = subprocess.check_output("readlink %s" % f, shell = 'True')
	link_text = link_text.decode('ascii').strip("\n")
	shutil.move(f, "links/")
	link_path = os.path.join(os.getcwd(), link_text)
	shutil.copy(link_path, ".")
