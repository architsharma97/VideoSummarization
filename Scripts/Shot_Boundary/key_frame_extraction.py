import sys
import imageio
import numpy as np
import cv2
import scipy.io
import sklearn.neighbors
import pywt

# System Arguments
# Argument 1: Location of the video
# Argument 2: Sampling rate (k where every kth frame is chosed)

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
	hist = cv2.calcHist(frames[0], [0, 1, 2], None, [256/num_bins_H, 256/num_bins_S, 256/num_bins_V],
		[0, 256, 0, 256, 0, 256])
	hist = cv2.normalize(hist).flatten()
	print "Generated Histogram"
	return hist;

def bhattacharyya_distance(color_histogram):
	distance_matrix = []
	for i in range(len(color_histogram)):
		temp_list = []
		for j in range(len(color_histogram)):
			hist = cv2.compareHist(color_histogram[i],color_histogram[j],cv2.cv.CV_COMP_BHATTACHARYYA)
			temp_list.append(hist)
		distance_matrix.append(temp_list)
	return distance_matrix

sklearn.neighbors.kneighbors_graph(color_histogram, n_neighbors, mode='connectivity', 
	metric='minkowski', p=2, metric_params=None, include_self=False, n_jobs=1)

cv2.compareHist(color_histogram[1],color_histogram[2],cv2.cv.CV_COMP_BHATTACHARYYA)

def main():
	print "Opening video!"
	global sampling_rate
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

	#calculate distance between feature histograms
	distance_matrix = bhattacharyya_distance(color_histogram)

	#calculate NNG
	eps_texture_NN = [None]*len(distance_matrix[0])
	eps_texture_RNN = [[]]*len(distance_matrix[0])
	for i in range(len(distance_matrix[0])):
		temp = float("inf")
		for j in range(len(distance_matrix[i])):
			if distance_matrix[i][j] <= temp:
				eps_texture_NN[i] = j
				temp = distance_matrix[i][j]
		eps_texture_RNN[eps_texture_NN[i]].append(i)


	#to-do : Add code to return the SCC of the Reverse nearest neighbor graph (RNNG) 

	#to-do : Select represenatative frames for each RNNG(it'll be the summary)

if __name__ == '__main__':
	main()