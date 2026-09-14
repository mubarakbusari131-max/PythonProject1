class Student:
    def __init__(self, name, amount, status= "pending"):
        self.name = name
        self.amount = amount
        self.status = status

    def __str__(self):
        return f"{self.name}: {self.amount} {self.status}"

    def to_dict(self):
        return {"name": self.name, "amount": self.amount, "status": self.status}

    @staticmethod
    def from_dict(cls, data):
        return cls(data["name"], data["amount"], data["status"])