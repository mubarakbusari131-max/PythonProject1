print("================")
print(" FEES PAYMENT")
print("================")
class Fees:
     def __init__(self, name, fees=150000):
         self.name = name
         self.fees = fees
         self.paid = 0

     def balance(self):
        return self.fees -  self.paid

     def amount_to_pay(self, amount):
         if amount < 0:
             print("amount cannot be negative")

         elif  amount > self.balance():
            print("You paid more than your school fees, and it can't be refunded")

         elif amount == 0 :
            print(f"your balance is {self.balance()}")

         else:
             self.paid += amount
             if self.balance() == 0:
                 print("you have paid up your school fees")

             else:
                 print(f"you have {self.balance()} left to balance your school fees ")

name = input("\n Enter your name: ")
school = Fees(name)
while school.balance() != 0:
    try:
        amount = int(input("Enter amount you want to pay: "))
    except ValueError:
        print("Please enter a valid credential")
        continue

    school.amount_to_pay(amount)

    if school.balance() == 0:
        break
    again = input("pay more? (yes/no): ").lower()
    if again != "yes":
        break