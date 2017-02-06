#!/usr/bin/env bash

for (( i=5; i>0; i=i-1 )); do
    echo "killing notes session in $i seconds"
    sleep 1
done

cd ~/Documents/notes/
docker-compose down
