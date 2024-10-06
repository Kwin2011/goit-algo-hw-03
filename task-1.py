import os
import shutil
import sys


def show_directory_contents(directory_path):
    #Виводить всі файли та папки вказаної директорії у зручному вигляді
    print(f"\nВміст теки {directory_path}:")
    for current_path, folders, files in os.walk(directory_path):
        # Рахуємо рівень вкладеності директорії для відступів
        depth = current_path.replace(directory_path, '').count(os.sep)
        indent = ' ' * 4 * depth
        print(f"{indent}{os.path.basename(current_path)}/")
        sub_indent = ' ' * 4 * (depth + 1)
        for file in files:
            print(f"{sub_indent}{file}")


def get_args():
    """Отримуємо аргументи командного рядка"""
    if len(sys.argv) < 2:
        print("Будь ласка, вкажіть шлях до вихідної теки.")
        sys.exit(1)

    source_directory = sys.argv[1]
    target_directory = sys.argv[2] if len(sys.argv) > 2 else 'dist'

    return source_directory, target_directory


def organize_files_by_extension(source_directory, target_directory):
    """Копіює файли з вихідної теки до нової, сортує їх за розширеннями"""
    try:
        if not os.path.exists(target_directory):
            os.makedirs(target_directory)

        for current_path, folders, files in os.walk(source_directory):
            for file in files:
                file_full_path = os.path.join(current_path, file)
                # Визначаємо розширення файлу або позначаємо його як "без розширення"
                file_extension = file.split('.')[-1] if '.' in file else 'no_extension'
                destination_folder = os.path.join(target_directory, file_extension)

                if not os.path.exists(destination_folder):
                    os.makedirs(destination_folder)

                shutil.copy(file_full_path, destination_folder)

    except Exception as error:
        print(f"Виникла помилка під час копіювання: {error}")


def main():
    # Отримуємо вихідну і цільову теки
    source_directory, target_directory = get_args()

    # Виводимо вміст вихідної теки до сортування
    show_directory_contents(source_directory)

    # Копіюємо файли та сортуємо їх
    organize_files_by_extension(source_directory, target_directory)

    # Виводимо вміст цільової теки після сортування
    show_directory_contents(target_directory)


if __name__ == "__main__":
    main()
