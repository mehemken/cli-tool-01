#!/bin/bash

git add .
git status
echo "Are you sure? yes/no"
read CHOICE

if [ "$CHOICE" == "yes" ]; then
    echo "Ok. You asked for it."
    echo "building..."
    TIMESTAMP="$(date)"
    git commit -am "Auto commit: $TIMESTAMP"
    cat alpha.py > prod.py
elif [ "$CHOICE" == "no" ]; then
    echo "You said no."
    echo "Build aborted."
else
    echo "Please say yes/no."
    echo "Build aborted."
    git reset
fi
