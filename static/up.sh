#!/usr/bin/env bash

DIR=$1
SESSION_NAME='notes'

cd $DIR

tmux start-server
tmux new-session -d -s $SESSION_NAME

tmux new-window -t $SESSION_NAME:1 -n work

tmux send-keys -t $SESSION_NAME:0 'cd ~/Documents/notes/; clear' enter
tmux send-keys -t $SESSION_NAME:0 'fig up -d & sleep 1' enter
tmux send-keys -t $SESSION_NAME:0 'firefox localhost:42424 2> /dev/null & clear' enter

tmux send-keys -t $SESSION_NAME:0 'docker ps' enter

tmux split-window -t $SESSION_NAME:1 -v
tmux send-keys -t $SESSION_NAME:1 'source activate jupyter; clear' enter

tmux select-window -t $SESSION_NAME:1
tmux attach -t $SESSION_NAME
