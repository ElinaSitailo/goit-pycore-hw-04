import json

DATA = [
    {
        "name": "Allen Raymond",
        "email": "nulla.ante@vestibul.co.uk",
        "phone": "(992) 914-3792",
        "favorite": False,
    },
    {
        "name": "Vasya Pupkin",
        "email": "vasya.pupkin@gmail.com",
        "phone": "(992) 111-2222",
        "favorite": True,
    },
]

DICT_KEY = "contacts"

FILENAME = "data.json"


def write_contacts_to_file(filename, input_list):
    with open(filename, "w") as fh:
        dict_to_save = {DICT_KEY: input_list}
        json.dump(dict_to_save, fh, indent=2)


def read_contacts_from_file(filename):
    with open(filename, "r") as fh:
        unpacked = json.load(fh)
        return unpacked[DICT_KEY]


write_contacts_to_file(FILENAME, DATA)
result = read_contacts_from_file(FILENAME)
print(result)