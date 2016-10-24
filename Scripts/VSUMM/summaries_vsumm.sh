#!/bin/bash
DIR=../../Data/SumMe/videos/;
OUT=../../Results/SumMe/VSUMM/;
sampling_rate
for filename in $DIR"*.mp4"; do
	name=${filename##*/};
	folder_name=${name%.mp4}
	mkdir $OUT$folder_name
	python vsumm.py $filename $sampling_rate -1 0 1 $OUT$folder_name
done