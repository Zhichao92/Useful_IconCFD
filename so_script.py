import os
import ansa
from ansa import base

def main(input_dir):
	files = [f for f in os.listdir(input_dir) if ".stl" in f]
	if(input_dir[-1] == "/"):
		input_dir = input_dir[:-1]
	new_dir = "%s_obj" % input_dir
	os.mkdir(new_dir)
	for f in files:
		base.InputStereoLithography(os.path.join(input_dir, f), properties_id = "offset")
		new_f = os.path.join(new_dir, f.replace(".stl", ".obj.gz"))
		base.OutputWaveFront(new_f, 'ALL', 'MILLIMETERS')
		base.DestroyAnsaModel(base.GetCurrentAnsaModel())
