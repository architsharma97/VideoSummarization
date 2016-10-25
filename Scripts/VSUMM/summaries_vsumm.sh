#!/bin/bash
DIR=../../Data/SumMe/videos/;
OUT=../../Results/SumMe/VSUMM/;
HOMEDIR=$PWD;
# choose pre-sampling rates and number of clusters for videos
# -1 for n_clusters defaults to 1/100 of video length

n_clusters=100;
for sampling_rate in "1" "2" "5" "10" "25" "30" "50" "75" "100"; do
	for filename in $DIR"paluma_jump.mp4"; do
		echo $sampling_rate
		cd $HOMEDIR
		name=${filename##*/};
		folder_name=${name%.mp4};
		mkdir $OUT$folder_name;
		mkdir $OUT$folder_name"/keyframes";
		python vsumm.py $filename $sampling_rate $n_clusters 0 0 1 $OUT$folder_name"/";
		cd ../Evaluation
		python evaluate.py $filename $sampling_rate $n_clusters $OUT$folder_name"/" $OUT$folder_name"/sampling_fmeasure.txt";
	done
done