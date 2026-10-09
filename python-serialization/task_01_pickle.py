#!/usr/bin/env python3
"""Module that pickles and unpickles a custom class."""
import pickle


class CustomObject:
    """A custom object that can be serialized with pickle."""

    def __init__(self, name, age, is_student):
        """Initialize the object with name, age and is_student."""
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Print the attributes of the object."""
        print("Name: {}".format(self.name))
        print("Age: {}".format(self.age))
        print("Is Student: {}".format(self.is_student))

    def serialize(self, filename):
        """Serialize the instance to filename using pickle."""
        try:
            with open(filename, "wb") as f:
                pickle.dump(self, f)
        except (OSError, pickle.PicklingError):
            return None

    @classmethod
    def deserialize(cls, filename):
        """Load and return an instance from filename, or None on error."""
        try:
            with open(filename, "rb") as f:
                return pickle.load(f)
        except (OSError, pickle.UnpicklingError, EOFError,
                AttributeError, ImportError, IndexError):
            return None
