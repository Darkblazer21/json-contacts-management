from pathlib import Path


def ask_for_new_contact():
    """Ask if user wants to add a new contact"""
    pass


def add_new_contact():
    """Add new contact to a file."""
    pass


def show_all_contacts(path):
    """Show all contacts in a file."""
    pass


filename = "contacts.json"
path = Path(filename)

while True:
    action = input(
        "Choose one of the following options:"
        "\n1. Show all contacts"
        "\n2. Add a new contact"
        "\n3. Search a contact by name"
        "To stop the program, press 'Q' or 'q'"
        "\nYour choice: "
    )

    if action.lower() == "q":
        break

    if action == "1":
        print()
    elif action == "2":
        print()
    elif action == "3":
        print()
    else:
        print("Invalid entry! Please choose a valid option.")
