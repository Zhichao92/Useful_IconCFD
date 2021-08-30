import numpy as np
import sys
import shutil

#rotate and shift block mesh to be better aligned with windtunnel STL

#original windtunnel coordinates
x_min = np.array([-30., -25., 0.])
x_max = np.array([ 30.,  25., 30.])

#get offset from data dict
def get_offset(data_dict):
    offset = np.array([0,0,0])
    with open(data_dict) as f:
        for line in f:
            if("referencePointTemplate" in line):
                line_ar = line.split()
                offset = [float(line_ar[-4]), float(line_ar[-3]), float(line_ar[-2])]
                break
    return offset

if(len(sys.argv) < 2):
    print(40*"-")
    print("Usage:")
    print(40*"-")
    print("python block_mesh_mod.py angle dataDict")
    print("Outputs rotated/translated in blockMesh system/blockMeshDict")
    print("copies original blockMeshDict to old_blockMeshDict")
    sys.exit()

offset = np.array(get_offset(sys.argv[2]))
angle = float(sys.argv[1])
theta = np.radians(angle)

x_max += offset
x_min += offset

x_block = np.zeros((3,2))
x_block[:,0] = x_min - 7.5
x_block[:,1] = x_max + 7.5

n_blocks = np.round((x_block[:,1] - x_block[:,0])/2.5)

rot_mat = np.array([[np.cos(theta), -np.sin(theta), 0],[np.sin(theta), np.cos(theta), 0], [0, 0, 1]])

wind_tunnel = np.array([[x_block[0][0], x_block[1][0], x_block[2][0]],
                           [x_block[0][1], x_block[1][0], x_block[2][0]],
                           [x_block[0][1], x_block[1][1], x_block[2][0]],
                           [x_block[0][0], x_block[1][1], x_block[2][0]],
                           [x_block[0][0], x_block[1][0], x_block[2][1]],
                           [x_block[0][1], x_block[1][0], x_block[2][1]],
                           [x_block[0][1], x_block[1][1], x_block[2][1]],
                           [x_block[0][0], x_block[1][1], x_block[2][1]]])
wind_tunnel -= offset
wind_tunnel_rot = [np.dot(rot_mat, w) for w in wind_tunnel]
wind_tunnel_rot += offset

new_coord_string = []

for i,w in enumerate(wind_tunnel_rot):
    new_coord_string.append("      (%f %f %f) // vertex number %d\n" % (w[0], w[1], w[2], i))



j = 0
lines = []
with open("system/blockMeshDict") as f:
    for line in f:
        if("vertex" in line):
            line = new_coord_string[j]
            j += 1
        if("hex (" in line):
            line = "      hex (0 1 2 3 4 5 6 7) (%d %d %d) simpleGrading (1 1 1)\n" % (n_blocks[0],n_blocks[1],n_blocks[2])
        lines.append(line)

shutil.copyfile("system/blockMeshDict", "old_blockMeshDict")
f = open("system/blockMeshDict", "w")
for line in lines:
    f.write(line)
f.close()
