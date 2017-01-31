#!/usr/bin/env python


class Lnotes:
    def __init__(self):
        self.commands = {}

    def register_to_list(self, func):
        def inner_func():
            item = func.__name__
            return item
        item = inner_func()
        self.commands['%s' % item] = func
        return 0


if __name__ == '__main__':
    pass

