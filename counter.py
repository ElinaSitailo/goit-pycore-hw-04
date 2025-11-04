import copy
import pickle


class Person:
    def __init__(self, name: str, email: str, phone: str, favorite: bool):
        self.name = name
        self.email = email
        self.phone = phone
        self.favorite = favorite

    def __copy__(self):
        # Повертає поверхневу копію об’єкта Person
        return type(self)(
            self.name,
            self.email,
            self.phone,
            self.favorite
        )
            
        
class Contacts:
    def __init__(self, filename: str, contacts: list[Person] = None):
        if contacts is None:
            contacts = []
        self.filename = filename
        self.contacts = contacts
        self.is_unpacking = False
        self.count_save = 0

    def save_to_file(self):
        with open(self.filename, "wb") as file:
            pickle.dump(self, file)

    def read_from_file(self):
        with open(self.filename, "rb") as file:
            content = pickle.load(file)
        return content

    def __getstate__(self):
        attributes = self.__dict__.copy()
        attributes["count_save"] = attributes["count_save"] + 1
        return attributes

    def __setstate__(self, value):
        self.__dict__ = value
        self.is_unpacking = True

    def __copy__(self):
        # Створюємо новий екземпляр Contacts з поверхневою копією списку контактів
        new_copy = type(self)(
            self.filename,
            self.contacts.copy()
        )
        new_copy.count_save = self.count_save
        new_copy.is_unpacking = self.is_unpacking
        return new_copy

    def __deepcopy__(self, memo):
        # Створюємо новий екземпляр Contacts з глибокою копією списку контактів
        new_copy = type(self)(
            copy.deepcopy(self.filename, memo),
            copy.deepcopy(self.contacts, memo)
        )
        new_copy.count_save = self.count_save
        new_copy.is_unpacking = self.is_unpacking
        return new_copy
        
        

DATA = [{'name': 'Allen Raymond', 'email': 'nulla.ante@vestibul.co.uk', 'phone': '(992) 914-3792', 'favorite': True},
         {'name': 'Chaim Lewis', 'email': 'dui.in@egetlacus.ca', 'phone': '(294) 840-6685', 'favorite': True}]
persons = Contacts("user_class.dat1", DATA)
persons.save_to_file()
first = persons.read_from_file()
first.save_to_file()
second = first.read_from_file()
second.save_to_file()
third = second.read_from_file()

print(persons.count_save)  # 0
print(first.count_save)  # 1
print(second.count_save)  # 2
print(third.count_save)  # 3        