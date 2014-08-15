#!/usr/bin/env bash

LONG_TAIL=tail-spot-frequency-lp-e-commonness.tsv
HEAD=head-spot-frequency-lp-e-commonness.tsv
LONG_INTERSECT=tail-head-intersection-spot-lp-e-commonness.tsv
mkdir -p results

echo "" > results/kendall-jaccard-head-tail-spots.txt 
echo "" > results/kendall-jaccard-head-tail-intersect-spots.txt
echo "" > results/kendall-jaccard-head-tail-entities.txt 
echo "" > results/kendall-jaccard-head-tail-intersect-entities.txt 


for lp in 0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9 1;
do
	for commonness in 0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9 1;
	do
		echo $lp, $commonness
		for f in $LONG_TAIL $HEAD $LONG_INTERSECT;
		do
			./scripts/get-spot-ranked-by-frequency.sh data/$f $lp 10000 /tmp/s-$f
			./scripts/get-top-entities-ranked-by-frequency.sh data/$f $lp $commonness 10000 /tmp/e-$f
		done
		
		for size in 5000 1000 500 100 50;
		 	do
				echo $lp,$commonness,$size
				scripts/kendall.py /tmp/s-$HEAD /tmp/s-$LONG_TAIL  $size $lp $commonness >> results/kendall-jaccard-head-tail-spots.txt
				scripts/kendall.py /tmp/s-$HEAD /tmp/s-$LONG_INTERSECT  $size $lp $commonness >>  results/kendall-jaccard-head-tail-intersect-spots.txt
				
				scripts/kendall.py /tmp/e-$HEAD /tmp/e-$LONG_TAIL $size $lp $commonness >>  results/kendall-jaccard-head-tail-entities.txt 

				scripts/kendall.py /tmp/e-$HEAD /tmp/e-$LONG_INTERSECT $size $lp $commonness  >>  results/kendall-jaccard-head-tail-intersect-entities.txt				
				
				
			done
	done
done
