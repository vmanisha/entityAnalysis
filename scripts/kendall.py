#!/usr/local/opt/python/bin/python2.7

import sys
import scipy as sp
import scipy.stats as stats
import scipy.spatial.distance as distance

def jaccard_distance(a, b):
    a=set(a)
    b=set(b)
    c = a.intersection(b)
    return float(len(c)) / (len(a) + len(b) - len(c))
    
def main():
    size = int(sys.argv[3])
    lp = float(sys.argv[4])
    commonness = float(sys.argv[5])
    
    with open(sys.argv[1]) as input1:
        with open(sys.argv[2]) as input2:
           
            x1 = map(lambda x: x.strip(), input1.readlines())
            x2 = map(lambda x: x.strip(), input2.readlines())
            size1 = len(x1)
            size2 = len(x2)
            x1 = x1[:size]
            x2 = x2[:size]
            tau, p_value = stats.kendalltau(x1, x2)
            #print x1,x2
            jaccard = jaccard_distance(x1,x2)
            print str(lp)+"\t"+str(commonness)+"\t"+str(size)+"\t"+str(size1)+"\t"+str(size2)+"\t"+str(tau)+"\t"+str(p_value)+"\t"+str(jaccard)

if __name__ == "__main__":
    main()