#!/usr/bin/python3
"""Console for HBNB"""

import cmd
import models

class HBNBCommand(cmd.Cmd):
    """Command interpreter class"""

    prompt = "(hbnb) "

    def emptyline(self):
        """Do nothing on empty input line"""
        pass

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        print()
        return True

    def do_create(self, arg):
        """Create a new instance of BaseModel, save it, and print the id"""
        if not arg:
            print("** class name missing **")
            return
        try:
            new_instance = models.classes[arg]()
            new_instance.save()
            print(new_instance.id)
        except KeyError:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """Prints the string representation of an instance"""
        if not arg:
            print("** class name missing **")
            return
        args = arg.split()
        if args[0] not in models.classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            obj_key = args[0] + "." + args[1]
            all_objs = models.storage.all()
            if obj_key in all_objs:
                print(all_objs[obj_key])
            else:
                print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        if not arg:
            print("** class name missing **")
            return
        args = arg.split()
        if args[0] not in models.classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            obj_key = args[0] + "." + args[1]
            all_objs = models.storage.all()
            if obj_key in all_objs:
                del all_objs[obj_key]
                models.storage.save()
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """Prints all string representation of all instances"""
        args = arg.split()
        all_objs = models.storage.all()
        if not arg:
            print([str(value) for value in all_objs.values()])
        elif args[0] not in models.classes:
            print("** class doesn't exist **")
        else:
            print([str(obj) for key, obj in all_objs.items() if key.startswith(args[0])])

    def do_update(self, arg):
        """Updates an instance based on the class name and id"""
        if not arg:
            print("** class name missing **")
            return
        args = arg.split()
        if args[0] not in models.classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            obj_key = args[0] + "." + args[1]
            all_objs = models.storage.all()
            if obj_key not in all_objs:
                print("** no instance found **")
                return
            if len(args) < 3:
                print("** attribute name missing **")
            elif len(args) < 4:
                print("** value missing **")
            else:
                obj = all_objs[obj_key]
                attr_name = args[2]
                attr_value = args[3]
                setattr(obj, attr_name, attr_value)
                obj.save()

if __name__ == '__main__':
    HBNBCommand().cmdloop()
