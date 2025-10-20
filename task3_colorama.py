# Створіть віртуальне оточення Python для ізоляції залежностей проекту.
# Скрипт має отримувати шлях до директорії як аргумент при запуску.
#   Цей шлях вказує, де знаходиться директорія, структуру якої потрібно відобразити.
# Використання бібліотеки colorama для реалізації кольорового виведення.
# Скрипт має коректно відображати як імена директорій,
#   так і імена файлів, використовуючи рекурсивний спосіб обходу директорій (можна, за бажанням, використати не рекурсивний спосіб).
# Повинна бути перевірка та обробка помилок, наприклад,
#    якщо вказаний шлях не існує або він не веде до директорії.
import sys
from pathlib import Path
from colorama import Fore, Style, init


# Ініціалізація colorama
init(autoreset=True)

SPACES =' '*6

def print_directory(path, prefix="") -> int:
    exit_code = 0
    try:
        path_obj = Path(path)
        dir_entries = sorted(path_obj.iterdir())
       
    except Exception as e:
        print(f"{Fore.RED}Error accessing directory {path}: {e}{Style.RESET_ALL}")
        exit_code = 1 
        return exit_code
        
    for entry in dir_entries:      
        if entry.is_dir():
            print(f"{prefix}{SPACES}{Fore.BLUE}{entry.name}{Style.RESET_ALL}")
            new_prefix = f"{prefix}{SPACES}"
            print_directory(entry, new_prefix)
        else: #file
            print(f"{prefix}{SPACES}{Fore.GREEN}{entry.name}{Style.RESET_ALL}")        

    return exit_code

def process_path(dir_path) -> int:
    exit_code = 0
    path_obj = Path(dir_path)

    if not path_obj.exists():
        print(f"{Fore.RED}The path '{dir_path}' does not exist.{Style.RESET_ALL}")
        exit_code = 1
    elif not path_obj.is_dir():
        print(f"{Fore.RED}The path '{dir_path}' is not a directory.{Style.RESET_ALL}")
        exit_code = 1
    else:
        print(f"{Fore.YELLOW}Directory structure of: {dir_path}{Style.RESET_ALL}")
        exit_code = print_directory(path_obj)
        
    return exit_code


def main():
    if len(sys.argv) > 1:
        dir_path = sys.argv[1]
        exit_code = 0
        try:    
            exit_code = process_path(dir_path)
        except Exception as e:
            print(f"{Fore.RED}An unexpected error occurred: {e}{Style.RESET_ALL}")
            exit_code = 1
        sys.exit(exit_code)
    else:
        print(f"{Fore.RED}Please provide a directory path as an argument.{Style.RESET_ALL}")
        sys.exit(1)
 
if __name__ == "__main__":
    main()

# активуйте середовище .env (.\.env\Scripts\Activate.ps1) та запустіть:
# python task3_colorama.py .
# or
# python task3_colorama.py c:\Users\Public\Music\