#!/bin/bash


DIR=(~/Documents/code-gitless/python/fluent-python/part5/ch14/)
FILE=(~/Documents/notes/posts/fluent-python-control-flow.md)

echo ""
echo "  Source file of this utility is:"
echo "  ~/Documents/code-gitless/tmux/snotes.sh"
echo ""
echo "  snotes stands for"
echo "  s[tudy]notes"

cd $DIR

tmux start-server
tmux new-session -d -s $1 -n notes
tmux new-window -t$1:1 -n work

tmux send-keys -t$1:0 'cd ~/Documents/notes/; clear' enter
tmux send-keys -t$1:0 'fig up -d' enter
tmux send-keys -t$1:0 'docker ps' enter
tmux send-keys -t$1:0 'echo "waiting for docker to start" & sleep 1' enter
tmux send-keys -t$1:0 'evince ~/Downloads/Fluent_Python.pdf 2> /dev/null & clear' enter
tmux send-keys -t$1:0 'firefox localhost:42424 2> /dev/null & clear' enter

tmux send-keys -t$1:1 "vim $FILE" enter
tmux send-keys -t$1:1 "G" enter
tmux split-window -t$1:1 -v
tmux send-keys -t$1:1 'source activate jupyter; clear' enter
tmux select-window -t$1:0

tmux attach -t $1

sleep .123

tmux select-window -t$1:1

