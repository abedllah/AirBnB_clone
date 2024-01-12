#!/usr/bin/python3

import cmd
from models.base_model import BaseModel
from models import storage
import shlex


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

    def do_create(self, arg):
         """Create a new instance of BaseModel, save it, and print its id."""
        args = shlex.split(arg)
        if not args or args[0] == "":
            print("** class name missing **")
        elif args[0] not in ["BaseModel"]:
            print("** class doesn't exist **")
        else:
            new_instance = BaseModel()
            new_instance.save()
            print(new_instance.id)

if __name__ == '__main__':
    HBNBCommand().cmdloop()
