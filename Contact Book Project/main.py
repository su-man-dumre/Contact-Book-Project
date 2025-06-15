from contact_manager import *

while True:
    print("\n=== Contact Book ===")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        add_contact()
    elif choice == '2':
        view_contacts()
    elif choice == '3':
        search_contact()
    elif choice == '4':
        update_contact()
    elif choice == '5':
        delete_contact()

    elif choice == '6':
        break
    else:
        print("Invalid choice!")
