#!/usr/bin/env python


class Lnotes:
    def __init__(self):
        with open('help_dialogue.txt', 'w') as f:
            f.write('\nWelcome to the help dialogue!\n{}'.format('#'*29))
        self.commands = {}
        self.help_dialogue = ''

    def register_to_list(self, func):
        def inner_func():
            name = func.__name__
            help_text = func.__doc__
            return name, help_text

        name, help_text = inner_func()

        self.commands['%s' % name] = func

        name = self.dname(name)
        dialogue = '\n{}\t{}\n'.format(name, help_text)
        self.help_dialogue += dialogue
        with open('help_dialogue.txt', 'a') as f:
            f.write( dialogue )

        return func()

    def dname(self, name):
        number_of_spaces_to_add = 16 - len(name)
        spaces = ' ' * number_of_spaces_to_add
        dname = name + spaces
        return dname


if __name__ == '__main__':
    pass
