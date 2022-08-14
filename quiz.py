import os
import glob
import shutil
from random import randint
from colorama import init

init()


class Quiz:
    def __init__(self, path: str, copy_path: str, quarter, year):
        """"
        ## Description: ##
        Класс осуществляет поиск по заранее обозначенному пути файлов `*.quiz`, заносит путь к файлам в список
        `self.quiz_list`, осуществляет просмотр сформированного списка путей.

        ## :param `path`: str##
        RAW строка. В переменной `path` указан путь к рабочей директорией.

        ## Конструктор: ##
        * `self.path: str` - рабочая директория. Определяется после проверки на существование пути и проверки, того,
        что путь ведёт к директории. Принимает либо путь к рабочей директории, либо значение "Error".
        * `self.quiz_list: list` - храниться полученный список с путями к файлам *.quiz.
        """
        self.path = self.check_path(path)
        self.copy_path = self.check_path(copy_path)
        self.quarter = quarter
        self.year = year
        self.quiz_list = self.find_file()

    def check_path(self, p):
        """
        ## Description: ##
        Метод осуществляет проверку на существование пути в файловой системе и того, что существующий путь,
        является директорией. Если, проверка не пройдена, то выведет, сообщение в консоль об ошибке.

        ##:param `p`: str##
        RAW строка, для проверки пути.
        ##:return: str##
        В случае успешной проверки, возвращает, путь в файловой системе для поиска файлов. В случае неудачи,
        вернёт строку "Error".
        """
        if os.path.exists(p):
            if os.path.isdir(p):
                return p
            else:
                print('\033[31m' + "Указанный путь не является директорией:", p, '\033[39m')
        else:
            print('\033[31m' + "Такой файл или директория не существует:", p, '\033[39m')
        return 'Error'

    def get_path(self):
        """
        ## Description: ##
        Геттер выводит переменную `self.path`

        ##:return:  self.path: str##
        """
        return self.path

    def get_copy_path(self):
        """
        ## Description: ##
        Геттер выводит переменную `self.copy_path`

        ##:return:  self.copy_path: str##
        """
        return self.copy_path

    def get_list(self):
        """
        ## Description: ##
        Метод выводит в консоль пронумерованные элементы списка `self.quiz_list`

        ##:return: str##
        """
        for n, elem in enumerate(self.quiz_list):
            print('\033[32m', n + 1, '\033[36m', elem, '\033[39m')

    def find_file(self):
        """
        ## Description: ##
        Метод осуществляет рекурсивный поиск файлов `*.quiz` в рабочей директории `self.path`, согласно выражению
        `'\**\*Тест\quiz\quiz[0-9].quiz'`, используя функцию glob одноимённого модуля.

        Если, в переменной  `self.path` значение "Error", то список заполняться не будет и `self.quiz_list` будет пуст.
        Если файл обнаружен, то добавляем в список `lst`, который в конструкторе будет присвоен списку `self.quiz_list`.
        :return: list
        """
        lst = []
        if self.path != "Error":
            for elem in sorted(glob.glob(self.path + '\**\\0_Тест\quiz\quiz[0-9].quiz', recursive=True)):
                lst.append(elem)
        return lst

    def copy_quiz(self):
        for elem in self.quiz_list:
            sp = elem.replace(self.path + "\\", '').split("\\")
            copy_dir = self.copy_path + f"\\Контрольные за {self.quarter}кв {self.year}\\{sp[0]}\\kontrol01"
            file = sp[-1]
            if os.path.exists(copy_dir) == False:
                os.makedirs(copy_dir)
            if os.path.exists(f"{copy_dir}\\{file}"):
                suffix = randint(1, 999)
                file = file[:-5] + f"_{suffix}" + file[-6:]
            shutil.copy2(elem, f"{copy_dir}\\{file}")