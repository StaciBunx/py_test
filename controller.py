import csv_operations as csvo
import ui
import log
from datetime import *


def mynotes():
    ui.hello()
    while True:
        command = ui.notes_menu()
        if command == 1:  # просмотре всех записей
            csvo.print_notes(csvo.read_csv)
            log.log('Просмотр всех заметок', 'Успешно')
        # if command == 2:  # поиск записи по дате

        if command == 3:  # добавить новую запись
            input_note = ui.input_new_note()
            input_note = note.lower()
            note = {}
            all_notes = csvo.read_csv()
            note['заголовок'] = input_note[0]
            note['текст'] = input_note[1]
            note['дата'] = date
            csvo.write_csv(note)

        # if command == 4:  # завершить работу
