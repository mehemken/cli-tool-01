#!/usr/bin/env python


class Comreg:
    def __init__(self):
        with open('help_dialogue.txt', 'w') as f:
            msg = '\nUsage\n-----'
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
        dialogue = '\n{}\t{}\n'.format(name, help_doc)
        self.help_message += dialogue
        with open('help_dialogue.txt', 'a') as f:
            f.write( dialogue )
        return func

    def help_dialogue(self, func):

        name = 'help'
        help_text = func.__doc__
        self.commands[name] = func


        return func

    def _dname(self, name):
        add_spaces = 16 - (len(name))
        spaces = ' ' * add_spaces
        return name + spaces


if __name__ == '__main__':
    pass

