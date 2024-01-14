#!/usr/bin/python3

import cmd
from models.base_model import BaseModel
from models import storage
import shlex
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """Interactive command-line console for HBNB data management"""

    prompt = '(hbnb) '

    Classes = {
        "BaseModel": BaseModel,
        "User": User,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Place": Place,
        "Review": Review,
    }

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
        elif args[0] not in self.Classes:
            print("** class doesn't exist **")
        else:
            new_instance = self.Classes[args[0]]()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, arg):
        """Print the string representation of an instance."""
        args = shlex.split(arg)
        if not args or args[0] == "":
            print("** class name missing **")
        elif args[0] not in self.Classes:
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
        elif args[0] not in self.Classes:
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
        if args and args[0] not in self.Classes:
            print("** class doesn't exist **")
        else:
            instances = []
            for key, value in storage.all().items():
                if not args or args[0] == "" or args[0] == value.__class__.__name__:
                    instances.append(str(value))
            print(instances)

    def default(self, arg):
        """Default command that handles class"""
        args = arg.split('.', 1)
        if args[0] in self.Classes:
            if args[1].strip('()') == 'all':
                self.do_all(args[0])
            elif args[1].strip('()') == 'count':
                class_name = args[0]
                self.count_obj(class_name)
            elif args[1].split('(')[0] == 'show':
                self.do_show(args[0]+' '+args[1].split('(')[1].strip(')'))
            elif args[1].split('(')[0] == 'destroy':
                self.do_destroy(args[0]+' '+args[1].split('(')[1].strip(')'))
            else:
                print('*** Unknown syntax ***')
        else:
            print("** class doesn't exist **")

    def count_obj(self, class_name):
        """Print the number of instances of a class."""
        if not class_name:
            print("** class name d **")
        elif class_name not in self.Classes:
            print("** class doesn't exist **")
        else:
            counter = 0
            for key, value in storage._FileStorage__objects.items():
                if class_name == key.split('.')[0]:
                    counter += 1
            print(counter)

    def do_update(self, arg):
        """Update an instance based on class name and id."""
        args = shlex.split(arg)
        if not args or args[0] == "":
            print("** class name missing **")
        elif args[0] not in self.Classes:
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
