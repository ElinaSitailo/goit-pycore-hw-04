from faker import Faker
import random

fake = Faker("en_US")


def get_mocked_cat_record():
    fake = Faker()
    mock = {
        "id": "".join(random.choices("0123456789abcdef", k=24)),
        "name": fake.first_name(),
        "age": fake.unique.random_int(min=1, max=20),
    }
    return mock


def get_mocked_salary_record():
    fake = Faker()
    salary = fake.unique.random_int(min=10000, max=200000)
    mock = {"full_name": fake.name(), "salary": round(salary, -2)}
    return mock
