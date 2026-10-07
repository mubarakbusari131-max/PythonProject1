import json
import os

def get_filename(class_name):
    return f"{class_name.lower().replace(' ','')}.json"

def save_data(students, class_name ):
    with open(get_filename(class_name), "w") as f:
        json.dump([s.to_dict() for s in students], f, indent=4)

def load_data(class_name):
    if not os.path.exists(get_filename(class_name)):
        return []
    with open(get_filename(class_name), "r") as f:
        return [Student.from_dict(d) for d in json.load(f)]

class Student:
    def __init__(self, name, subjects):
        self.name = name
        self.subject = subjects

    def __str__(self):
        return f"{self.name} {self.subject}"

    def to_dict(self):
        return {"name": self.name, "subject": self.subject}

    @classmethod
    def from_dict(cls, d):
        return cls(d["name"], d["subject"])