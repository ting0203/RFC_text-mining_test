#/bin/bash
echo $1
grep -v '^#' $1.v1 \
| sed 's/,/ /g' \
| awk '{print $2;}' \
| sort -n \
| uniq \
> $1.v2

./01-Expand.sh `cat $1.v2`
mv rfc.final.short $1.v3.short
mv rfc.final.long  $1.v3.long
awk '{print $1;}' $1.v3.short | diff - $1.v2
