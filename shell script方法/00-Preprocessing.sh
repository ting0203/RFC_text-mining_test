#/bin/bash

grep -v "^#" rfc.list \
| grep -v "Not Issued" \
| sed -r 's/^([0-9]+).*\[(.*)\].*$/\1\2/g' \
> rfc.time

awk '{print $1,$NF;}' rfc.time \
> rfc.year

grep -v "^#" rfc.list \
| grep "(Status: " \
| sed -r 's/^([0-9]+).*\(Status: ([ A-Za-z]+)\).*$/\1 \2/g' \
> rfc.status

grep -v "^#" rfc.list \
| grep "(Obsoletes" \
| sed -r 's/^([0-9]+).*\((Obsoletes[ ,RFCIEN0-9]+)\).*$/\1 \2/g' \
> rfc.obsolete

grep -v "^#" rfc.list \
| grep "(Updates" \
| sed -r 's/^([0-9]+).*\((Updates[ ,RFCIEN0-9]+)\).*$/\1 \2/g' \
> rfc.update

grep -v "^#" rfc.list \
| grep "(Obsoleted" \
| sed -r 's/^([0-9]+).*\((Obsoleted-By[ ,RFCIEN0-9]+)\).*$/\1 \2/g' \
| sed 's/RFC//g' \
> rfc.obsoleted-by

grep -v "^#" rfc.list \
| grep "(Updated" \
| sed -r 's/^([0-9]+).*\((Updated-By[ ,RFCIEN0-9]+)\).*$/\1 \2/g' \
| sed 's/RFC//g' \
> rfc.updated-by

join -a 1 rfc.year rfc.obsoleted-by \
| join -a 1 - rfc.updated-by \
| join -a 1 - rfc.obsolete \
| join -a 1 - rfc.update \
| sed 's/,//g' \
| sed 's/RFC//g' \
> rfc.history

sed -E 's/IEN[0-9]+//g' rfc.history \
> rfc.history-noIEN
