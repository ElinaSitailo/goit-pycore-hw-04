import csv

DATA = [{'name': 'Allen Raymond', 'email': 'nulla.ante@vestibul.co.uk', 'phone': '(992) 914-3792', 'favorite': True},
         {'name': 'Chaim Lewis', 'email': 'dui.in@egetlacus.ca', 'phone': '(294) 840-6685', 'favorite': True}]

FILENAME = "data.csv"


def write_contacts_to_file(filename, contacts):
    with open(filename, "w", encoding="utf-8", newline="") as f:
        columns = contacts[0].keys()
        writer = csv.DictWriter(f, delimiter=",", fieldnames=columns)
        writer.writeheader()
        writer.writerows(contacts)
    
        
def read_contacts_from_file(filename):
    with open(filename, "r", newline="", encoding="utf-8") as fh:
        reader = csv.DictReader(fh)

        result_list = []
        for row in reader:
            f = row["favorite"] == "True"
            result_list.append(
                {
                    "name": row["name"],
                    "email": row["email"],
                    "phone": row["phone"],
                    "favorite": f
                }
            )
        return result_list


write_contacts_to_file(FILENAME, DATA)
result = read_contacts_from_file(FILENAME)
print(result)
