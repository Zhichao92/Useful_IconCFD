# Useful_IconCFD
This repository contains scripts useful for setting up, monitoring, and debugging iconCFD runs. Scripts may not be up to date with latest version of icon, use with care.

convert/convert_obj_to_stl.py -- convert input folder from .stl to .obj.gz input/ -> input_obj convert/convert_stl_to_obj.py -- convert input folder from .obj.gz to .stl input/ -> input_stl Conversion scripts use ANSA. Update script location from (/s/tmp/pnorman8) on line 36 if you deploy this yourself

archive.py -- Archive an icon case for later rerunning. Run in directory of Case folder. Places dataDict, input, and output from fordcfd-post .tgz archive

make_dirs.py -- Make directories ("GOPT0962", "GEOM0960", "VPMS1000", "GRWS0960"). Drag and drop files into these directories and use copy_stls_up.py to easily name files

copy_stls_up.py -- Copies .stl files from directories up one level and preappends directory name to file (GOPT0962/file.stl -> GOPT0962_file.stl). Use after make_dirs.py

copy_links.py -- Copies files from dynamic links to current directory

setup_like.py -- Give .stls in a directory the same name prefixes as those in another directory

merge_pids.py -- Merge all pids in an STL file. May prevent layer collapse at pid boundaries within STL

refine_bounds.py -- Change from level 0 to level 2 in iconHexMeshDict for boundaries: inlet, outlet, outlet2, topWalls, lateralWalls. Run this in the Case directory

trim_prefix.py -- Remove all prefixes (GOPT, GEOM, VPMS, GRWS) from all files in directory

dict_like.py -- Take fields from source_data_dict and copy into target_data_dict including Area, wheel base length, front/rear track, reference point, endtime, start avg time, Porous Media coeffs
