from colorama import *


def check_menu(num: str, menu_num: int) -> int:
    '''Валидирует выбор пользователя в меню приложения. Если вводится число, которого нет в выборе - выдает ошибку'''
    while True:
        try:
            n = int(input(num))
            if 0 < int(n) < menu_num:
                return n
            else:
                print(
                    Fore.RED + f'Неверно! Введите число от 1 до {menu_num-1} в соответствии с пунктами меню!' + Style.RESET_ALL)
        except ValueError:
            print(
                Fore.RED + f'Неверно! Введите число от 1 до {menu_num-1} в соответствии с пунктами меню!' + Style.RESET_ALL)


def check_empty(text: str) -> str:
    '''Проверка - не допускает ввода пустой строки'''
    while True:
        try:
            input_str = str(input(text))
            if (len(input_str) != 0):
                return input_str
            else:
                print(
                    Fore.RED + 'Вы ничего не ввели!' + Style.RESET_ALL)
        except ValueError:
            print(Fore.RED + 'Неверно!' + Style.RESET_ALL)


# def check_alpha(text: str) -> str:
#     while True:
#         try:
#             input_str = str(text)
#             if (input_str.isalpha()):
#                 return input_str
#             else:
#                 print(Fore.RED + 'Вы ввели не текст' + Style.RESET_ALL)
#         except ValueError:
#             print(Fore.RED + 'Неверно!' + Style.RESET_ALL)


def check_digit(date: str) -> int:
    date.replace('-', '')
    try:
        if (date.isdigit()):
            return date
        else:
            print(Fore.RED + 'Вы ввели что-то не то' + Style.RESET_ALL)
    except ValueError:
        print(Fore.RED + 'Неверно!' + Style.RESET_ALL)


# def check_empty(input:str) -> str:
#     '''Проверка на буквы (не допускает ввода пустой строки)'''
#     while True:
#         try:
#             if (len(input) != 0):
#                 return input
#             else:
#                 print(
#                     Fore.RED + 'Вы ничего не ввели!' + Style.RESET_ALL)
#                 break
#         except ValueError:
#             print(Fore.RED + 'Неверно!' + Style.RESET_ALL)
