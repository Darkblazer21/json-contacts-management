import json
from pathlib import Path


def check_file_is_ok(path):
    """Check if a file exists and is not empty."""
    if path.exists():
        if path.stat().st_size != 0:
            return True

    return False


def sort_contact(contacts):
    """Sort alphabetically a dictionary of contacts using the 'name' key."""
    sorted_contacts = dict(sorted(contacts.items()))

    return sorted_contacts


def load_contacts(path):
    """Load data from a file."""
    contents = path.read_text()
    contacts = json.loads(contents)
    contacts = dict(contacts)

    return contacts


def ask_new_contact_info(contacts=None):
    """Ask infos about a new contact"""
    if contacts is None:
        contacts = {}

    name = input("Enter a new contact name: ").lower()

    infos = {"phone": "", "email": ""}
    for key in infos.keys():
        infos[key] = input(f"Enter this person's {key}: ").lower()

    contacts[name] = infos

    return contacts


def store_new_content(contents, path):
    """Store newly added contents in a file."""
    new_contents = json.dumps(contents)
    path.write_text(new_contents)

    print("Contact added successfully!")


def add_new_contact(path):
    """Add new contact to a file."""
    if check_file_is_ok(path):
        contacts = load_contacts(path)

        contacts_updated = ask_new_contact_info(contacts=contacts)
        store_new_content(contacts_updated, path)
    else:
        new_contact = ask_new_contact_info()
        store_new_content(new_contact, path)


def search_for_contact(path, name):
    """Search for a contact in a file."""
    found_names = []
    if check_file_is_ok(path):
        contacts = load_contacts(path)
        sorted_contacts = sort_contact(contacts)

        if name in contacts:
            found_names.append(name)

        show_search_results(found_names, sorted_contacts)

    else:
        print(
            "The file is empty or does not exist.Please choose option 2 to add a new contact."
        )


def show_search_results(name_list, contacts):
    """Show a contact found after a successfull search."""
    if name_list:
        print("\n--- Search Results ---")
        for name in name_list:
            print(f"\n--- {name.title()} ---")
            for key, value in contacts[name].items():
                print(f"- {key.title()}: {value}")
    else:
        print("\nNo results!")


def show_all_contacts(path):
    """Show all contacts in a file."""
    if check_file_is_ok(path):
        contacts = load_contacts(path)
        contacts = sort_contact(contacts)

        for name in contacts.keys():
            print(f"\n--- {name.title()} ---")
            for key, value in contacts[name].items():
                print(f"- {key.title()}: {value}")

    else:
        print(
            "The file is empty or does not exist.Please choose option 2 to add a new contact."
        )


filename = "contacts.json"
path = Path(filename)

while True:
    action = input(
        "\nChoose one of the following options:"
        "\n1. Show all contacts"
        "\n2. Add a new contact"
        "\n3. Search a contact by name"
        "To stop the program, press 'Q' or 'q'"
        "\nYour choice: "
    )

    if action.lower() == "q":
        break

    if action == "1":
        show_all_contacts(path)
    elif action == "2":
        add_new_contact(path)
    elif action == "3":
        name = input("Please enter the name you're searching for: ").lower()
        search_for_contact(path, name)
    else:
        print("Invalid entry! Please choose a valid option.")
