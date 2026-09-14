from busar import Bursar, save_bursar, load_bursar
from student import Student
from management import BursaryManagement, load_application, save_application
import re

application_list = load_application()
bursar_list = load_bursar()
bursary = BursaryManagement(application_list)
def is_valid_email(email):
    pattern = r"^[\w]+@[\w]+\.[\w]{2,}$"
    return re.match(pattern, email) is not None
def is_valid_password(password):
    pattern = r"^(?=.*[£$@&%])[\w$£@&%]{7,}$"
    return re.match(pattern, password) is not None

while True:
    print('=================')
    print('  AFOY ACADEMY ')
    print('=================')
    print('\nwelcome to AFOY Academy ')
    print('1.Bursar')
    print('2.student')
    print('3.Exit')

    try:
        choice = int(input('enter your choice:'))
    except ValueError:
        print('invalid choice, please enter a valid choice')
        continue
    if choice == 3:
        break

    if choice == 2:
        while True:
            print('\n=====STUDENT MENU====')
            print('1.Submit Application')
            print('2.Back')
            try:
                s_choice = int(input('enter option:'))
            except ValueError:
                print('invalid choice, please enter a valid option')
                continue
            if s_choice == 2:
                break

            if s_choice == 1:
                print('====Student Board====')
                name = input('enter your name:')
                amount = float(input('enter amount requested:'))
                new_student = Student(name, amount)
                application_list.append(new_student)
                save_application(application_list)
                print(f'\nApplication submitted successfully{name}')

    if choice == 1:
        while True:
            print('\n====Bursar MENU====')
            print('1.Create Account')
            print('2.Login')
            print('3.Back')
            try:
                option = int(input('enter option:'))
            except ValueError:
                print('invalid choice, please enter a valid option')
                continue
            if option == 3:
                break

            if option == 1:
                username = input('enter username:')
                email = input('enter email:')
                password = input('enter password:')

                if is_valid_email(email) and is_valid_password(password):
                    new_bursar = Bursar(username, email, password)
                    bursar_list.append(new_bursar)
                    save_bursar(bursar_list)
                    print(f'\n{username} account created successfully')
                else:
                    if not is_valid_email(email):
                        print('invalid email format, please try again')
                    if not is_valid_password(password):
                        print('invalid password format, include at least 7 character and include £$@&%')

            elif option == 2:
                while True:
                    print('====LOGIN MENU====')
                    login_username = input('enter username:')
                    password = input('enter password:')
                    found = None
                    for b in bursar_list:
                        if b.username == login_username and b.password == password:
                            found = b
                            break
                    if found is None:
                        print('input a valid credential')
                        continue

                    else:
                        print(f'Welcome, {found.username}')
                        break
                while True:
                    print('\n====LOGIN MENU====')
                    print('1.View All Application')
                    print('2.Search Application')
                    print('3.Approve Application')
                    print('4.Reject Application')
                    print('5.Remove Application')
                    print('6.Total Disbursed')
                    print('7.Logout')
                    try:
                        b_option = int(input('enter option:'))
                    except ValueError:
                        print('invalid choice, please enter a valid option')
                        continue

                    if b_option == 1:
                        for s in bursary.application:
                            print(s)
                    elif b_option == 2:
                        name = input('enter name to search')
                        result = bursary.search_application(name)
                        print(result if result else "not found")
                    elif b_option == 3:
                        name = input('enter name to approve')
                        print("Approved" if bursary.approve_application(name) else "not found")
                    elif b_option == 4:
                        name = input('enter name to reject')
                        print("Rejected" if bursary.reject_application(name) else "not found")
                    elif b_option == 5:
                        name = input('enter name to remove')
                        print("Removed" if bursary.remove_application(name) else "not found")
                    elif b_option == 6:
                        print(f'Total Disbursed: {bursary.total_disbursed()}')
                    elif b_option == 7:
                        break
