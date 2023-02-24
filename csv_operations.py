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

# def delete_csv(search_data: str) -> str:
#     '''
#     Удаляет задачу из файла cvs. Ищет в файле строку с искомым значением, остальные строки записывает во времемнное хранилище.
#     Затем значения из временного хранилища перезаписывает в файл, стирая предыдущие данные.
#     Возвращает строку с информацией о ходе выполнения задачи.
#     '''
#     temp_string = ''
#     status = ''
#     found_note = ''
#     with open(notes_csv, 'r', encoding='utf-8', newline='\n') as file:
#         reader = csv.reader(file)
#         for row in reader:
#             note = ','.join(row).lower()
#             if search_data in note:
#                 found_note = note
#                 continue
#             else:
#                 temp_string += f'{note}\n'
#     with open(notes_csv, 'w', encoding='utf-8', newline='\n') as file:
#         file.write(temp_string)
#     if (found_note == ''):
#         status = f'Не найдено заметок c этой датой"{search_data}"'
#     else:
#         status = f'Вы удалили из заметок:\n{found_note}'
#     return status


def search_note_by_data(search_data: str) -> str:
    """
    Ищет контакт по запросу
    """
    with open(notes_csv, 'r', encoding='utf-8', newline='\n') as file:
        reader = csv.reader(file)
        for row in reader:

            find_note = ','.join(row).lower()
            if search_data in find_note:
                return find_note
            else:
                print(f'Не найдено заметок c этой датой"{search_data}"')


def edit_note(find_note: str, new_note: str):
    """
    Редактирует заметку

    """
    temp_string = ''
    temp_note = ''
    with open(notes_csv, 'r', encoding='utf-8', newline='\n') as file:
        reader = csv.reader(file)
        for row in reader:
            note = ','.join(row).lower()
            if find_note.lower() in note:
                temp_note = new_note
                continue
            else:
                temp_string += f'{note}\n'
        temp_string += f'{temp_note}\n'
    with open(notes_csv,'w', encoding='utf-8', newline='\n') as file:
        file.write(temp_string)
    if (temp_note == ''):
        return f'Не найдено задач по запросу {find_note}'
    else:
         return f'Успешно перезаписно'



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
