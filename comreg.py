#!/usr/bin/env python


class Commands:
    def __init__(self):
        self.commands = {}

    def command(self, func):
        def get_name():
            item = func.__name__
            return item
        item = get_name()
        self.commands['%s' % item] = func
        return 0

    def help_dialogue(self, func):
        self.commands['help'] = func
        return func


if __name__ == '__main__':
    pass

