#!/usr/bin/env bash

SESSION_NAME='notes'

for (( i=5; i>0; i=i-1 )); do
    echo "killing notes session in $i seconds"
    sleep 1
done

cd ~/Documents/notes/
docker-compose down

tmux kill-session -t $SESSION_NAME
