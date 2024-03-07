def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except (KeyError, ValueError, IndexError) as e:
            if isinstance(e, KeyError):
                return "Enter user name."
            elif isinstance(e, ValueError):
                return "Give me name and phone please."
            elif isinstance(e, IndexError):
                return "Invalid number of arguments."
    return inner

@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

@input_error
def change_user_phone(args, contacts):
    name, phone = args
    if name not in contacts:
        raise KeyError("Contact not found")
    contacts[name] = phone
    return "Contact changed."

@input_error
def phone_username(name, contacts):
    if name in contacts:
        return f"Phone number for contact '{name}': {contacts[name]}"
    else:
        raise KeyError("Contact not found.")

def all_users_phone(contacts):
    return contacts

# Решта коду без змін
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_user_phone(args, contacts))
        elif command == "phone":
            if args:
                print(phone_username(args[0], contacts))
            else:
                print("Please provide a username.")
        elif command == "all":
            print(all_users_phone(contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()