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
                name = input("Enter student name:")
                Class = input("Enter Class:")




