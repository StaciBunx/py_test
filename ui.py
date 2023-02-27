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
          '1 - 📜 Просмотреть все заметки \n'
           '2 - 👀 Просмотреть заметки по...  \n'
           '3 - ✍️  Добавить новую заметку \n'
           '4 - ✈️  Завершить работу\n'
           f'{Style.RESET_ALL}'))
    return ch.check_menu(number, 5)


def search_submenu(number: str = '') -> int:
    '''
    Подменю для поиска записей.
    '''
    print(f'{Style.BRIGHT + Fore.YELLOW}Выберите по какому параметру будет поиск (введите 1 или 2): {Style.RESET_ALL} \n'
          '1 - 🔡 ...тексту записи \n'
          '2 - 📆 ...дате записи')
    return ch.check_menu(number, 3)


def note_not_found():
    print('По вашему запросу ничего не найдено')


def note_found(find_note: str) -> None:
    print(f'Найдена заметка:\n{find_note}')


def search_submenu_action(number: str = '') -> str:
    '''
    Подменю после вызова поиска записи
    '''
    print((f'{Style.BRIGHT + Fore.YELLOW}👀 Выберите дальнейшее действие для работы: {Style.RESET_ALL} \n'
           '1 - 🧹 Удалить заметку \n'
           '2 - ✏️  Редактировать заметку'))
    return ch.check_menu(number, 3)


def search_input(text: str = '') -> str:
    '''Ввод запроса в поисковую строку'''
    print((
        f'{Style.BRIGHT + Fore.YELLOW}✍️  Введите текст для поиска:{Style.RESET_ALL} '))
    return ch.check_empty(text)


def search_date(date: str = '') -> str:
    '''Ввод запроса в поисковую строку'''
    print((
        f'{Style.BRIGHT + Fore.YELLOW}✍️  Введите дату в формате YYYY-MM-DD:{Style.RESET_ALL} '))
    return ch.check_empty(date)

def input_new_note() -> list:
    '''
    Функция добавляет новые данные, возвращает список. Дата добавляется автоматически на момент создания заметки.
    '''
    note = []
    print((
        f'{Style.BRIGHT + Fore.YELLOW}✍️ Введите данные: {Style.RESET_ALL}'))
    heading = ch.check_empty('Заголовок: ')
    heading = heading.capitalize()
    note.append(heading)
    text = ch.check_empty('Текст: ')
    note.append(text)
    current_date = date.today()
    note.append(current_date)
    return note
