#!/usr/bin/python3
"""importing relevant modules"""
import sys
import cmd
import json
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models.place import Place

classesList = [
        "BaseModel",
        "User",
        "Place",
        "Review",
        "City",
        "State",
        "Amenity"
        ]
"""creating our class"""
class HBNBCommand(cmd.Cmd):
    """Defines our Airbnb Console"""
    prompt = '(hbnb)'
    def emptyline(self):
        """
        Won't execute if an empty line + ENTER is clicked.
        """
        pass
    def do_quit(self, arg):
        """
        Quit command to exit the program.
        Args:
        arg: Argument passed (not used here).
        """
        sys.exit(1)
    def do_EOF(self, arg):
        """
        Handle end of file (Ctrl+D).
        Args:
        arg: Argument passed (not used here).
        """
        print("")
        return True
    def do_create(self, args):
        """
        Creates a new instance of a specified class,
        saves it to a JSON file, and prints its ID.
        Args:
        args: Arguments passed (class name and optional attributes).
        """
        args_list = args.split(" ")
        if len(args_list) == 1 and args_list[0] == "":
            print("** class name missing **")
        elif args_list[0] not in classesList:
            print("** class doesn't exist **")
        else:
            instance = eval(args_list[0] + "()")  # Creates an instance of the specified class
            storage.save()  # Saves the instance to a JSON file (not shown here)
            print(instance.id)  # Prints the ID of the created instance
            #Create an instance of the HBNBCommand class and start the command loop
    def do_show(self, args):
        """
        Prints the string representation of an instance
        based on the class name and ID.
        Args:
        args: Arguments passed (class name and instance ID).
        """
        args_list = args.split()
        if len(args_list) < 2:
            print("** class name and instance id missing **")
            return
        class_name, instance_id = args_list[0], args_list[1]
        if class_name not in classesList:
            print("** class doesn't exist **")
            return
        objects = storage.all()
        obj_id = f"{class_name}.{instance_id}"
        if obj_id in objects:
            obj = objects[obj_id]
            print(obj)
        else:
            print("** no instance found **")
    def do_destroy(self, args):
        """
        Deletes an instance based on the class name and ID
        (saves the change into the JSON file).
        Args:
        args: Arguments passed (class name and instance ID).
        """
        args_list = args.split()
        if len(args_list) < 2:
            print("** class name and instance id missing **")
            return
        class_name, instance_id = args_list[0], args_list[1]
        if class_name not in classesList:
            print("** class doesn't exist **")
            return
        objects = storage.all()
        obj_id = f"{class_name}.{instance_id}"
        if obj_id in objects:
            del objects[obj_id]
            fstorage.save()
        else:
            print("** no instance found **")
    def do_all(self, args):
        """
        Prints a list of string representations of all instances
        based on the class name or prints all instances if no class name is provided.
        Args:
        args: Arguments passed (optional class name).
        """
        objs = storage.all()
        args_list = args.split()
        if not args_list or args_list[0] == "":
            objs_list = [str(obj) for obj in objs.values()]
            print(objs_list)
        elif args_list[0] in classesList:
            class_name = args_list[0]
            objs_list = [str(objs[obj]) for obj in objs if obj.split(".")[0] == class_name]
            print(objs_list)
        else:
            print("** class doesn't exist **")
    def do_update(self, arg):
        """
        Updates an instance based on the class name, ID, attribute, and value.
        Args:
        arg: Arguments passed (class name, instance ID, attribute, and value).
        """
        objs = storage.all()
        args = arg.split()
        if len(args) < 2:
            print("** class name and instance id missing **")
        elif args[0] in classesList:
            class_name, instance_id = args[0], args[1]
            if instance_id not in [name_id.split(".")[1] for name_id in objs]:
                print("** no instance found **")
                return
            name_id = f"{class_name}.{instance_id}"
            obj = objs[name_id]
            if len(args) < 3:
                print("** attribute name missing **")
            elif len(args) < 4:
                print("** value missing **")
            else:
                attr_name, attr_value = args[2], args[3]
                try:
                    attr_value = eval(attr_value.strip('"'))
                except Exception:
                    pass
                setattr(obj,attr_name,attr_value)
                storage.save()
        else:
            print("** class doesn't exist **")

    def default(self, line):
        """
        Default method for handling custom commands.
        Args:
        line: Input line containing the command.
        """
        args = line.split(".")
        if len(args) >= 2:
            className = args[0]
            method = args[1]
            if className in classesList:
                objects = storage.all()
                if method == "count()":
                    times = sum(1 for key in objects if className in key)
                    print(times)
                elif method == "all()":
                    allList = [str(objects[key]) for key in objects if className in key]
                    print(allList)
                elif "show" in method:
                    show_id = method.split("(")[1].strip(")").replace('"', '')
                    show_str = f"{className} {show_id}"
                    self.do_show(show_str)
                elif "destroy" in method:
                    destroy_id = method.split("(")[1].strip(")").replace('"', '')
                    destroy_str = f"{className} {destroy_id}"
                    self.do_destroy(destroy_str)
                elif "update" in method:
                    # Extract update_id, attribute, and value
                    update_params = method.split("(")[1].strip(")").split(", ")
                    if "{" not in update_params[0]:
                        update_id, attr, value = [param.strip('"') for param in update_params]
                        update_str = f"{className} {update_id} {attr} {value}"
                        self.do_update(update_str)
if __name__ == '__main__':
    HBNBCommand().cmdloop()
