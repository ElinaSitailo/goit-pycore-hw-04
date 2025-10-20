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


def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."


def update_contact(args, contacts):
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return "Contact updated."
    else:
        return "Contact not found."


def show_contact(args, contacts):
    name = args[0]
    if name in contacts:
        return f"{name}: {contacts[name]}"
    else:
        return "Contact not found."


def show_all_contacts(contacts):
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
PHONE1 = "555-1234"
PHONE2 = "555-5678"
assert parse_input("  AdD  John  12345 ") == ("add", "John", "12345")
assert parse_input("EXIT") == ("exit",)
assert get_output_by_command("hello", [], {}) == ("How can I help you?", False)
assert get_output_by_command("add", [TEST_NAME, PHONE1], {}) == ("Contact added.", False)
assert get_output_by_command("phone", [TEST_NAME], {TEST_NAME: PHONE1}) == (f"{TEST_NAME}: {PHONE1}",False)
assert get_output_by_command("change", [TEST_NAME, PHONE2], {TEST_NAME: PHONE1}) == ("Contact updated.", False)
assert get_output_by_command("all", [], {TEST_NAME: PHONE2}) == (f"{TEST_NAME}: {PHONE2}", False)

# Приклад використання функції:
# Запустіть скрипт і введіть команди "hello" та "exit"  для перевірки роботи бота.
# python task4_bot.py
