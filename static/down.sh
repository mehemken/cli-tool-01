#!/usr/bin/env bash

SESSION_NAME='notes'

for (( i=3; i>0; i=i-1 )); do
    echo "killing notes session in $i seconds"
    sleep 1
done

cd ~/Documents/notes/
docker-compose down

tmux kill-session -t $SESSION_NAME


##############################
# Git stuff


function set_to_branch_devel () {
    if [ "$CURRENT_BRANCH" != "devel" ]; then
        git checkout devel
    fi
}

function reset_branch_devel () {
    set_to_branch_devel
    git reset
}


CURRENT_BRANCH=$(git symbolic-ref HEAD | sed 's!refs\/heads\/!!')
set_to_branch_devel


git add .
git status
echo "Are you sure? yes/no"
read CHOICE

if [ "$CHOICE" == "yes" ]; then
    echo "Ok. You asked for it."
    echo "building..."
    TIMESTAMP="$(date)"
    git commit -am "Auto commit: $TIMESTAMP"
elif [ "$CHOICE" == "no" ]; then
    echo "You said no."
    echo "Build aborted."
    git reset
    exit $?
else
    echo "Please say yes/no."
    echo "Build aborted."
    exit $?
fi

echo "Merge? yes/no"
read MERGE_CHOICE

if [ "$MERGE_CHOICE" == "yes" ]; then
    echo "Ok. You asked for it again."
    echo "Merging..."
    git checkout master
    git merge devel
    git checkout devel
elif [ "$MERGE_CHOICE" == "no" ]; then
    echo "You said no."
    echo "Merge aborted."
    exit $?
else
    echo "Please say yes/no."
    echo "Merge aborted."
    exit $?
fi
