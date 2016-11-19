import sys
import imageio
import numpy as np
import cv2
import scipy.io
import pywt
from scc import strongly_connected_components_tree

# System Arguments
# Argument 1: Location of the video
# Argument 2: Sampling rate (k where every kth frame is chosed)

# defines the number of bins for pixel values of each type as used the original work
num_bins_H=32
num_bins_S=4
num_bins_V=2

# manual function to generate histogram on HSV values
def generate_histogram_hsv(frame):
	hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
	hsv_frame = hsv_frame
	global num_bins_H, num_bins_S, num_bins_V
	hist = cv2.calcHist([frame], [0, 1, 2], None, [256/num_bins_H, 256/num_bins_S, 256/num_bins_V],
		[0, 256, 0, 256, 0, 256])
	hist = cv2.normalize(hist).flatten()
	return hist;

# function to calculate the distance matrix for bhattacharyya_distance
def bhattacharyya_distance(color_histogram):
	distance_matrix=np.zeros((len(color_histogram),len(color_histogram)))
	for i in range(len(color_histogram)):
		temp_list = []
		for j in range(len(color_histogram)):
			print i,j
			if i != j:
				distance_matrix[i][j] = cv2.compareHist(color_histogram[i],color_histogram[j],cv2.cv.CV_COMP_BHATTACHARYYA)
			else:
				distance_matrix[i][j] = float("inf")
	return distance_matrix

def main():
	if len(sys.argv) < 3:
		print "Incorrect no. of arguments, Halting !!!!"
		return
	print "Opening video!"
	#frame chosen every k frames
	sampling_rate=int(sys.argv[2])
	video=imageio.get_reader(sys.argv[1]);
	print "Video opened\nChoosing frames"

	#replace this with the frames detected using shot boundary detection.
	frames=[np.array(video.get_data(i*sampling_rate)) for i in range(len(video)/sampling_rate)]

	print "Frames chosen"
	#extracting color features from each representative frame
	print "Generating Histrograms"
	color_histogram=[generate_histogram_hsv(frame) for frame in frames]
	print "Color Histograms generated"

	#to-do (optional): extract texture features for each frame

	#calculate distance between each pair of feature histograms
	print "Evaluating the distance matirix for feature hitograms"
	distance_matrix = bhattacharyya_distance(color_histogram)
	print "Done Evalualting distance matrix"

	#constructing NNG (nearest neighbour graph) based of distance_matrix
	print "Constructing NNG"
	eps_texture_NN = [None]*len(distance_matrix[0])
	for i in range(0,len(distance_matrix[0])):
		temp = float("inf")
		for j in range(len(distance_matrix[i])):
			if distance_matrix[i][j] <= temp:
				eps_texture_NN[i] = j
				temp = distance_matrix[i][j]
		print eps_texture_NN[i], i

	#constructing RNNG(reverse nearest neighbour graph) for the above NNG
	print "Constructing RNNG"
	eps_texture_RNN = {}
	for i in range(len(eps_texture_NN)):
		if eps_texture_NN[i] in eps_texture_RNN.keys():
			eps_texture_RNN[eps_texture_NN[i]].append(i)
		else:
			eps_texture_RNN[eps_texture_NN[i]] = [i]
		if i not in eps_texture_RNN.keys():
			eps_texture_RNN[i] = []

	#calculating the SCCs(strongly connected components) for RNNG
	print "Finiding the strongly connected components of RNNG"
	vertices = [i for i in range(0,len(frames))]
	scc_graph = strongly_connected_components_tree(vertices, eps_texture_RNN)

	#choosing one frame per SCC in summary
	print "Evaluating final summary"
	summary = []
	for scc in scc_graph:
		summary.append(next(iter(scc))*sampling_rate)

	# writing the summary in a file 
	file = open(sys.argv[1]+'.summary', 'w')
	for item in summary:
	  file.write("%s\n" % item)	

if __name__ == '__main__':
	main()