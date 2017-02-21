#!/usr/bin/env bash

DIR=$1
SESSION_NAME='notes'

######################################################
# Start the flaskapp

cd ~/Documents/notes/
docker-compose up -d &
FLASK_PID=$!
echo "flaskapp running (PID $FLASK_PID)"

######################################################
# Start the firefox

STATUS=""

echo "Checking status of flaskapp..."
while [ "$STATUS" != "ready" ]; do
	STATUS=$(curl localhost:42424/ready --silent | jq '.status' | sed 's/\"//g' )
	if [ "$STATUS" == "ready" ]; then
        echo "flaskapp is ready"
		firefox localhost:42424 2> /dev/null &
		FIREFOX_PID=$!
	else
        echo "flaskapp is not ready"
		sleep 1
	fi
done


######################################################
# Start the tmux server
cd $DIR
tmux start-server
tmux new-session -d -s $SESSION_NAME -n work

tmux split-window -t $SESSION_NAME:0 -v

tmux select-window -t $SESSION_NAME:0
tmux attach -t $SESSION_NAME

