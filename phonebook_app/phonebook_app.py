class phonebook:
    phone_directory = []

    def __init__(self, name, phone_number):
        self.name = name
        self.phone = phone_number
        phonebook.phone_directory.append(self)

    def show_contact(self):
        return f"Name: {self.name}, Phone Number: {self.phone}"

    @classmethod
    def show_all_contacts(cls):
        if len(cls.phone_directory) == 0:
            print("No contacts found.")
        else:
            print("All Contacts:")
            for contact in cls.phone_directory:
                print(contact.show_contact())

    @classmethod
    def search_contact(cls, name):
        for contact in cls.phone_directory:
            if contact.name.lower() == name.lower():
                print(f"Contact found: {contact.show_contact()}")
                return
        print("Contact not found.")

    @staticmethod
    def validate_phone_number(phone_number):
        import re
        pattern = r'^\d{10}$'

        if re.match(pattern, phone_number):
            return True
        else:
            return False

    @staticmethod
    def delete_contact(name):
        for contact in phonebook.phone_directory:
            if contact.name.lower() == name.lower():
                phonebook.phone_directory.remove(contact)
                return f"Contact {name} deleted successfully."

        return "Contact not found."


# Add contacts
n_contacts = int(input("Enter the number of contacts you want to add: "))

for i in range(n_contacts):
    name = input("Enter contact name: ")
    phone_number = input(
        "Enter contact phone number (format: XXXXXXXXXX): "
    )

    if phonebook.validate_phone_number(phone_number):
        phonebook(name, phone_number)
    else:
        print("Invalid phone number format. Please use XXXXXXXXXX.")


# Menu
while True:
    print("\nSelect an option:")
    print("1. Show all contacts")
    print("2. Search for a contact")
    print("3. Delete a contact")
    print("4. Exit")

    option = input("Enter your choice (1/2/3/4): ")

    if option == '1':
        phonebook.show_all_contacts()

    elif option == '2':
        name = input(
            "Enter the name of the contact you want to search for: "
        )
        phonebook.search_contact(name)

    elif option == '3':
        name = input(
            "Enter the name of the contact you want to delete: "
        )
        print(phonebook.delete_contact(name))

    elif option == '4':
        print("Exiting the phonebook application.")
        break

    else:
        print("Invalid option. Please choose 1-4.")