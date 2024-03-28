#!/bin/bash

prj=$1
PathProfiler=../refer/PathProfiler
input=${path}/${prj}/00.svs
mask=${path}/${prj}/01.mask
output=${path}/${prj}/02.patch

mkdir -p ${output}

python ${PathProfiler}/tile-extract/tiling.py --save_folder ${output}\
       	--slide_dir ${input} \
       	--mask_magnification 1.25  \
	--tile_magnification 20\
	--tile_size 512\
	--stride 512\
	--mask_ratio 0.1\
	--mask_dir ${mask} \
	--slide_id '*.svs'
