#!/bin/bash

cd ~/Documents/notes/

docker-compose up -d &
pid=$!

echo "The first ps"
ps > ps-output.txt
echo "Parent: The flaskapp is running (PID $pid)..."
~/Documents/code-gitless/tmux/lnotes/scratch/async-flaskapp/stop-flask.sh
wait $pid


for (( i=2; i>0; i=i-1 )); do
	echo "Parent: $i"
	sleep 1
done
echo "The third ps"
ps >> ps-output.txt
echo "Parent: The flaskapp was terminated."

cat ps-output.txt
