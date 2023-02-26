import csv

global notes_csv

notes_csv = 'notes_csv.csv'


def read_csv() -> list:
    '''Чтение файла csv, возвращает список со словарем.'''
    allnotes = []
    with open(notes_csv, 'r', encoding='utf-8', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            allnotes.append(row)
    return allnotes


def write_csv(input_note: dict):
    '''Принимает новые значения в виде словаря, записывает новую заметку в cvs файл'''
    with open(notes_csv, 'a', encoding='utf-8', newline='') as file:
        fieldnames = ['заголовок', 'текст', 'дата']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writerow(input_note)


def print_cvs():
    with open(notes_csv, 'r', encoding='utf-8', newline='') as file:
        reader = csv.reader(file, delimiter=',')
        for row in reader:
            print('\n'.join(row))
            print('\n')


def delete_csv(input_string: str) -> None:
    '''
    Удаляет задачу из файла cvs. Ищет в файле строку с искомым значением, остальные строки записывает во времемнное хранилище.
    Затем значения из временного хранилища перезаписывает в файл, стирая предыдущие данные.
    Возвращает строку с информацией о ходе выполнения задачи.
    '''
    temp_string = ''
    found_note =''
    with open(notes_csv, 'r', encoding='utf-8', newline='\n') as file:
        reader = csv.reader(file)
        for row in reader:
            note = ','.join(row).lower()
            if input_string.lower() in note:
                found_note = note
                continue
            else:
                temp_string += f'{note}\n'
    with open(notes_csv, 'w', encoding='utf-8', newline='\n') as file:
        file.write(temp_string)


def search_note_by_input(search_input: str) -> str:
    """
    Ищет контакт по запросу
    """
    with open(notes_csv, 'r', encoding='utf-8', newline='\n') as file:
        reader = csv.reader(file)
        find_note = ''
        for row in reader:
            note = '\n'.join(row).lower()
            if search_input.lower() in note:
                find_note = note.capitalize()
                continue
    return find_note




# def search_contact(contact):
#     """
#     Ищет контакт по запросу
#     """
#     with open(t, 'r', encoding='utf-8') as f:
#         search_contact =''
#         for line in f:
#             if contact in line:
#                 print(line)
#                 search_contact = line
#         return search_contact


# def save_note(note):
#     """
#     Функция записывает новую заметку
#     """
#     with open(notes, 'a', encoding='utf-8') as file:
#         file.write(f"\n{note}")

# def delete_note(contact):
#     """
#     Удаляет заметку
#     """
#     f = open(notes, 'r', encoding='utf-8')
#     lines = f.readlines()
#     f.close()
#     f = open(t, 'w', encoding='utf-8')
#     for line in lines:
#         if line != contact:
#             f.write(line)
#     f.close()
