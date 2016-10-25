#!/bin/bash
DIR=../../Data/SumMe/videos/;
OUT=../../Results/SumMe/VSUMM/;
HOMEDIR=$PWD;
# choose pre-sampling rates and number of clusters for videos
# -1 for n_clusters defaults to 1/100 of video length

# sampling rates for future use
# "2" "5" "10" "25" "30" "50" "75" "100"

# percent of the actual video
for n_clusters in "15"; do
	for sampling_rate in "1"; do
		for filename in $DIR"Playing_on_water_slide.mp4"; do
			echo $sampling_rate
			cd $HOMEDIR
			name=${filename##*/};
			folder_name=${name%.mp4};
			mkdir $OUT$folder_name;
			mkdir $OUT$folder_name"/keyframes";
			python vsumm.py $filename $sampling_rate $n_clusters 0 0 1 $OUT$folder_name"/";
			cd ../Evaluation
			python evaluate.py $filename $sampling_rate $n_clusters $OUT$folder_name"/" $OUT$folder_name"/sampling_fmeasure_"$n_clusters".txt";
		done
	done
done