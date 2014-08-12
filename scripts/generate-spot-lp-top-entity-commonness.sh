EXPECTED_ARGS=2
E_BADARGS=65

if [ $# -ne $EXPECTED_ARGS ]
then
  echo "Usage: `basename $0` head/tail-enriched.json.gz spots-lp-top-entity-commonness"
  exit $E_BADARGS
fi

zcat $1 | jq -r '.frequency as $f | .spots[] | "\(.mention)\t\($f)\t\(.linkProbability)\t\(.candidates[0].wikiname)\t\(.candidates[0].commonness)" ' > $2
#zcat $1 | jq -r ' .spots[] | "\(.mention)\t\(.linkProbability)\t\(.candidates[0].wikiname)\t\(.candidates[0].commonness)" '> $2
