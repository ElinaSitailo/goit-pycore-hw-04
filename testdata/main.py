import get_mocked_record as mock

CATS_FILE_PATH = "testdata/cats.txt"
SALARY_FILE_PATH = "testdata/salary.txt"
RECORD_COUNT = 10

def fill_cats_test_data():
    with open(CATS_FILE_PATH, "w", encoding="utf-8") as file:
        for _ in range(RECORD_COUNT):
            record = mock.get_mocked_cat_record()
            line = f"{record['id']},{record['name']},{record['age']}\n"
            file.write(line)


def fill_salary_test_data():
    with open(SALARY_FILE_PATH, "w", encoding="utf-8") as file:
        for _ in range(RECORD_COUNT):
            record = mock.get_mocked_salary_record()
            line = f"{record['full_name']},{record['salary']}\n"
            file.write(line)


def main():
    fill_cats_test_data()
    fill_salary_test_data()
    print(
        f"Test data files have been created. See '{CATS_FILE_PATH}' and '{SALARY_FILE_PATH}'."
    )


if __name__ == "__main__":
    main()
