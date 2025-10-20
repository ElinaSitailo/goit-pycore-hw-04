# Функція total_salary(path) має приймати один аргумент -
#   шлях до текстового файлу (path).
# Файл містить дані про заробітні плати розробників, розділені комами.
#   Кожен рядок вказує на одного розробника.
# Функція повинна аналізувати файл,
#   обчислювати загальну та середню суму заробітної плати.
# Результатом роботи функції є кортеж із двох чисел:
#   загальної суми зарплат і середньої заробітної плати.


# The method to calculate total and average salary
def total_salary(path):
    total = 0 
    count = 0
    try:
        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                line_values = line.strip().split(",")
                if len(line_values) >= 2:
                    salary = line_values[
                        1
                    ].strip()  # Зарплата знаходиться в другій колонці
                    if salary.isdigit():
                        total += int(salary)
                        count += 1
    except Exception as e:
        print(f"Не можу обробити файл: {path}. Помилка обробки: {e}")
        return 0, 0

    print(f"Сума заробітних плат: {total}. Кількість рядків ззарплатою: {count}")    
    average = total / count if count > 0 else 0
    return total, average


def main():
    total, average = total_salary("testdata/salary.txt")
    print(
        f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}"
    )


if __name__ == "__main__":
    main()

# для оновлення тестових даних активуйте середовище .env (.\.env\Scripts\Activate.ps1) та запустіть:  
    # python ./testdata/main.py
# цей файл працює без середовища
