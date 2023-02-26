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
            log.log('Просмотр всех заметок', 'Успешно')
        if command == 2:  # поиск записи
            next_command = ui.search_submenu()
            if next_command == 1: #поиск по тексту
                search_input = ui.search_input()
                csvo.search_note_by_input(search_input)
                log.log('Поиск заметки по тексту', 'Успешно')
                action_command = ui.search_submenu_action
                # if action_command = 1: #удаление записи
                # if action_command = 2: #редакирование записи

            # if next_command ==2: #поиск по дате

        if command == 3:  # добавить новую запись
            input_note = ui.input_new_note()
            note = noto.write_note(input_note)
            csvo.write_csv(note)
            ui.success()
            log.log('Добавить новую запись', 'Успешно')
        if command == 4:  # завершить работу
            ui.bye()
            log.log('Завершение работы', 'Успешно')
            break
