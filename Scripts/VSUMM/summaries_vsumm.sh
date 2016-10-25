#!/bin/bash
DIR=../../Data/SumMe/videos/;
OUT=../../Results/SumMe/VSUMM/;
HOMEDIR=$PWD;
# choose pre-sampling rates and number of clusters for videos
# -1 for n_clusters defaults to 1/100 of video length
sampling_rate=1;
n_clusters=200;

for filename in $DIR"paluma_jump.mp4"; do
	cd $HOMEDIR
	name=${filename##*/};
	folder_name=${name%.mp4};
	mkdir $OUT$folder_name;
	mkdir $OUT$folder_name"/keyframes";
	python vsumm.py $filename $sampling_rate $n_clusters 0 1 $OUT$folder_name"/";
	cd ../Evaluation
	python evaluate.py $filename $sampling_rate $n_clusters $OUT$folder_name"/";
done