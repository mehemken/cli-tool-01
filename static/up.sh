#!/usr/bin/env bash

DIR=$1
SESSION_NAME='notes'

######################################################
# Start the flaskapp

cd ~/Documents/notes/
docker-compose up -d &
FLASK_PID=$!

######################################################
# Start the firefox

firefox localhost:42424 2> /dev/null &
FIREFOX_PID=$!

######################################################
# Start the tmux server
cd $DIR
tmux start-server
tmux new-session -d -s $SESSION_NAME

tmux new-window -t $SESSION_NAME:1 -n work

tmux send-keys -t $SESSION_NAME:0 'docker ps' enter

tmux split-window -t $SESSION_NAME:1 -v
tmux send-keys -t $SESSION_NAME:1 'source activate jupyter; clear' enter

tmux select-window -t $SESSION_NAME:1
tmux attach -t $SESSION_NAME

######################################################
# End the tmux session

wait $FLASK_PID
tmux kill-session -t $SESSION_NAME
