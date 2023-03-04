#!/bin/bash

for line in $(cat input.txt)
do

	wget https://www.youtube.com/results?search_query=$line -O searchResults.html
	grep -oP '(?<=videoId":")[^"]*' searchResults.html | head -n1 >> videoId.txt

done

rm searchResults.html