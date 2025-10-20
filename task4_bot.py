# Програма повинна мати функцію main(),
#   яка управляє основним циклом обробки команд.
# Реалізуйте функцію parse_input(),
#   яка розбиратиме введений користувачем рядок на команду та її аргументи.
#   Команди та аргументи мають бути розпізнані незалежно від регістру введення.
# Ваша програма повинна очікувати на введення команд користувачем
#   та обробляти їх за допомогою відповідних функцій.
#   В разі введення команди "exit" або "close",
#   програма повинна завершувати виконання.
# Напишіть функції обробники для різних команд,
#   такі як add_contact(),
#   change_contact(),
#   show_phone() тощо.
# Використовуйте словник Python для зберігання імен і номерів телефонів.
#   Ім'я буде ключем, а номер телефону – значенням.
# Ваша програма має вміти ідентифікувати
#   та повідомляти про неправильно введені команди.
import re


# The method normalizes phone strings by removing non-numbers and addind leading ''+'' if needed.
# If phone number starts with 0 - replace it with +380
# If phone number starts with 3 - add leading +
# If phone number starts with 8 - replace it with +38
#
# Output phone format: +380952345678
def normalize_phone(inphone: str) -> str:
    try:
        phone = re.sub(r"\D", "", inphone)  # Remove all non-digit characters
        if len(phone) < 9:  # Assuming a valid phone number has at least 9 digits
            return ""

        if phone.startswith("0"):
            phone = "38" + phone
        elif phone.startswith("8"):
            phone = "3" + phone

        phone = "+" + phone

        return phone

    except Exception as e:
        print(f"Error normalizing phone number '{inphone}': {e}")
        return ""


def parse_input(user_input):
    if len(user_input.strip()) == 0:
        return ("",)
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def add_contact(args, contacts) -> str:
    if len(args) < 2:
        return "Insufficient arguments. Usage: add <name> <phone>"

    name, phone = args

    normalized_phone = normalize_phone(phone)
    if not normalized_phone:
        return "Invalid phone number format. Valid phone is at least 9 symbols."

    contacts[name] = normalized_phone
    return "Contact added."


def update_contact(args, contacts) -> str:
    if len(args) < 2:
        return "Insufficient arguments. Usage: change <name> <phone>"
    name, phone = args

    normalized_phone = normalize_phone(phone)
    if not normalized_phone:
        return "Invalid phone number format. Valid phone is at least 9 symbols."   

    if name in contacts:
        contacts[name] = phone
        return "Contact updated."
    else:
        return "Contact not found."


def show_contact(args, contacts) -> str:
    if len(args) < 1:
        return "Insufficient arguments. Usage: phone <name>"
    name = args[0]
    if name in contacts:
        return f"{name}: {contacts[name]}"
    else:
        return "Contact not found."


def show_all_contacts(contacts) -> str:
    if contacts:
        return "\n".join(f"{name}: {phone}" for name, phone in contacts.items())
    else:
        return "No contacts found."


def get_output_by_command(command, args, contacts):
    is_exit = False
    if command == "hello":
        output = "How can I help you?"
    elif command == "add":
        output = add_contact(args, contacts)
    elif command == "change":
        output = update_contact(args, contacts)
    elif command == "phone":
        output = show_contact(args, contacts)
    elif command == "all":
        output = show_all_contacts(contacts)
    elif command == "help" or command == "?":
        output = (
            "Available commands:\n"
            "hello - Greet the bot\n"
            "add <name> <phone> - Add a new contact. Expected phone lenght is at least 9 digits.\n"
            "change <name> <phone> - Change an existing contact's phone number. Expected phone lenght is at least 9 digits.\n"
            "phone <name> - Show the phone number of a contact\n"
            "all - Show all contacts\n"
            "exit, close, goodbye - Exit the program"
        )
    elif command in ("exit", "close", "goodbye"):
        output = "Goodbye!"
        is_exit = True
    else:
        output = "Unknown command. Please try again."

    return output, is_exit


def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)
        output, is_exit = get_output_by_command(command, args, contacts)
        print(output)
        if is_exit:
            break


if __name__ == "__main__":
    main()


TEST_NAME = "Vasya"
PHONE1 = "099 555-1234"
PHONE2 = "099 555-5678"
assert parse_input("  AdD  John  12345 ") == ("add", "John", "12345")
assert parse_input("EXIT") == ("exit",)
assert parse_input("") == ("",)
assert parse_input("  ") == ("",)
assert get_output_by_command("hello", [], {}) == ("How can I help you?", False)
assert get_output_by_command("add", [TEST_NAME, PHONE1], {}) == (
    "Contact added.",
    False,
)
assert get_output_by_command("phone", [TEST_NAME], {TEST_NAME: PHONE1}) == (
    f"{TEST_NAME}: {PHONE1}",
    False,
)
assert get_output_by_command("change", [TEST_NAME, PHONE2], {TEST_NAME: PHONE1}) == (
    "Contact updated.",
    False,
)
assert get_output_by_command("all", [], {TEST_NAME: PHONE2}) == (
    f"{TEST_NAME}: {PHONE2}",
    False,
)
assert get_output_by_command("exit", [], {}) == ("Goodbye!", True)
assert get_output_by_command("unknown", [], {}) == (
    "Unknown command. Please try again.",
    False,
)
assert get_output_by_command("phone", ["NonExistent"], {}) == (
    "Contact not found.",
    False,
)
assert get_output_by_command("change", ["NonExistent", PHONE1], {}) == (
    "Contact not found.",
    False,
)
assert get_output_by_command("add", [TEST_NAME], {}) == (
    "Insufficient arguments. Usage: add <name> <phone>",
    False,
)
assert get_output_by_command("change", [TEST_NAME], {}) == (
    "Insufficient arguments. Usage: change <name> <phone>",
    False,
)
assert get_output_by_command("phone", [], {}) == (
    "Insufficient arguments. Usage: phone <name>",
    False,
)
assert get_output_by_command("all", [], {}) == ("No contacts found.", False)
assert get_output_by_command("", [], {}) == (
    "Unknown command. Please try again.",
    False,
)
assert get_output_by_command("add", [], {}) == (
    "Insufficient arguments. Usage: add <name> <phone>",
    False,
)
assert get_output_by_command("change", [], {}) == (
    "Insufficient arguments. Usage: change <name> <phone>",
    False,
)
assert normalize_phone("099 555-1234") == "+380995551234"
assert normalize_phone("+380995551234") == "+380995551234"  
assert normalize_phone("80995551234") == "+380995551234"
assert normalize_phone("380995551234") == "+380995551234"
assert normalize_phone("995551234") == "+995551234"
assert normalize_phone("12345") == ""


# Приклад використання функції:
# Запустіть скрипт і введіть команди "hello" та "exit"  для перевірки роботи бота.
# python task4_bot.py
