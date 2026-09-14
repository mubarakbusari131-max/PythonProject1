import json
import os
from student import Student

APPLICATION_FILE = "bursaries.json"

def save_application(application_list, filename = APPLICATION_FILE):
    with open(filename,'w') as f:
        json.dump([s.to_dict() for s in application_list], f, indent = 2)

def load_application(filename = APPLICATION_FILE):
    if not os.path.exists(filename):
        return []
    with open(filename,'r') as f:
        data = json.load(f)
        return [Student.from_dict(d) for d in data]

class BursaryManagement:
    def __init__(self, applications = None):
        self.application = applications if applications is not None else []

    def add_application(self, student):
        self.application.append(student)

    def remove_application(self, name):
        for s in self.application:
            if s.name == name:
                self.application.remove(s)
                return True
        return False

    def search_application(self, name):
        for s in self.application:
            if s.name == name:
                return s
        return None

    def approve_application(self, name,):
        student = self.search_application(name)
        if student is None :
            return False
        student.status = "approved"
        return True

    def reject_application(self, name):
        student = self.search_application(name)
        if student is None:
            return False
        student.status = "rejected"
        return True

    def total_disbursed(self):
        total = 0
        for s in self.application:
            if s.status == "approved":
                total += s.amount
        return total

