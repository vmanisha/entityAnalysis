EXPECTED_ARGS=2
E_BADARGS=65

if [ $# -ne $EXPECTED_ARGS ]
then
  echo "Usage: `basename $0` head/tail-enriched.json.gz spots-per-query-distribution.tsv (frequency \t number-of-spots)"
  exit $E_BADARGS
fi

zcat $1 | jq '.numberOfSpots' | sort | uniq -c | sort -nk2 | awk '{print $1"\t"$2}' > $2