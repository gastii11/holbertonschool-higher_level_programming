#!/usr/bin/python3

import pickle


class CustomObject:
    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        with open(filename, 'wb') as task_01_pickle:
            pickle.dump(self, task_01_pickle)

    @classmethod
    def deserialize(cls, filename):
        try:
            with open(filename, 'rb') as task_01_pickle:
                return pickle.load(task_01_pickle)
        except FileNotFoundError:
            return None
        except Exception as e:
            return None
