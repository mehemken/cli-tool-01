# Command line tool

This command line tool controls the flask container in my other repo, localnotes-md. Essentially, the goal of this thing is to launch and stop the docker container and a tmux session in the project folder of my choice.

The main application is written in `alpha.py`. When I want to deploy, I use `build.sh`, which adds the changes to `prod.py`.

`comreg.py` is short for command re-- hrm... I forgot the word I was thinking of when I wrote that. This script is a library that provides a nice set of decorators to use in `alpha.py`.

The `static` folder contains a few bash scripts. I originally wrote a lot of the functionality of the CLI args in bash. That is to say, my Python bumped that to some bash scripts. I've since decided that most things are best done in Python. I've been moving a lot of the functionality from those bash scripts to `alpha.py`.
