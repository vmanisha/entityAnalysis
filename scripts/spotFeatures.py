import sys
#import ast
import json
MENTION = 'mention'
QUERY = 'query'
ENTITY = 'entity'
WIKI = 'wikiname'
CAND = 'candidates'
SPOTS = 'spots'

class SpotManager :
	
	def __init__(self):
		self.spotDict = {}
		self.spotCount = {}
	
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
		
class Spot:
	#hold spot info
	def __init__(self,jsonObj):
		self.spot = jsonObj[MENTION]
		#store entity:wikiname
		#self.entity = {}
		#for entObj in json[CAND]:
		#	self.entity[entObj[ENTITY]] = entObj[WIKI]
		
	def getEntCount(self):
		return len(self.entity)

#arg[1] = filename to analyze
def main(argv):
	spotMan = SpotManager()
	for line in open(argv[1],'r'):
		taggedDict = json.loads(line.strip())
		spotDict = taggedDict[SPOTS]
		#query = taggedDict[QUERY]
		if spotDict:
			for spot in spotDict:
				spotObj = Spot(spot)
				spotMan.addSpot(spotObj)
	spotMan.printSpotCounts()


if __name__ == '__main__':
	main(sys.argv)