import json
import os

DATA_FILE = 'contacts.json'

# Load contacts from the JSON file
def load_contacts():
    if not os.path.exists(DATA_FILE):  #in checks that contacts.json file exits or not
        with open(DATA_FILE, 'w') as f:
            json.dump([], f)

    with open(DATA_FILE, 'r') as f:
        return json.load(f)

# Save contacts to the JSON file
def save_contacts(contacts):
    with open(DATA_FILE, 'w') as f:
        json.dump(contacts, f, indent=4)

# 1 Add a new contact
def add_contact():
    contacts = load_contacts()
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    email = input("Enter email: ")
    address = input("Enter address: ")

    new_contact = {
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    }

    contacts.append(new_contact)
    save_contacts(contacts)
    print("Contact added successfully!")

# 2 View all contacts
def view_contacts():
    contacts = load_contacts()
    if not contacts:
        print("No contacts found.")
        return

    print("\n--- Contact List ---")
    for idx, contact in enumerate(contacts, start=1):
        print(f"\nContact {idx}")
        print(f"Name: {contact['name']}")
        print(f"Phone: {contact['phone']}")
        print(f"Email: {contact['email']}")
        print(f"Address: {contact['address']}")

# 3 Search contact by name or phone
def search_contact():
    contacts = load_contacts()
    keyword = input("Enter name or phone to search: ").lower()

    found = False
    for contact in contacts:
        if keyword in contact['name'].lower() or keyword in contact['phone']:
            print("\n--- Contact Found ---")
            print(f"Name: {contact['name']}")
            print(f"Phone: {contact['phone']}")
            print(f"Email: {contact['email']}")
            print(f"Address: {contact['address']}")
            found = True

    if not found:
        print("No matching contact found.")

# 4 Update a contact
def update_contact():
    contacts = load_contacts()
    name = input("Enter the name of the contact to update: ").lower()

    for contact in contacts:
        if name == contact['name'].lower():
            print("Leave blank to keep the current value.")

            new_name = input(f"New name [{contact['name']}]: ") or contact['name']
            new_phone = input(f"New phone [{contact['phone']}]: ") or contact['phone']
            new_email = input(f"New email [{contact['email']}]: ") or contact['email']
            new_address = input(f"New address [{contact['address']}]: ") or contact['address']

            contact['name'] = new_name
            contact['phone'] = new_phone
            contact['email'] = new_email
            contact['address'] = new_address

            save_contacts(contacts)
            print("Contact updated successfully!")
            return

    print("Contact not found.")

# 5 Delete a contact
def delete_contact():
    contacts = load_contacts()
    name = input("Enter the name of the contact to delete: ").lower()

    for i, contact in enumerate(contacts):
        if name == contact['name'].lower():
            confirm = input(f"Are you sure you want to delete {contact['name']}? (y/n): ")
            if confirm.lower() == 'y':
                contacts.pop(i)
                save_contacts(contacts)
                print("Contact deleted successfully!")
                return

    print("Contact not found.")