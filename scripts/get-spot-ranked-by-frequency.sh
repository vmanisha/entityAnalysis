EXPECTED_ARGS=4
E_BADARGS=65

if [ $# -ne $EXPECTED_ARGS ]
then
  echo "Usage: `basename $0` tail/head-spot-frequency-lp-e-commonness.tsv link-probability size output"
  exit $E_BADARGS
fi

cat $1 | awk -F'	' -v t=$2 '{if ($3>t) print; }' | cut -f 1,2 |  sort -k1  | datamash -g 1 sum 2 | sort -t'	' -nrk2 | head -$3 | cut -f 1 > $4

