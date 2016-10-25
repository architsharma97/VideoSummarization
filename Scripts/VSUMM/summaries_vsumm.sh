#!/bin/bash
DIR=../../Data/SumMe/videos/;
OUT=../../Results/SumMe/VSUMM/;

# choose pre-sampling rates and number of clusters for videos
# -1 for n_clusters defaults to 1/100 of video length
sampling_rate=30;
n_clusters=20;

for filename in $DIR"*.mp4"; do
	name=${filename##*/};
	folder_name=${name%.mp4};
	mkdir $OUT$folder_name;
	mkdir $OUT$folder_name"/keyframes";
	python vsumm.py $filename $sampling_rate $n_clusters 0 1 $OUT$folder_name"/";
done