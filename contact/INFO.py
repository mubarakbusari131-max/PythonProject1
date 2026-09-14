import json
import os
FILE_NAME = "../number.json"

def save_contact(num_data, filename=FILE_NAME):
    with open(filename, "w") as f:
        json.dump([n.to_dict() for n in num_data], f, indent=2)

def load_contact(filename=FILE_NAME):
    if not os.path.exists(filename):
        return []
    with open(filename, "r") as f:
        data = json.load(f)
    return [Contact.from_dict(n) for n in data]

class Contact:
    def __init__(self, name, phone_no):
        self.name = name
        self.phone_no = phone_no

    def __str__(self):
        return f" {self.name} {self.phone_no}"

    def to_dict(self):
        return {"name": self.name, "phone_no": self.phone_no}

    @classmethod
    def from_dict(cls, data):
        return cls(data["name"], data["phone_no"])
