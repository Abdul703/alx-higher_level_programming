#!/usr/bin/python3
"""Base class for all subsequent classes"""
import json
import csv


class Base:
    """The Base class"""

    __nb_objects = 0

    def __init__(self, id=None):
        """initialise the object id

        Args:
            id (int, optional): an id number of the object. Defaults to None.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """serialize an object

        Args:
            list_dictionaries (dict): an object to serialize

        Returns:
            str: serialized object
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """save json object in to a file

        Args:
            list_objs (list): json objects to save
        """
        with open(f"{cls.__name__}.json", "w") as f:
            if list_objs is None:
                f.write("[]")
            else:
                objs = [obj.to_dictionary() for obj in list_objs if obj]
                json_str = cls.to_json_string(objs)
                f.write(json_str)
        f.close()

    @staticmethod
    def from_json_string(json_string):
        """deserialise a string

        Args:
            json_string (str): a string to deserialise

        Returns:
            str: deserialised string
        """
        if json_string:
            return json.loads(json_string)
        return []

    @classmethod
    def create(cls, **dictionary):
        """duplicate an instance

        Returns:
            instance: an instance that can be Square or Rectangle
        """
        dummy_instance = cls(1, 2) if cls.__name__ == 'Rectangle' else cls(1)
        dummy_instance.update(**dictionary)
        return dummy_instance

    @classmethod
    def load_from_file(cls):
        """load json from a file

        Returns:
            list: list of json objects in the file
        """
        try:
            with open(f"{cls.__name__}.json", "r") as f:
                dictnaries = cls.from_json_string(f.read())
                return [cls.create(**dictionary) for dictionary in dictnaries]
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """save json object in to a file

        Args:
            list_objs (list): json objects to save
        """
        with open(f"{cls.__name__}.csv", "w", newline="") as f:
            objs = [obj.to_dictionary() for obj in list_objs if obj]

            csv_writer = csv.writer(f)
            for list_obj in list_objs:
                csv_writer.writerow(list_obj.to_dictionary().values())
        f.close()

    @classmethod
    def load_from_file_csv(cls):
        """load json from a file

        Returns:
            list: list of json objects in the file
        """
        try:
            with open(f"{cls.__name__}.csv", "r") as csvfile:
                csv_reader = csv.reader(csvfile)
                # header = next(csv_reader, None)

                object_type = {
                    "Square": ["id", "size", "x", "y"],
                    "Rectangle": ["id", "width", "height", "x", "y"],
                }

                # List to store dictionaries
                dictnaries = []
                for row in csv_reader:
                    # Convert the row values to integers
                    values = [int(value) for value in row]

                    # Create the dictionary using the specified order of keys
                    dictionary = dict(zip(object_type[cls.__name__], values))

                    # Append the dictionary to the list
                    dictnaries.append(dictionary)

                return [cls.create(**dictionary) for dictionary in dictnaries]
        except FileNotFoundError:
            return []
