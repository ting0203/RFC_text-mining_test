#!/bin/sh

awk -f dotgen.awk $1.v3.short \
| dot -Tpng \
> $1.v4.png
