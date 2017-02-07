#!/bin/bash

cd ~/Documents/notes/

# for i in 3 2 1; do
for (( i=3; i>0; i=i-1 )); do
	echo "Child: $i"
	sleep 1
done
echo "The second ps"
ps >> ps-output.txt
echo "Child: shut down the flaskapp?"
read
docker-compose down
echo "Child: flask app is down."


for (( i=2; i>0; i=i-1 )); do
	echo "Child: $i"
	sleep 1
done
