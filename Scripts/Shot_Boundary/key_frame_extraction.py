import sys
import imageio
import numpy as np
import cv2
import scipy.io
import cv2


# defines the number of bins for pixel values of each type as used the original work
num_bins_H=32
num_bins_S=4
num_bins_V=2

#frame chosen every k frames
sampling_rate=int(sys.argv[2])


# manual function to generate a 3D tensor representing histogram on HSV values
# extremely slow
def generate_histogram_hsv(frame):
	print "Received frame"
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
	global num_bins_H, num_bins_S, num_bins_V
	histogram=np.zeros((num_bins_H,num_bins_S,num_bins_V))
	for row in range(len(hsv_frame)):
		for col in range(len(hsv_frame[row])):
			r,g,b=hsv_frame[row][col]
			histogram[r/num_bins_H][g/num_bins_S][b/num_bins_V]+=1;
	return histogram
	print "Generated Histogram"


def main():
	global num_bins, sampling_rate, percent, num_centroids
	print "Opening video!"
	video=imageio.get_reader(sys.argv[1]);
	print "Video opened\nChoosing frames"

	#replace this with the frames detected using shot boundary detection.
	#choosing the subset of frames from which video summary will be generateed
	frames=[video.get_data(i*sampling_rate) for i in range(len(video)/sampling_rate)]
	print "Frames chosen"
	print "Length of video %d" % len(video)
		
	#extracting color features from each frame
	print "Generating 3D Tensor Histrograms"
	color_histogram=[generate_histogram_hsv(frame) for frame in frames]
	print "Color Histograms generated"

	#to-do(optional) : extract texture features for each frame

	#to-do : Add code to return the Nearest neighbor graph (NNG)

	#to-do : Add code to return the SCC of the Reverse nearest neighbor graph (RNNG) 

	#to-do : Select represenatative frames for each RNNG(it'll be the summary)

if __name__ == '__main__':
	main()