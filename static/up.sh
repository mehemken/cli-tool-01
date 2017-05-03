#!/usr/bin/env bash

DIR=$1
SESSION_NAME='notes'

######################################################
# Start the tmux server
cd $DIR
tmux start-server
tmux new-session -d -s $SESSION_NAME -n work

tmux select-window -t $SESSION_NAME:0
tmux attach -t $SESSION_NAME
