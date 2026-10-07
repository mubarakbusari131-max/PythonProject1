import json
import os

FILE_NAME = "../Form.json"

def save_student(student_data, filename=FILE_NAME):
    with open(filename, "w") as f:
        json.dump([s.to_dict() for s in student_data], f, indent=2 )

def load_student(filename=FILE_NAME):
    if not os.path.exists(filename):
        return []
    with open(filename, "r") as f:
        data = json.load(f)
    return [Student.from_dict(d) for d in data]

class Student:
    def __init__(self, email,name, course, sub_comb,reg_id):
        self.email = email
        self.name = name
        self.course = course
        self.sub_comb = sub_comb
        self.reg_id = reg_id

    def str(self):
        return f"{self.email} {self.name} {self.course} {self.sub_comb} {self.reg_id}"

    def to_dict(self):
        return {"email":self.email, "name":self.name, "course":self.course, "sub_comb":self.sub_comb, "reg_id": self.reg_id}

    @classmethod
    def from_dict(cls, data):
        return cls(data["email"],data["name"],data["course"],data["sub_comb"],data["reg_id"])

