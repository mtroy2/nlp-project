#!/bin/bash

for (( i = 1; i < 493; ++i )); do
  f="$( printf "%03d.txt" "$i" )"
  sed -i '1,2d' "$f"
  sed -i ':a;N;$!ba;s/\n//g' "$f"
  sed -i 's/  / /g' "$f"
done
