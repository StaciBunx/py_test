from colorama import *
import check as ch
from datetime import date


def hello():
    '''
    Приветсвует пользователя
    '''
    print((
        f'{Style.BRIGHT + Fore.GREEN}Добро пожаловать!🖐️{Style.RESET_ALL}'))


def bye():
    '''
    Прощается с пользователем
    '''
    print((
        f'{Style.BRIGHT + Fore.GREEN}До встречи!🤗{Style.RESET_ALL}'))


def success():
    print((
        f'{Style.BRIGHT + Fore.YELLOW}✅ Успешно!{Style.RESET_ALL}'))


def notes_menu(number: str = '') -> int:
    '''
    Вывод в консоль меню приложения. В возврате запускает модуль проверки, где функция принимает число от пользователя, проверяет и возвращает его.
    '''

    print((f'{Style.BRIGHT + Fore.YELLOW}\nВыберите действие с записной книжкой (введите цифру от 1 до 4): \n{Style.RESET_ALL}'
          '1 - 📜 Просмотреть все записи \n'
           '2 - 👀 Поиск записи по дате \n'
           '3 - ✍️ Добавить новую запись \n'
           '4 - ✈️ Завершить работу\n'
           f'{Style.RESET_ALL}'))
    return ch.check_menu(number, 5)


# def input_search(number: str = '') -> str:
#     '''
#     Подменю для поиска контакта.
#     '''
#     print(e.emojize(f'{Style.BRIGHT + Fore.YELLOW}Выберите по какому параметру будет поиск (введите 1 или 2): {Style.RESET_ALL} \n'
#                     '1 - :input_latin_lowercase: По имени \n'
#                     '2 - :input_numbers: По номеру телефона'))
#     return ch.check_phone_menu(number, 3)


def search_submenu(number: str = '') -> int:
    '''
    Подменю после вызова поиска записи
    '''
    print((f'{Style.BRIGHT + Fore.YELLOW}:eyes:  Выберите действие для работы: {Style.RESET_ALL} \n'
           '1 - 🧹 Удалить запись \n'
           '2 - ✏️Редактировать запись'))
    return ch.check_menu(number, 3)


def print_all(data_list: list) -> None:
    '''
    Вывод всех записей в консоль
    '''
    print((
        f'{Style.BRIGHT + Fore.YELLOW}📜Ваши записи: {Style.RESET_ALL}'))
    for line in data_list:
        print(line)


def print_note(contact_data: str = '') -> None:
    '''
    Выводит определенную запись в консоль, н-р после поиска, или редактирования, или добавления.
    '''
    print(e.emojize(
        f'{Style.BRIGHT + Fore.YELLOW}💟Ваша запись: \n {contact_data}{Style.RESET_ALL}'))


def input_new_note() -> list:
    '''
    Функция добавляет новые данные, возвращает строку.
    '''
    note = []
    print((
        f'{Style.BRIGHT + Fore.YELLOW}✍️  Добавьте новую запись: {Style.RESET_ALL}'))
    heading = ch.check_alpha('Заголовок: ')
    heading = heading.capitalize()
    note.append(heading)
    text = ch.check_alpha('Текст: ')
    text = text.capitalize()
    note.append(text)
    current_date = date.today()
    note.append(current_date)
    return note


def edit_data(note_data: str = '') -> str:
    '''
    Функция перезаписывает новые данные поверх имеющейся записи
    '''
    print((
        f'{Style.BRIGHT + Fore.YELLOW}📇Введите новые данные: {Style.RESET_ALL}'))
    return ch.check_length(note_data)

# def search(contact: str = '') -> None:
#     '''
#     Ввод в поисковую строку и поиск
#     '''
#     contact = str(input(e.emojize(
#         f'{Style.BRIGHT + Fore.YELLOW}:writing_hand: Введите искомый контакт:{Style.RESET_ALL} '))).capitalize()
#     return
