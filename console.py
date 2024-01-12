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
            
    def do_show(self, arg):
        """Print the string representation of an instance."""
        args = shlex.split(arg)
        if not args or args[0] == "":
            print("** class name missing **")
        elif args[0] not in ["BaseModel"]:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            if key in storage.all():
                print(storage.all()[key])
            else:
                print("** no instance found **")
                
    def do_destroy(self, arg):
        """Delete an instance based on class name and id."""
        args = shlex.split(arg)
        if not args or args[0] == "":
            print("** class name missing **")
        elif args[0] not in ["BaseModel"]:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            if key in storage.all():
                del storage.all()[key]
                storage.save()
            else:
                print("** no instance found **")
                
    def do_all(self, arg):
        """Print all string representations of instances."""
        args = shlex.split(arg)
        if args and args[0] not in ["BaseModel"]:
            print("** class doesn't exist **")
        else:
            instances = []
            for key, value in storage.all().items():
                if not args or args[0] == "" or args[0] == value.__class__.__name__:
                    instances.append(str(value))
            print(instances)
            
    def do_update(self, arg):
        """Update an instance based on class name and id."""
        args = shlex.split(arg)
        if not args or args[0] == "":
            print("** class name missing **")
        elif args[0] not in ["BaseModel"]:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif "{}.{}".format(args[0], args[1]) not in storage.all():
            print("** no instance found **")
        elif len(args) < 3:
            print("** attribute name missing **")
        elif len(args) < 4:
            print("** value missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            instance = storage.all()[key]
            attribute_name = args[2]
            value = args[3]
            if hasattr(instance, attribute_name):
                attribute_type = type(getattr(instance, attribute_name))
                setattr(instance, attribute_name, attribute_type(value))
                storage.save()

if __name__ == '__main__':
    HBNBCommand().cmdloop()
