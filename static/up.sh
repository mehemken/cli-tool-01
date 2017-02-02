#!/usr/bin/env bash

DIR= $1
SESSION_NAME= 'notes'
FIRST_WINDOW_NAME= 'docker'

cd $DIR

tmux start-server
tmux new-session -d -s $SESSION_NAME -n $FIRST_WINDOW_NAME

tmux attach -t$SESSION_NAME
