#!/bin/sh

echo $@ | sed 's/ /\n/g' | sort -n | uniq > rfc.temp.1
count=1
echo "$count"
while [ $count -gt 0 ]; do
	join rfc.temp.1 rfc.history-noIEN \
	| sed -E 's/(Obsoleted|Updated)-By//g' \
	| sed -E 's/(Obsoletes|Updates)//g' \
	| awk '{$2=""; print;}' \
	| sed -E 's/ +/\n/g' \
	| sort -n \
	| uniq \
	> rfc.temp.2
	count=`diff -B rfc.temp.1 rfc.temp.2 | wc -l | awk '{print $1;}'`
	echo $count
	cp rfc.temp.2 rfc.temp.1
done
join rfc.temp.1 rfc.history > rfc.final.long
join rfc.temp.1 rfc.year \
| join -a 1 - rfc.obsoleted-by \
| join -a 1 - rfc.updated-by \
| sed 's/,//g' \
> rfc.final.short

