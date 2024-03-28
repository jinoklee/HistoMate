#!/bin/bash

prj=$1

PathProfiler=../referi/PathProfiler
output=${path}/${prj}/01.mask
input=${path}/${prj}/00.svs


mkdir -p ${output}

python ${PathProfiler}/tissue-segmentation/run.py \
	--save_folder ${output}\
       	--slide_dir ${input}\
       	--mask_magnification 1.25 \
	--batch_size 16 \
	--model ${PathProfiler}/checkpoint_ts.pth
