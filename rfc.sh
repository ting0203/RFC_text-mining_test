#!/bin/sh

echo $1
grep -v "Page" rfc$1.txt | grep -v "^RFC $1" > rfc$1_1.txt
