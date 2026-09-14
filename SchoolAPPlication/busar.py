import json
import os
BURSAR_fILE = "bursars.json"
def save_bursar(bursar_list, filename = BURSAR_fILE):
    with open(filename,'w') as f:
        json.dump([b.to_dict() for b in bursar_list], f,  indent=2)

def load_bursar(filename = BURSAR_fILE):
    if not os.path.exists(filename):
        return []
    with open(filename,'r') as f:
        data = json.load(f)
        return[Bursar.from_dict(d) for d in data]

class Bursar:
    def __init__(self,username,email,password):
        self.username = username
        self.email = email
        self.password = password

    def __str__(self):
        return f'{self.username} {self.email}{self.password}'

    def to_dict(self):
        return {"username": self.username, "email":self.email, "password":self.password }
    @classmethod
    def from_dict(cls,data):
        return cls(data["username"], data["email"], data["password"])

