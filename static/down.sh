#!/usr/bin/env bash


SESSION_NAME='notes'

tmux send-keys -t $SESSION_NAME:0 'fig down' enter

for i in 5 4 3 2 1
do
    echo "killing notes session in $i seconds"
    sleep 1
done

docker ps

tmux kill-session -t $SESSION_NAME
