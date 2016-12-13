#!/usr/bin/awk -f

BEGIN {
	FS = " ";
	OFS=":";
}
{
	$2 = "\""$2"\""
	$3 = $3","
	print $1,$2,$3
}
