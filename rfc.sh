#!/bin/sh

echo $1

#過濾含Page那行的文字，RFC xxx開頭，內容含+-，多個...開頭，數字.
grep -v "Page" rfc$1.txt \
| grep -v "^RFC $1" \
| grep -v "+-"  \
| sed -E 's/\.\.+[0-9]+/ /g' \
| sed -E 's/[0-9+]\.//g'\
> rfc$1_1.txt

#echo  rfc$1_nltk_test.py

#執行python
#python rfc$1_nltk_test.py 