import matplotlib.pyplot as plt
import sys
#plot the head entity % coverage with id
def plot1(file1):
	x = []
	y = []
	
	for line in open(file1,'r'):
		split = line.split('\t')
		x.append(float(split[0]))
		y.append(round(float(split[1]),3))
	l, = plt.plot(x, y, 'r-')
	plt.xlabel('Entity Id')	
	plt.ylabel('Percentage')	
	plt.rcParams['xtick.major.pad']='8'
	#plt.title('C')
	plt.savefig('paper/images/entity-head-dist.png', bbox_inches='tight')
	#plt.shwow()


#plot the ratios of head:tail with respect to number of entities in query
def plot2(data):
	for ent, counts in data.iteritems():
		#print ent, counts
		x = []
		y = []
		sent = ent #str(int(ent))#+' Entities'
		#total = sum(counts.values())
		for a, b in sorted(counts.items(), key =lambda x : x[0]) :
			#if a < 10:
			x.append(a)
			y.append(b)
			#y.append(b/total)
		#print ent, x, y
		if len(x) > 0 and len(y) > 0 : #and ent < 7:
			#print x, y
			l, = plt.plot(x, y,label=sent)
		
		#plt.title('C')
	#plt.xlabel('Query Distribution vs Head To Tail Entities Ratio')	
	plt.xlabel('Id')	
	#plt.xlabel('Rank of Co-occuring Head Entity')	
	#plt.xlabel('Rank of Co-occuring Head Entity')	
	#plt.ylabel('% Queries')	
	plt.ylabel('Log Frequency')	
	plt.xscale('log')
	plt.yscale('log')
	plt.rcParams['xtick.major.pad']='8'
	plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0., title = 'Types')
	plt.savefig('paper/images/head-tail-ent-spot-dist.png', bbox_inches='tight')


def plotHist(data):
	width = 0.24       # the width of the bars

	fig = plt.figure()
	ax = plt.subplot(111)
	rect = []
	colour = ['r','b','g', 'y']
	for i in range(len(data[1:])):
		print i, data[0], data[i+1], [x+(width*i) for x in data[0]]
		
		rect.append(ax.bar([x+(width*i) for x in data[0]], data[i+1], width, color=colour[i]))
		

	# add some text for labels, title and axes ticks
	ax.set_ylabel('%Queries')
	ax.set_xlabel('#Entities in Query')
	#ax.set_title('')
	ax.set_xticks([x+(width*1.5) for x in data[0]])
	ax.set_xticklabels( tuple(data[0]) )
	
	box = ax.get_position()
	ax.set_position([box.x0, box.y0 + box.height * 0.1,
                 box.width, box.height * 0.9])

	ax.legend((rect[0], rect[1], rect[2]),('All-Head', 'All-Tail','Head and Tail'),loc='upper center',
	fancybox=True, ncol=4, bbox_to_anchor=(0.5,-0.1))
	# Put a legend below current axis
	plt.show()
	plt.savefig('paper/images/entity-head-tail-count.png')
	
#plot the band of entity popularity
if __name__ == '__main__':
	arg = sys.argv
	data = []
	done = False;
	for line in open(arg[1],'r'):
		split= line.strip().split();
		if not done:
			for i in range(len(split)):
				data.append([])
			done = True
		
		for i in range(len(split)):
			data[i].append(float(split[i]))
	print data						
	#plot1(arg[1])
	plotHist(data)
#plot the ratios of head:tail with respect to number of entities in query


