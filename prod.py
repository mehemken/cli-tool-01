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
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)


import sys, os
import shlex
import subprocess
from comreg import Comreg
import requests
import webbrowser
import time
from threading import Thread, Event


app = Comreg()


##### commands


@app.help_dialogue
def help_text():
    sys.stdout.write('\nWelcome to l(ocal)notes!\n\n')
    msg = ''
    with open(app.help_file, 'r') as f:
        for line in f:
            msg += line
        msg += '\n'
    sys.stdout.write( msg )
    return msg

@app.command
def up():
    """Starts a new tmux session with the notes app and several windows."""

    def start_docker():
        DOCKER_ROOT = os.path.abspath('~/Documents/notes/')
        os.chdir(DOCKER_ROOT)
        cmd = shlex.split('docker-compose up -d')
        subprocess.call(cmd)

    def start_tmux():
        up_file = app.running_dir + '/static/up.sh'
        subprocess.call( ['bash', up_file, app.working_directory] )
        logger.info('Tmux launched.')

    def start_browser():
        # Redo the webbrowser open with python
        for _ in range(10):
            try:
                response = requests.get('http://localhost:42424')
            except:
                logger.exception('Site is not ready yet')
                time.sleep(0.5)
            else:
                webbrowser.open('http://localhost:42424')
                break

    start_tmux()

    launch_browser = Thread(target=start_browser)
    launch_docker = Thread(target=start_docker)
    launch_browser.start()
    launch_docker.start()



@app.command
def down():
    """Shuts down the notes app, git commits and ends the tmux session."""
    down_file = app.running_dir + '/static/down.sh'
    subprocess.call( ['bash', down_file] )

@app.command
def set():
    """This sets the working directory for next lnotes session."""
    def set_given_dir(result):
        dir_path = os.path.dirname(os.path.realpath(__file__))
        current_directory = dir_path + '/static/current_working_directory.txt'
        with open(current_directory, 'w') as f:
            f.write(result)
        sys.stdout.write( 'New wd: {}\n'.format( result ) )
    try:
        dot = sys.argv[2]
    except:
        print('Not enough args. lnotes set requires args.')
    if dot == '.':
        result = os.getcwd()
        set_given_dir(result)
    elif sys.argv[2]:
        result = sys.argv[2]
        set_given_dir(result)
    else:
        result = help_text()
    return result


##### main


def handle_args():
    """
    Returns function object corresponding to option given.
    """
    option = None
    if len(sys.argv) < 2:
        return help_text
    elif sys.argv[1] not in app.commands:
        return help_text
    else:
        msg = '--- lnotes: {} ---\n'.format( sys.argv[1] )
        msg.upper()
        sys.stdout.write( msg )
        option = app.commands[ sys.argv[1] ]
    return option


def main():
    option = handle_args()
    if callable(option):
        result = option()
    return result


if __name__ == '__main__':

    option = main()
    print()
