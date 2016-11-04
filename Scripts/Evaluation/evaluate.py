import sys
sys.path.append("../../Data/SumMe/python")
import os
from summe import *
import imageio
# System Arguments
# Argument 1: Location of the video
# Argument 2: Sampling rate
# Argument 3: Percentage of clusters
# Argument 4: Results folder

# OPTIONAL
# Argument 5: File where the results will be written

def main():
	video=sys.argv[1]
	directory=sys.argv[4]
	sampling_rate=int(sys.argv[2])
	n_clusters=int(sys.argv[3])
	video_length=len(imageio.get_reader(sys.argv[1]))
	n_clusters=int(n_clusters*video_length/100)
	if video_length/sampling_rate < n_clusters:
		n_clusters=video_length/sampling_rate

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

	if len(sys.argv)>5:
		if os.path.exists(sys.argv[5])==False:
			out_file=open(sys.argv[5],'a')
			out_file.write("Sampling rate, Number of Clusters, F-measure, Summary Length\n")
		else:
			out_file=open(sys.argv[5],'a')
		out_file.write("%d,%d,%f,%f\n"%(sampling_rate,n_clusters,f_measure,summary_length))
	
	# optional plotting of results
	# methodNames={'VSUMM using Color Histrograms'}
	# summaries={}
	# summaries[0]=frame_indices
	# plotAllResults(summaries,methodNames,videoName,HOMEDATA)

if __name__ == '__main__':
	main()