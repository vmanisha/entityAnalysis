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
	
#plot the band of entity popularity
if __name__ == '__main__':
	arg = sys.argv
	plot1(arg[1])
#plot the ratios of head:tail with respect to number of entities in query

#plot the band of entity popularity
