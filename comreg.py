#!/usr/bin/env python


import os


class Comreg:
    def __init__(self):
        self.running_dir = os.path.dirname(os.path.realpath(__file__))
        current_directory = self.running_dir + '/static/current_working_directory.txt'
        with open(current_directory, 'r') as f:
            self.working_directory = f.readline()
        self.help_file = self.running_dir + '/static/help_dialogue.txt'
        with open(self.help_file, 'w') as f:
            msg = """\tCurrent directory:\n\t{}\n\tUsage:\n""".format(
                    self.working_directory )
            f.write( msg )
        self.commands = {}
        self.help_message = ''

    def command(self, func):
        def get_name():
            name = func.__name__
            help_doc = func.__doc__
            return name, help_doc
        name, help_doc = get_name()
        self.commands['%s' % name] = func

        name = self._dname(name)
        dialogue = '\n{} {}\n'.format(name, help_doc)
        self.help_message += dialogue
        with open(self.help_file, 'a') as f:
            f.write( dialogue )
        return func

    def help_dialogue(self, func):

        name = 'help'
        help_text = func.__doc__
        self.commands[name] = func


        return func

    def _dname(self, name):
        add_spaces = 12 - (len(name))
        spaces = ' ' * add_spaces
        return name + spaces


if __name__ == '__main__':
    pass

