# contact_book.py
# A Simple Command-Line Contact Book Application

import os

CONTACTS_FILE = "contacts.txt"


def ensure_file_exists():
    """Create the file if it doesn't exist."""
    if not os.path.exists(CONTACTS_FILE):
        open(CONTACTS_FILE, "w").close()


def add_contact():
    """Add a new contact to the file."""
    name = input("Enter Name: ").strip()
    phone = input("Enter Phone Number: ").strip()
    email = input("Enter Email: ").strip()

    with open(CONTACTS_FILE, "a") as file:
        file.write(f"{name},{phone},{email}\n")

    print(f"✅ Contact '{name}' added successfully!\n")


def view_contacts():
    """Display all saved contacts."""
    ensure_file_exists()
    with open(CONTACTS_FILE, "r") as file:
        contacts = file.readlines()

    if not contacts:
        print("⚠️ No contacts found.\n")
        return

    print("\n📒 Contact List:")
    print("-" * 40)
    for idx, contact in enumerate(contacts, start=1):
        name, phone, email = contact.strip().split(",")
        print(f"{idx}. Name: {name} | Phone: {phone} | Email: {email}")
    print("-" * 40 + "\n")


def search_contacts():
    """Search for a contact by name or phone number."""
    keyword = input("Enter Name or Phone to Search: ").strip().lower()
    ensure_file_exists()

    found = False
    with open(CONTACTS_FILE, "r") as file:
        for contact in file:
            name, phone, email = contact.strip().split(",")
            if keyword in name.lower() or keyword in phone:
                print(f"🔎 Found -> Name: {name} | Phone: {phone} | Email: {email}")
                found = True

    if not found:
        print("❌ No matching contact found.\n")
    print()


def menu():
    """Main menu to interact with the user."""
    ensure_file_exists()
    while True:
        print("===== 📞 CONTACT BOOK =====")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Exit")
        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contacts()
        elif choice == "4":
            print("👋 Exiting Contact Book. Goodbye!")
            break
        else:
            print("⚠️ Invalid choice, please try again.\n")


if __name__ == "__main__":
    menu()
