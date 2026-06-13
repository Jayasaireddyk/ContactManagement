import json
import os

FILE_NAME = "contacts.json"

def load_contacts():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []

def save_contacts(contacts):
    with open(FILE_NAME, "w") as file:
        json.dump(contacts, file, indent=4)

def add_contact(contacts):
    name = input("Enter Name: ")
    phone = input("Enter Phone Number: ")
    email = input("Enter Email: ")

    contact = {
        "name": name,
        "phone": phone,
        "email": email
    }

    contacts.append(contact)
    save_contacts(contacts)

    print("Contact Added Successfully!")

def view_contacts(contacts):
    if not contacts:
        print("No contacts found!")
        return

    print("\n--- Contact List ---")

    for i, contact in enumerate(contacts, start=1):
        print(f"{i}. Name: {contact['name']}")
        print(f"   Phone: {contact['phone']}")
        print(f"   Email: {contact['email']}")
        print()

def edit_contact(contacts):
    view_contacts(contacts)

    if not contacts:
        return

    number = int(input("Enter contact number to edit: "))

    if 1 <= number <= len(contacts):
        contacts[number - 1]["name"] = input("New Name: ")
        contacts[number - 1]["phone"] = input("New Phone: ")
        contacts[number - 1]["email"] = input("New Email: ")

        save_contacts(contacts)
        print("Contact Updated Successfully!")

    else:
        print("Invalid Contact Number!")

def delete_contact(contacts):
    view_contacts(contacts)

    if not contacts:
        return

    number = int(input("Enter contact number to delete: "))

    if 1 <= number <= len(contacts):
        deleted = contacts.pop(number - 1)

        save_contacts(contacts)

        print(f"{deleted['name']} deleted successfully!")

    else:
        print("Invalid Contact Number!")

def main():
    contacts = load_contacts()

    while True:
        print("\n===== Contact Management System =====")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Edit Contact")
        print("4. Delete Contact")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_contact(contacts)

        elif choice == "2":
            view_contacts(contacts)

        elif choice == "3":
            edit_contact(contacts)

        elif choice == "4":
            delete_contact(contacts)

        elif choice == "5":
            print("Exiting Program...")
            break

        else:
            print("Invalid Choice!")


main()