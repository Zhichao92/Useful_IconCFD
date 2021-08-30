import sys

refine_level = 2
if(len(sys.argv) == 1):
    print("using default refinement 2")
else:
    refine_level = 3

fname = "system/iconHexMeshDict"
out_text = []
with open(fname) as f:
    inlet_line      =  "{name BBINL0000_inlet_________________002; minRefinementLevel 0; maxRefinementLevel 0; surfaceLayers 0;}"
    outlet2_line    =  "{name BBOUT0000_outlet2_______________003; minRefinementLevel 0; maxRefinementLevel 0; surfaceLayers 0;}"
    outlet_line     =  "{name BBOUT0000_outlet________________019; minRefinementLevel 0; maxRefinementLevel 0; surfaceLayers 0;}"
    topwall_line    =  "{name BBWAL0000_topWalls______________007; minRefinementLevel 0; maxRefinementLevel 0; surfaceLayers 0;}"
    lateralwall_line = "{name BBWAL0000_lateralWalls__________013; minRefinementLevel 0; maxRefinementLevel 0; surfaceLayers 0;}"
    for line in f:
        if inlet_line in line or outlet_line in line or topwall_line in line or lateralwall_line in line or outlet2_line in line:
            line = line.replace("minRefinementLevel 0", "minRefinementLevel %d" % refine_level)
            line = line.replace("maxRefinementLevel 0", "maxRefinementLevel %d" % refine_level)
        out_text.append(line)


f = open(fname, "w")
for line in out_text:
    f.write(line)
