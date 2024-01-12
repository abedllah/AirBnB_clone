#!/usr/bin/python3

import cmd

class HBNBCommand(cmd.Cmd):
    """Interactive command-line console for HBNB data management"""

    prompt = '(hbnb) '

    def do_EOF(self, arg):
        """Exit the console"""
        return True

    def emptyline(self):
        """Ignore empty lines"""
        return False

    def do_quit(self, arg):
        """Quit the console"""
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
