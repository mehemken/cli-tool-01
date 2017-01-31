#!/usr/bin/env python

"""
This Simple tool will start my tmux session lnotes.
The session will start up my docker containers that 
run my notes app as well as the various tmux windows
and panes that I like. I like to have two windows
where the second window is split into two panes.

The tool will have two options. The first one will
start the session and the second option will end it.
The end sequence will always include a git commit.
"""


import sys
from comreg import Commands


app = Commands()


##### commands


@app.help_dialogue
def help_text():
    msg = """
Usage:
    $ lnotes [OPTIONS]

--- Options:
up                starts the session

down              ends the session

set [FILEPATH]    sets the  working directory of
                  the next session.
"""
    sys.stdout.write( msg )
    sys.exit()


@app.command
def up():
    sys.stdout.write('This starts the program.\n')
    # run the start bash script


@app.command
def down():
    sys.stdout.write('This ends the program.\n')
    # run the end bash script


@app.command
def set():
    sys.stdout.write('This sets the working directory for next lnotes session.\n')
    # run the end bash script


##### main


def handle_args():
    """
    Returns function object corresponding to option given.
    """
    option = None
    if len(sys.argv) < 2:
        return help_text
    elif sys.argv[1] not in app.commands:
        sys.stdout.write( msg )
        return help_text
    else:
        msg = 'Argument given: {}\n'.format( sys.argv[1] )
        sys.stdout.write( msg )
        option = app.commands[ sys.argv[1] ]
    return option


def main():
    sys.stdout.write('\nWelcome to l(ocal)notes!\n')
    return handle_args()


if __name__ == '__main__':

    option = main()
    if callable(option):
        option()
    else:
        print(type(option))
        print(option)
        sys.exit('Option is not callable')
