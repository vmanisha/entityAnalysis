EXPECTED_ARGS=2
E_BADARGS=65

if [ $# -ne $EXPECTED_ARGS ]
then
  echo "Usage: `basename $0` head/tail-enriched.json.gz spots-link-probability-distribution.tsv (frequency \t link-probability)"
  exit $E_BADARGS
fi

zcat $1 | jq -r '.spots[] | .linkProbability ' | awk '{print int($1*10)*10/100}' | sort | uniq -c | awk '{print $1"\t"$2}' > $2