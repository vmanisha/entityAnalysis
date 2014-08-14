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

#plot the band of entity popularity
if __name__ == '__main__':
	arg = sys.argv
	plot1(arg[1])