#!/bin/bash

num_writer() {

if [ $# -eq 1 ]
then
	while [ "$count" -le "$num_rands" ] 
	do
		shuf -i 0-32767 -n 1 >> rands_"$num_rands".txt
		(( count++ ))
	done
	sort -nr rands_"$num_rands".txt > rands_"$num_rands"_sort.txt

	largest_value=`head -1 rands_"$num_rands"_sort.txt`
	smallest_value=`tail -1 rands_"$num_rands"_sort.txt`

	echo You requested $num_rands numbers '['between 0 and 32767']'
	echo The largest value generated was $largest_value
	echo The smallest value generated was $smallest_value
	awk '{ total += $1 } END {print "The average value generated was " total/NR }' rands_"$num_rands"_sort.txt

	echo You requested $num_rands numbers '['between 0 and 32767']' >> rands_"$num_rands".txt
	echo The largest value generated was $largest_value >> rands_"$num_rands".txt
	echo The smallest value generated was $smallest_value >> rands_"$num_rands".txt
	awk '{ total += $1 } END {print "The average value generated was " total/NR }' rands_"$num_rands"_sort.txt >> rands_"$num_rands".txt

fi

if [ "$#" -gt 2 ]
then	

	while [ "$count" -le "$num_rands" ] 
	do
		
		(( count++ ))
		shuf -i "$min"-"$max" -n 1 >> rands_"$num_rands".txt
	done
	sort -nr rands_"$num_rands".txt > rands_"$num_rands"_sort.txt
	largest_value=`head -1 rands_"$num_rands"_sort.txt`
	smallest_value=`tail -1 rands_"$num_rands"_sort.txt`

	echo You requested $num_rands numbers '['between $min and $max']'
	echo The largest value generated was $largest_value
	echo The smallest value generated was $smallest_value
	awk '{ total += $1 } END {print "The average value generated was " total/NR }' rands_"$num_rands"_sort.txt

	echo You requested $num_rands numbers '['between $min and $max']' >> rands_"$num_rands".txt
	echo The largest value generated was $largest_value >> rands_"$num_rands".txt
	echo The smallest value generated was $smallest_value >> rands_"$num_rands".txt
	awk '{ total += $1 } END {print "The average value generated was " total/NR }' rands_"$num_rands"_sort.txt >> rands_"$num_rands".txt


fi

}




num_rands=$1
min=$2
max=$3

count=1


num_writer "$@"