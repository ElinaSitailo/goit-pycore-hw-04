# Функція get_cats_info(path) має приймати один аргумент
# - шлях до текстового файлу (path).
# Файл містить дані про котів, де кожен запис містить унікальний ідентифікатор,
#   ім'я кота та його вік.
# Функція має повертати список словників,
#   де кожен словник містить інформацію про одного кота.
def get_cats_info(path):
    cats = []

    lines_total = 0
    valid_lines = 0
    try:
        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                line_values = line.strip().split(",")
                lines_total += 1
                if len(line_values) == 3:
                    cat_id = line_values[0].strip()
                    name = line_values[1].strip()
                    age = line_values[2].strip()
                    if age.isdigit():
                        cats.append({"id": cat_id, "name": name, "age": int(age)})
                        valid_lines += 1
            print(
                f"Загальна кількість рядків: {lines_total}. Кількість рядків про котиків: {valid_lines}"
            )
    except Exception as e:
        print(f"Не можу обробити файл: {path}. Помилка обробки: {e}")
        return []
    return cats


def main():
    cats_info = get_cats_info("testdata/cats.txt")
    print(cats_info)


if __name__ == "__main__":
    main()

# для оновлення тестових даних активуйте середовище .env (.\.env\Scripts\Activate.ps1) та запустіть:
# python ./testdata/main.py
# Цей файл працює без середовища
