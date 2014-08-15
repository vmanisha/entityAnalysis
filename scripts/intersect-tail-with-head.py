#!/usr/bin/env python

import sys


def main():
    head_queries = {}
    with open(sys.argv[1]) as head:
        for line in head:
            head_queries[line.split("\t")[0]]=1
    with open(sys.argv[2]) as tail:
        with open(sys.argv[3],"w") as output: 
            for line in tail: 
                if (line.split("\t")[0] in head_queries):
                    output.write(line)
        

if __name__ == "__main__":
    main()