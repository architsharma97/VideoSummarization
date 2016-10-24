# k means clustering to generate video summary
import sys
import imageio
import numpy as np
import cv2

# k-means
from sklearn.cluster import KMeans

# defines the number of bins for pixel values of each type {r,g,b}
num_bins=16

# size of values in each bin
range_per_bin=256/num_bins

#frame chosen every k frames
sampling_rate=int(sys.argv[2])

#manual function to generate a 3D tensor representing histogram
def generate_histogram(frame):
	global num_bins, sampling_rate
	histogram=np.zeros(num_bins,num_bins,num_bins)
	for row in range(len(frame)):
		for row in range(len(frame[row])):
			r,g,b=frame[row][col]
			histogram[r/num_bins][g/num_bins][b/num_bins]+=1;
	return histogram

def main():
	global num_bins, sampling_rate
	video=imageio.get_reader(sys.argv[1]);

	#choosing the subset of frames from which video summary will be generateed
	frames=[video.get_data(i*sampling_rate) for i in range(len(video)/sampling_rate)]
	
	#manually generated histogram
	color_histogram=[generate_histogram(frame) for frame in frames]

	#opencv: generates 3 histograms corresponding to each channel for each frame
	channels=['b','g','r']
	hist=[]
	for i,col in enumerate(channels):
		hist.append([cv2.calcHist([frame],[i],None,[num_bins],[0,256]) for frame in frames])
    
	#clustering

	#unfold the tensor into a vector
	color_histogram=np.asarray([hist.flatten() for hist in color_histogram])
	
		
if __name__ == '__main__':
	main()