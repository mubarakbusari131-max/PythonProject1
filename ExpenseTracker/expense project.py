
import re
from expenses import Expenses, User, save_user, load_user, save_expense, load_expense

user_list = load_user()
expense_list = load_expense()

def is_valid_email(email):
    pattern=r"^[\w.]+@[\w.]+\.\w{2,}$"
    return re.fullmatch(pattern,email) is not None

def is_valid_password(password):
    pattern=r"^(?=.*[%$£&])[\w*&%$£]{6,}$"
    return re.fullmatch(pattern,password) is not None
while True:
    print('====================')
    print('   Daily EXPENSES ')
    print('====================')
    print('\nWelcome to daily expenses')
    print('1.create Account')
    print('2.login')
    print('3.logout')
    print('4.exit')

    try:
        choice = int(input('Enter choice:'))
    except ValueError:
        print('Please enter a number')
        continue
    if choice == 4:
        break


    if choice ==3:
        while True:
            sure = input('sure you want to logout ?(y/n ?)')
            if sure == 'y':
                break
            else:
                pass

    if choice == 1:
        print('\n====Create Account====')
        username = input('input username')
        email = input('input email')
        password = input('input password')

        if is_valid_email(email) and is_valid_password(password):
            new_user = User(email, username, password)
            user_list.append(new_user)
            save_user(user_list)
            print(f'{username} account created successfully')


    if choice == 2:
        while True:
            print('\n====Login Menu====')
            login_username = input('input username')
            password = input('input password')
            found_user = None
            for u in user_list:
                if u.username == login_username and u.password == password:
                    found_user = u
                    break

            if found_user is None:
                print('please input valid credentials')
                continue
            else:
                print(f'Welcome, {found_user.username}')
                break
        while True:
            print('\n====Login Menu====')
            print('1.Add expenses')
            print('2.Remove expenses')
            print('3.View expenses ')
            print('4.search expenses')
            print('5.Back to main menu')
            try:
                option = int(input('Enter option:'))

            except ValueError:
                print('input invalid option')
                continue

            if option == 1:
                while True:
                    print('\n====Add Expenses====')
                    name = input('expense name').strip().lower()
                    amount = float(input('expense amount'))
                    category = input('expense category').strip().lower()
                    date = (input('expense date'))
                    description = input('expense description').strip().lower()

                    new_expenses = Expenses(name, amount, category, date, description)
                    expense_list.append(new_expenses)
                    save_expense(expense_list)
                    print('expense added')

                    again = input('add another expense(y/n ?)')
                    if again != 'y':
                        break

            elif option == 2:
                while True:
                    remove_search = input('search expense').lower().strip()
                    found = False
                    for expense in expense_list:
                        if expense.name.lower() == remove_search:
                            expense_list.remove(expense)
                            save_expense(expense_list)
                            print('expense removed')
                            found = True
                            break
                    if not found:
                        print('expense not found')

                    remove_another_expense = input('redo expense(y/n ?)').strip().lower()
                    if remove_another_expense != 'y':
                        break

            elif option == 3:
                print('\n=====EXPENSES=====')
                for expense in expense_list:
                    print(expense)

                if not expense_list:
                    print('No expenses found')
                input('\nPress enter to return to login menu')

            elif option == 4:
                search_expense = input('search expense').lower().strip()
                found = False
                for expense in expense_list:
                    if expense.name.lower() == search_expense:
                        print(expense)
                        found = True
                if not found:
                    print('expense not found')
                input('\nPress enter to return to login menu')


            elif option == 5:
                break

