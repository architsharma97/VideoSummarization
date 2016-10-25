import sys
sys.path.append("../../Data/SumMe/python")

from summe import *
import imageio
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

	print "Getting frames of summary!"
	frame_indices=[int(idx) for idx in open(directory+'frame_indices_'+str(n_clusters)+'_'+str(sampling_rate)+'.txt','r').read().splitlines()]
	print "Got the frames'"

	video=video.split('/')
	videoName=video[len(video)-1].split('.')[0]
	print videoName
	
	video[len(video)-2]="GT"
	HOMEDATA='/'.join(video[0:len(video)-1])
	print HOMEDATA

	# OPTIONAL: Recreating summary
	# video=imageio.get_reader(sys.argv[1])
	# summary=np.array([video.get_data(idx) for idx in frame_indices])
	
	f_measure, summary_length=evaluateSummary(frame_indices,videoName,HOMEDATA)
	print "F-measure %.3f at length %.2f" %(f_measure, summary_length)

if __name__ == '__main__':
	main()