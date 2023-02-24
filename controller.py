import csv_operations as csvo
import note_operations as noto
import ui
import log
from datetime import *


def mynotes():
    ui.hello()
    while True:
        command = ui.notes_menu()
        if command == 1:  # просмотр всех записей
            csvo.print_cvs()
            # csvo.print_notes(csvo.read_csv)
            # all_notes_list = csvo.read_csv()
            # print(noto.print_notes(all_notes_list))
            # log.log('Просмотр всех заметок', 'Успешно')
        # if command == 2:  # поиск записи по дате

        if command == 3:  # добавить новую запись
            input_note = ui.input_new_note()
            note = noto.write_note(input_note)
            csvo.write_csv(note)
            ui.success()

        if command == 4:  # завершить работу
            ui.bye()
            break
