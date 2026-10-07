from sub import Student, save_data, load_data, get_filename


print("===============")
print("  REPORT CARD  ")
print("===============")
while True:
    print("\nLOGIN AS")
    print("1. Teacher")
    print("2. Management")
    print("3. Student")
    print("4. Exit")
    try:
        login = int(input("\nEnter your choice:"))
    except ValueError:
        print("Please enter a valid choice")
        continue
    if login == 4:
        print("Goodbye")
        break

    elif login == 1:
        while True:
            print("\nTEACHERS MENU")
            print("1.Add Result")
            print("2.Edit Result")
            print("3.Delete Result")
            print("4.View Results")
            print("5.Back")

            try:
                option = int(input("\nEnter Option:"))
            except ValueError:
                print("Please enter a valid option")
                continue
            if option == 5:
                break

            elif option == 1:
                print("\nRESULT ADDING MENU")
                while True:
                    name = input("Enter student name:").strip().lower()
                    Class = input("Enter Class:").strip().lower()
                    subjects = []
                    while True:
                        subject = input("Enter subject:").strip().lower()
                        try:
                            score = int(input("Enter score for subject:"))
                        except ValueError:
                            print("Please enter a valid score")

                            continue
                        subjects.append(f"{subject}:{score}")

                        students = load_data(Class)
                        students.append(Student(name, subjects))
                        save_data(students, Class)
                        print(f"\n{name} Result added to {Class}")

                        again=input("\nDo you want to record another subject?(yes/no):")
                        if again != "yes":
                            break

                    another = input("\nDo you want to record another student?(yes/no):")
                    if another != "yes":
                        break

            elif option == 2:
                print("\nRECORD EDITING MENU")








