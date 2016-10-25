import sys
sys.path.append("../../Data/SumMe/python")

from summe import *
# System Arguments
# Argument 1: Location of the video
# Argument 2: Sampling rate
# Argument 3: Number of clusters
# Argument 4: Results folder

def main():
	video=sys.argv[1]
	directory=sys.argv[4]
	sampling_rate=int(sys.argv[2])
	n_clusters=int(sys.argv[3])

	frame_indices=[int(idx) for idx in open(directory+'frame_indices_'+str(n_clusters)+'_'+str(sampling_rate)+'.txt','r').read().splitlines()]
	print frame_indices

if __name__ == '__main__':
	main()