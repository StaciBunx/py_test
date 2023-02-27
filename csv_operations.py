import csv

global notes_csv

notes_csv = 'notes_csv.csv'


def write_csv(input_note: dict) -> None:
    '''Принимает новые значения в виде словаря, записывает новую заметку в cvs файл'''
    with open(notes_csv, 'a', encoding='utf-8', newline='') as file:
        fieldnames = ['заголовок', 'текст', 'дата']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writerow(input_note)


def print_cvs():
    '''
    Печатает все содержимое файлы csv
    '''
    with open(notes_csv, 'r', encoding='utf-8', newline='') as file:
        reader = csv.reader(file, delimiter=',')
        for row in reader:
            print('\n'.join(row))
            print('\n')


def print_note_by_date(date_input: str) -> None:
    ''' Печатает только те заметки, которые совпадают с запрашиваемой датой'''
    with open(notes_csv, 'r', encoding='utf-8', newline='\n') as file:
        reader = csv.reader(file, delimiter=',')
        for row in reader:
            if date_input in row:
                print('\n'.join(row))
                print('\n')


def delete_csv(input_string: str) -> None:
    '''
    Удаляет заметку из файла cvs. Ищет в файле строку с искомым значением, остальные строки записывает во времемнное хранилище.
    Затем значения из временного хранилища перезаписывает в файл, стирая предыдущие данные.
    '''
    temp_string = ''
    with open(notes_csv, 'r', encoding='utf-8', newline='\n') as file:
        reader = csv.reader(file)
        for row in reader:
            note = ','.join(row).lower()
            if input_string.lower() in note:
                continue
            else:
                temp_string += f'{note}\n'
    with open(notes_csv, 'w', encoding='utf-8', newline='\n') as file:
        file.write(temp_string)


def search_note_by_input(search_input: str) -> str:
    """
    Ищет заметку содержащую текст из запроса, возвращает строку с найденной заметкой
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
