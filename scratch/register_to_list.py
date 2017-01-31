#!/usr/bin/env python

from lnotes_lib import Lnotes


foobar = Lnotes()

@foobar.register_to_list
def my_func():
    """That func tho..."""
    pass

@foobar.register_to_list
def the_second():
    """This is the_second. It does nothing."""
    pass

@foobar.register_to_list
def king_code():
    """This is king_code. It does nothing."""
    pass

@foobar.register_to_list
def salamander():
    """This is salamander. It does nothing."""
    pass

@foobar.register_to_list
def help_text():
    msg = ''
    with open('help_dialogue.txt', 'r') as f:
        for line in f:
            msg += line
    return msg



if __name__ == '__main__':
    print(help_text)
