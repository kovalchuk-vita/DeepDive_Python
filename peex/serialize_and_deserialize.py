"""
Write a Python program for Serialize and deserialize an object
"""

import pickle

# Define a sample class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"Person(name={self.name}, age={self.age})"

# Create an instance of the Person class
person = Person("Vita", 30)

# Serialize the object to a byte stream
serialized_person = pickle.dumps(person)
print("Serialized:", serialized_person)

# Deserialize the byte stream back to an object
deserialized_person = pickle.loads(serialized_person)
print("Deserialized:", deserialized_person)