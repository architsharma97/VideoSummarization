#!/bin/bash
DIR=../../Data/SumMe/videos/;
OUT=../../Results/SumMe/Uniform_Sampling/;
HOMEDIR=$PWD;
sampling_rate="1";

for percent in "15"; do
	echo $percent
	for filename in $DIR"paluma_jump.mp4";do
		echo $filename
		cd $HOMEDIR
		name=${filename##*/};
		folder_name=${name%.mp4};
		mkdir $OUT$folder_name;
		python uniform.py $filename $percent $OUT$folder_name"/";
		cd ../Evaluation
		python evaluate.py $filename $sampling_rate $percent $OUT$folder_name"/" $OUT$folder_name"/final_results_uniform_"$percent".txt" uniform;
	done
done