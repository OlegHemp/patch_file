from quiz import Quiz


def main():
    """
    ## Description: ##
    Функция получает входные данные по которым "строит" путь к рабочей директории, создаёт три объекта
    класса Quiz, которые копируют файлы из рабочей директории. Копирование производится с помощью
    метода copy_quiz().
    `year`: str: Год
    `quarter`: int: Значение квартала.
    `list_quarter`: dict[int, List[str]]: Словарь кварталов, содержит часть пути рабочей директории
    `SW_PATH`: str: Рабочая директория. При необходимости, можно править.
    `COPY_PATH`: str: Директория, куда необходимо копировать файлы. При необходимости, можно править.
    :return:
    """
    year = input("Введите год (ГГГГ):")
    quarter = int(input("Введите квартал (от 1 до 4):"))
    list_quarter = {1: ["01_Январь", "02_Февраль", "03_Март"],
                    2: ["04_Апрель", "05_Май", "06_Июнь"],
                    3: ["07_Июль", "08_Август", "09_Сентябрь"],
                    4: ["10_Октябрь", "11_Ноябрь", "12_Декабрь"],
                    }
    SW_PATH = r"C:\python_file\Skillbox\patch_file\B_E_G_I_N_folder" + f"\\_{year}"
    COPY_PATH = r"C:\python_file\Skillbox\patch_file\C_O_P_Y_2001_2022"
    q1 = Quiz(SW_PATH + f"\\{list_quarter[quarter][0]}", COPY_PATH, quarter, year)
    q2 = Quiz(SW_PATH + f"\\{list_quarter[quarter][1]}", COPY_PATH, quarter, year)
    q3 = Quiz(SW_PATH + f"\\{list_quarter[quarter][2]}", COPY_PATH, quarter, year)
    print("Вывод рабочей директории:", q1.get_path())
    print("Вывод рабочей директории:", q2.get_path())
    print("Вывод рабочей директории:", q3.get_path())
    print("Вывод директории для записи:", q1.get_copy_path())
    print(f"\nКопируем тесты за {list_quarter[quarter][0]}:")
    q1.get_list()
    q1.copy_quiz()
    print(f"\nКопируем тесты за {list_quarter[quarter][1]}:")
    q2.get_list()
    q2.copy_quiz()
    print(f"\nКопируем тесты за {list_quarter[quarter][2]}:")
    q3.get_list()
    q3.copy_quiz()

if __name__ == '__main__':
    main()
