#!/bin/bash
DIR=../../Data/SumMe/videos/;
OUT=../../Results/SumMe/VSUMM/;
sampling_rate=10
n_clusters=-1
for filename in $DIR"paluma_jump.mp4"; do
	name=${filename##*/};
	folder_name=${name%.mp4}
	mkdir $OUT$folder_name
	mkdir $OUT$folder_name"/keyframes"
	python vsumm.py $filename $sampling_rate $n_clusters 0 1 $OUT$folder_name"/"
done