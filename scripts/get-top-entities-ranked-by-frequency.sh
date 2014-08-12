EXPECTED_ARGS=5
E_BADARGS=65

if [ $# -ne $EXPECTED_ARGS ]
then
  echo "Usage: `basename $0` tail/head-spot-frequency-lp-e-commonness.tsv link-probability commonness size output"
  exit $E_BADARGS
fi

cat $1 | awk -F'	' -v t=$2 -v c=$3 '{if ($3>=t && $5>=c) print; }' | awk -F"	" '{print $4"\t"$2}' |  sort -k1  | datamash -g 1 sum 2 | sort -t'	' -nrk2 | head -$4 | cut -f 1 > $5

