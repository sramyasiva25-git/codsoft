contacts = []   

def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")

    contact = {
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    }

    contacts.append(contact)
    print("Contact added successfully!\n")


def view_contacts():
    if not contacts:
        print("No contacts found.\n")
        return

    print("Contact List:")
    for i, contact in enumerate(contacts, start=1):
        print(i, contact["name"], "-", contact["phone"])
    print()


def search_contact():
    search = input("Enter name or phone to search: ")

    for contact in contacts:
        if search == contact["name"] or search == contact["phone"]:
            print("Contact Found:")
            print(contact)
            print()
            return

    print("Contact not found.\n")


def update_contact():
    phone = input("Enter phone number of contact to update: ")

    for contact in contacts:
        if phone == contact["phone"]:
            contact["name"] = input("Enter new name: ")
            contact["email"] = input("Enter new email: ")
            contact["address"] = input("Enter new address: ")
            print("Contact updated successfully!\n")
            return

    print("Contact not found.\n")


def delete_contact():
    phone = input("Enter phone number to delete: ")

    for contact in contacts:
        if phone == contact["phone"]:
            contacts.remove(contact)
            print("Contact deleted successfully!\n")
            return

    print("Contact not found.\n")

while True:
    print("----- Contact Book -----")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        add_contact()
    elif choice == "2":
        view_contacts()
    elif choice == "3":
        search_contact()
    elif choice == "4":
        update_contact()
    elif choice == "5":
        delete_contact()
    elif choice == "6":
        print("Thank you for using Contact Book.")
        break
    else:
        print("Invalid choice. Try again.\n")