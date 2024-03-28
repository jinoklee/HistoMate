#!/bin/bash


prj=$1
input=${path}/${prj}/02.patch
output=${path}/${prj}/03.macenko

for d in $(ls *)
do
	echo $d

	mkdir -p $output/$d/20.0x

	for i in $(ls  $input/$d/20.0x/*.png)
	do
		bi=$(basename $i)
		out=$output/$d/20.0x/$bi
		if [ ! -e $out ];then
			python ./colnorm.py --slide_id $i --output_id $out
		else 
			echo "exists"
		fi
		#echo $i
	done


done


	


