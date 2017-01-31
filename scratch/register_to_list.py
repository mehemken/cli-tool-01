#!/usr/bin/env python

from lnotes_lib import Lnotes


foobar = Lnotes()


@foobar.register_to_list
def my_func():
    pass

@foobar.register_to_list
def the_second():
    pass

@foobar.register_to_list
def king_code():
    pass

@foobar.register_to_list
def salamander():
    pass


if __name__ == '__main__':
    print('')
    for key, val in foobar.commands.items():
        print(key, val)
    print('')

