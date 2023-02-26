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


# def check_length(length: str) -> str:
#     '''Проверка длины вводимой строки и тут же проверка на пустую строку'''
#     while True:
#         try:
#             l = input(length)
#             if len(l) == 0:
#                 print(Fore.RED + 'Вы ничего не ввели!' + Style.RESET_ALL)
#             elif len(l) < 280:
#                 return l
#             else:
#                 print(Fore.RED + 'Вы ввели слишком длинный текст! ' + Style.RESET_ALL)
#         except ValueError:
#             print(Fore.RED + 'Неверно! Повторите ввод!' + Style.RESET_ALL)


def check_empty(text: str) -> str:
    '''Проверка на буквы (не допускает ввода пустой строки)'''
    while True:
        try:
            a = input(text)
            if (len(a)!=0):
                return a
            else:
                print(
                    Fore.RED + 'Вы ничего не ввели!' + Style.RESET_ALL)
        except ValueError:
            print(Fore.RED + 'Неверно!' + Style.RESET_ALL)
