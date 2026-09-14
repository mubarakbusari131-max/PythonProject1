from contact.INFO import Contact, load_contact, save_contact
import time
contact_list = load_contact()
print("===========")
print("  CONTACT  ")
print("===========")
print("\nWelcome to Contact")
while True:
    print("1.Add Contact")
    print("2.Remove Contact")
    print("3.Search Contact")
    print("4.Edit Contact")
    print("5.View Contact")
    print("6.Clear Contact")
    print("7.Exit")
    try:
        choice = int(input("Enter choice:"))
    except ValueError:
        print("Please enter a valid choice")
        continue
    if choice == 7:
        break
    if choice == 1:
        print("====Add Contact====")
        while True:
            name = input("Enter name:").strip().lower()
            phone_no = input("Enter phone number:")
            new_contact = Contact(name, phone_no)
            contact_list.append(new_contact)
            save_contact(contact_list)
            print("Contact added successfully")
            again = input("Do you want to add another contact?(y/n):").strip().lower()
            if again != "y":
                break
        input("\nPress enter to back to main menu")

    elif choice == 2:
        print("====Search Contact====")
        while True:
            s_name = input("Enter contact to remove:").strip().lower()
            found = False
            for contact in contact_list:
                if contact.name == s_name:
                    contact_list.remove(contact)
                    save_contact(contact_list)
                    print("Contact removed successfully")
                    found = True
                    break
            if not found:
                print("contact not found")

            ag= input("\nDo you want to remove another contact?(y/n):").strip().lower()
            if ag != "y":
                break
        input("\nPress enter to back to main menu")

    elif choice == 3:
        print("====SEARCH CONTACT====")
        while True:
            search_name = input("Enter contact to search:").strip().lower()
            found = False
            for contact in contact_list:
                if contact.name == search_name:
                    print(f"\n{contact}")
                    found = True
                    break
            if not found:
                print("contact not found")
            s_again = input("\nDo you want to search another contact?(y/n):").strip().lower()
            if s_again != "y":
                break

    elif choice == 4:
        print("====EDIT CONTACT====")
        while True:
            edit = input("Enter contact to edit:").strip().lower()
            found = False
            for contact in contact_list:
                if contact.name == edit:
                    print(f"\n{contact}")
                    new_name = input("\nEnter new name(leave blank to keep current:)").strip().lower()
                    new_phone_no = input("Enter new phone number(leave blank to keep current:)").strip().lower()
                    if new_name != "":
                        contact.name = new_name
                    if new_phone_no != "":
                        contact.phone_no = new_phone_no
                    save_contact(contact_list)
                    print("Contact updated successfully")
                    found = True
                    break
            if not found:
                print("contact not found")
            edit_again = input("\nDo you want to edit another contact?(y/n):").strip().lower()
            if edit_again != "y":
                break
        input("\npress enter to back to main menu ")

    elif choice == 5:
        print("====VIEW CONTACT====")
        for contact in contact_list:
            print(f"\n{contact}")
            time.sleep(1.0)
        if not contact_list:
            print("No contact found")
        input("\nPress enter to back to main menu")

    elif choice == 6:
        print("====CLEAR CONTACT====")
        if contact_list:
            contact_list.clear()
            save_contact(contact_list)
            print("Contact cleared successfully")
        else:
            print("No contact found")
        input("\nPress enter to back to main menu")


