import pickle


class Person:
    def __init__(self, name: str, email: str, phone: str, favorite: bool):
        self.name = name
        self.email = email
        self.phone = phone
        self.favorite = favorite
        
        
        


class Contacts:
    def __init__(self, filename: str, contacts: list[Person] = None):

        self.filename = filename
        if contacts is None:
            contacts = []
        else:
            self.contacts = contacts
        
        

    def save_to_file(self):
        with open(self.filename, "wb") as fh:
            pickle.dump(self.contacts, fh)
            

    def read_from_file(self):
        with open(self.filename, "rb") as fh:
            self.contacts = pickle.load(fh)
            return contacts



contacts = [
    Person(
        "Allen Raymond",
        "nulla.ante@vestibul.co.uk",
        "(992) 914-3792",
        False,
    ),
    Person(
        "Chaim Lewis",
        "dui.in@egetlacus.ca",
        "(294) 840-6685",
        False,
    ),
]

persons = Contacts("user_class.dat", contacts)

persons.save_to_file()
r = persons.read_from_file()
print(r[0].name)