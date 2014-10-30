#some functions
import sys
from plots import plot2
import ast
def findAverage(file1):
	stats = {'total':0.0, 'hh':0.0, 'ht':0.0, 'tt':0.0}
	i = 1
	total = 0
	headForTail = {}
	#rankDist = {}
	for line in open(file1,'r'):
		split = line.strip().split('\t')
		hc = float(split[1])
		tc = float(split[2])
		total = hc+tc
		#rankFreq = ast.literal_eval(split[-1].strip())
		#for entry, val in rankFreq.items():
		#	rankDist[entry] = rankDist.setdefault(entry, 0.0)+ 1
		
		if total not in headForTail:
			headForTail[total]={'tot':0.0, 'hh':0.0, 'tt':0.0, 'ht':0.0}
		#{'tot':0.0,'rtot':0.0}
		#if tc not in headForTail:
		#	headForTail[tc]={}#{'tot':0.0,'rtot':0.0}
		
		try:
			
			#headForTail[total]={'tot':0.0}#{'tot':0.0,'rtot':0.0}
			if hc > 0 and tc == 0:
				headForTail[total]['hh']+=1
			elif tc > 0 and hc == 0:
				headForTail[total]['tt']+=1
			else:
				headForTail[total]['ht']+=1
				
				
			#headForTail[tc][hc] = headForTail[tc].setdefault(hc,0.0)+1.0
			#for entry, val in rankFreq.items():
			#	headForTail[total][entry] = headForTail[total].setdefault(entry,0.0) + val
			
			#ratio = round(hc/tc,2)
			#headForTail[total][ratio] = headForTail[total].setdefault(ratio,0.0)+1.0
			#headForTail[total]['rtot']+=ratio
		except:
			pass
		headForTail[total]['tot']+=1
		
		#		headForTail[total]= {'hh':0.0,'tt':0.0, 'hp':0.0,\
		#		'tp':0.0, 'httot':0.0,'tot':0.0}
		#if hc > 0 and tc > 0:
		#	headForTail[total]['hp']+= hc/total
		#	headForTail[total]['tp']+= tc/total
		#	headForTail[total]['httot']+= 1
		#elif hc == 0:
		#	headForTail[total]['tt']+=1
		#elif tc == 0:
		#	headForTail[total]['hh']+=1
		#headForTail[total]['tot']+=1
				
		#tid = int(split[0])
		#stats['total'] += float(split[1])
		#stats['hh'] += hc
		#stats['ht'] += float(split[])
		#stats['tt'] += tc
		#if tc not in headForTail:
		#	headForTail[tc] = {}
		#headForTail[tc][hc]= headForTail[tc].setdefault(hc, 0.0) + 1.0
		i+=1
	#total+= stats['hh']+ stats['tt']
	#print total, stats	['hh']/total, stats['tt']/total
	

	for entry, counts in headForTail.items():
		print entry, str(counts) #, counts['rtot']/counts['tot']
	#print rankDist
	#plot2(headForTail)
		
def loadEntDict(file1):
	headEnt = {}
	for line in open(file1,'r'):
		split = line.split('\t')
		count = int(split[-1])
		ent = split[0].strip()
		if count > 200000:
			headEnt[ent] = 1
		elif count > 22000:
			headEnt[ent] = 2
		elif count > 5800:
			headEnt[ent] = 3
		elif count > 1900:
			headEnt[ent] = 4
		elif count >700:
			headEnt[ent] = 5 #95%
		elif count > 450:
			headEnt[ent] = 6 #97.8
		else:
			headEnt[ent] = 7
	return headEnt

def findHeadEntitiesCoOccurrance(file1, file2):
	headEntCo = {1:0.0,2:0.0,3:0.0,4:0.0,5:0.0,6:0.0,7:0.0}
	#entTotal = 0.0
	#entTotal+= int(split[-1])
	headEnt = loadEntDict(file1)
	
	total = 0.0
	tt = 0.0
	hh = 0.0
	for line in open(file2,'r'):
		split = line.split('\t')
		ent1 = split[0].strip()
		ent2 = split[1].strip()
		count = float(split[-1])
		total+= count
		if ent1 in headEnt and ent2 in headEnt:
			hh+=count
		elif ent1 in headEnt:
			headEntCo[headEnt[ent1]] += count
		elif ent2 in headEnt:
			headEntCo[headEnt[ent2]] += count
		else:
			tt+= count
	
	print 'tt',tt, tt/total, 'hh', hh, hh/total
	for quant, freq in headEntCo.items():
		print quant, freq, freq/total
	#for ent, count in sorted(headEnt.items(), reverse = True, key = lambda x : x[1]):
	#	print ent,count/entTotal, ' '.join('{0}:{1}'.format(x,y) for x,y in headEntCo[ent].items())
		# headEntCo[ent]['ht']
		
	#for rtype, count in coOccurStats.items():
	#	print rtype, count/total

#spot rank in head and tail
def findHeadRankTail(file1, file2):
	spotRank = {}
	i = 1.0
	total = 0.0
	for line in open(file1,'r'):
		split = line.split('\t')
		if split[0] not in spotRank:
			spotRank[split[0]] = {'hrank':'NA', 'trank':'NA',\
			 'normHRank':'NA', 'normTRank':'NA'}
			total+=1.0
		spotRank[split[0]]['hrank'] = i
		i+=1
	i = 1.0
	for line in open(file2,'r'):
		split = line.split('\t')
		if split[0] not in spotRank:
			spotRank[split[0]] = {'hrank':'NA', 'trank':'NA',\
			 'normHRank':'NA', 'normTRank':'NA'}
			total+=1.0
		spotRank[split[0]]['trank'] = i
		i+=1
	
	for spot, ranks in spotRank.items():
		if ranks['hrank'] !='NA':
			ranks['normHRank'] = round(ranks['hrank']/total,5)
		if ranks['trank'] !='NA':
			ranks['normTRank'] = round(ranks['trank']/total,5)	
		
	sort = sorted(spotRank.items(), key = lambda x : x[1]['trank'])
	#notInHead = 0
	#notInTail = 0
	for entry in sort:
		ranks = entry[1]
		print entry[0], '\t', ranks['hrank'],'\t', ranks['trank'], \
			ranks['normHRank'], ranks['normTRank']
		#if entry[1]['hrank'] == 'NA':
			#notInHead+=1
		#elif entry[1]['trank'] == 'NA':
			#notInTail+=1
	#print 'Not in Head', notInHead,'and not in tail ', notInTail

def loadSpotEntDict(file1):
	freqDict = {}
	i = 0
	for line in open(file1, 'r'):
		split = line.split('\t')	
		freqDict[i] = int(split[-1])
		i+=1
	return freqDict	


def countEnt(fileName):
	count = {}
	for line in open(fileName,'r'):
		split = line.strip().split('\t');
		total = float(split[1])+ float(split[2]);
		if total not in count:
			count[total] = 0;
		count[total] += 1;
	for entry, query in count.iteritems():
		print entry, '\t' , query;

if __name__ == '__main__':
	arg = sys.argv
	#countEnt(arg[1])
	#findHeadRankTail(arg[1],arg[2])
	#findHeadEntitiesCoOccurrance(arg[1], arg[2])
	findAverage(arg[1])
	#toPlot = {}
	#toPlot['spot-head'] =  loadSpotEntDict(arg[1])
	#toPlot['spot-tail'] =  loadSpotEntDict(arg[2])
	#toPlot['ent-head'] =  loadSpotEntDict(arg[3])
	#toPlot['ent-tail'] =  loadSpotEntDict(arg[4])
	#plot2(toPlot)
