import sys
import json
import os

print("====================")
print(" EXAM REGISTRATION  ")
print("====================")
print("\nWelcome to Afoy Academy")
print()
STUDENT_FILE = 'students.json'

def save_student(student_data, filename = STUDENT_FILE):
    with open(filename, 'w') as f:
        json.dump([s.to_dict() for s in student_data], f, indent=2)

def load_student(filename = STUDENT_FILE):
    if not os.path.exists(filename):
        return []
    with open(filename, 'r') as f:
        data = json.load(f)
    return [Student.from_dict(d) for d in data]

def generate_id(prefix, existing_id_):
    if not existing_id_:
        return f"{prefix}001"
    next_id = [int(i[len(prefix):]) for i in existing_id_]
    return f"{prefix}{max(next_id)+1:03d}"

class Student:
    def __init__(self, name_, age_, course_, subject_, reg_id_):
        self.name = name_
        self.age = age_
        self.course = course_
        self.subject = subject_
        self.reg_id = reg_id_

    def __str__(self):
        return f'{self.name} {self.age} {self.course} {self.subject}, {self.reg_id}'

    def to_dict(self):
        return {'name': self.name, 'age': self.age, 'course': self.course, 'subject': self.subject, "reg_id": self.reg_id}

    @classmethod
    def from_dict(cls, data):
        return cls(data['name'], data['age'], data['course'], data['subject'], data["reg_id"])

name = input("Enter your name:")
age = None
while True:
    try:
        age = int(input("Enter your age:"))
    except ValueError:
        print("Please enter an integer")
        continue
    if age >= 18:
        break
    else:
        print('underage is not entitled to the exam')
        sys.exit()

course = input("Enter your course:")
subject = input("Enter your subject combination:")

student_list = load_student()
existing_id = [s.reg_id for s in student_list]
reg_id = generate_id("AF03EXMFT", existing_id)

student = Student(name, age, course, subject, reg_id)
student_list.append(student)
save_student(student_list)

print(f'\nRegistration Successful {name}')
print(f'\nYour Registration ID is {reg_id}')