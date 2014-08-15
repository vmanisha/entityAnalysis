import sys
#import ast
import json
<<<<<<< HEAD
<<<<<<< HEAD
from stats import loadEntDict
MENTION = 'mention'
QUERY = 'query'
ENTITY = 'entity'
WIKI = 'wikiname'
CAND = 'candidates'
SPOTS = 'spots'
FREQ = 'frequency'

class SpotManager :
	
	def __init__(self):
		self.spotDict = {}
		self.spotCount = {}
	
	def addSpot(self, spotObj, freq):
		if spotObj.spot not in self.spotDict:
			self.spotDict[spotObj.spot] = spotObj
			self.spotCount[spotObj.spot] = 0
		self.spotCount[spotObj.spot]+=freq
	
	#def delSpot(self, spotObj):
	
	def getSpotObj(self, spotName):
		if spotName in self.spotDict:
			return self.spotDict[spotName]
	
	def printSpotCounts(self):
		sortBySpotCount = sorted(self.spotCount.items(),reverse=True, key = lambda x : x[1] )
		for entry in sortBySpotCount:
			print entry[0].encode('utf-8','ignore'),'\t',entry[1]
			
	def printSpotEntityCounts(self):
		entCount = {}
		for spotObj in self.spotDict.values():
			#print spotObj.spot,'\t',spotObj.entities
			entCount[spotObj.entities] = entCount.setdefault(spotObj.entities,0) + 1.0
		for entry, value in entCount.items():
			print entry,'\t',value
				
class Spot:
	#hold spot info
	def __init__(self,jsonObj):
		#self.spot = jsonObj[MENTION]
		self.spot = jsonObj[CAND][0][WIKI]
		if jsonObj[CAND]:
			self.entities = len(jsonObj[CAND])
	def addSpot(self, spotObj):
		if spotObj.spot not in self.spotDict:
			self.spotDict[spotObj.spot] = spotObj
			self.spotCount[spotObj.spot] = 0
		self.spotCount[spotObj.spot]+=1
	
	#def delSpot(self, spotObj):
		
	def printSpotCounts(self):
		sortBySpotCount = sorted(self.spotCount.items(),reverse=True, key = lambda x : x[1] )
		for entry in sortBySpotCount:
			print entry[0],'\t',entry[1]
		
	def getEntCount(self):
		return len(self.entity)

class CoOccurManager:
	
	def __init__(self):
		self.coDict = {}
	
	def addSpots(self,spot1, spot2,val):
		a = ''
		b = ''
		if spot1 <= spot2:
			a = spot1
			b = spot2
		else:
			a = spot2
			b = spot1
		#spot 1 spot 2 freq
		if a not in self.coDict:
			self.coDict[a] = {}
		
		self.coDict[a][b]  = self.coDict[a].setdefault(b,0.0) + val
	
	def printCoStats(self):
		for st1, slist in self.coDict.items():
			for st2, freq in slist.items():
				print st1.encode('utf-8','ignore'),'\t', st2.encode('utf-8','ignore'),'\t', freq 	


	
#arg[1] = filename to analyze
def main(argv):
	spotMan = SpotManager()
	#coMan = CoOccurManager()
	
	headEnt = loadEntDict(argv[2])
	
	queryEntStats = {}
	qid = 0
	for line in open(argv[1],'r'):
		taggedDict = json.loads(line.strip())
		spotDict = taggedDict[SPOTS]
		spotList = []
		freq = taggedDict[FREQ]
		#query = taggedDict[QUERY]
		if spotDict:
			for spot in spotDict:
				spotObj = Spot(spot)
				spotList.append(spotObj.spot)
				spotMan.addSpot(spotObj,freq)
		#get the co-occurance stats
		qid += 1
		#if len(spotList) > 1:
		queryEntStats[qid]= {'h':0.0,'t':0.0,'hdist':{}}
		for i in range(len(spotList)):
			ent1 = spotList[i]
			if ent1 in headEnt:
				queryEntStats[qid]['h']+= 1.0
				quant = headEnt[ent1]
				queryEntStats[qid]['hdist'][quant] = queryEntStats[qid]['hdist'].setdefault(quant,0.0)+1.0
			else:
				queryEntStats[qid]['t']+= 1.0
		#if qid in queryEntStats:
		#	if queryEntStats[qid]['t'] == queryEntStats[qid]['h']:
		#		print query, len(spotList), spotList
			
			'''for i in range(len(spotList)-1):
				for j in range(i+1, len(spotList)):
					ent1 = spotList[i]
					ent2 = spotList[j]
					if ent1 in headEnt and ent2 in headEnt:
						queryEntStats[qid]['hh']+=1.0
					elif ent1 in headEnt:
						quant = headEnt[ent1]
						queryEntStats[qid]['ht'][quant] = queryEntStats[qid]['ht'].setdefault(quant,0.0)+1.0
					elif ent2 in headEnt:
						quant = headEnt[ent2]
						queryEntStats[qid]['ht'][quant] = queryEntStats[qid]['ht'].setdefault(quant,0.0)+1.0
					else:
						queryEntStats[qid]['tt']+= 1.0
					#print i , j
					#coMan.addSpots(spotList[i],spotList[j],freq)
			'''
	#oFile = open(argv[3],'w')
	for entry, stats in queryEntStats.items():
		#total = sum(stats.values())
		print entry,'\t',  stats['h'],'\t',stats['t'],'\t', str(stats['hdist'])
		#oFile.write(entry+'\t'+str( stats['h'])+'\t'+str(stats['t'])+'\t'+ str(stats['hdist']))
			
		
		
	#print the pairs and freq
	#coMan.printCoStats()
	#print the ent count and freq
	#spotMan.printSpotCounts()
	#spotMan.printSpotEntityCounts()


if __name__ == '__main__':
	main(sys.argv)


