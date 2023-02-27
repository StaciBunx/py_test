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
        elif command == 2:  # поиск записи
            next_command = ui.search_submenu()
            if next_command == 1:  # поиск по тексту
                search_input = ui.search_input()
                find_note = csvo.search_note_by_input(search_input)
                if (find_note == ''):
                    log.log('Поиск заметки по тексту', 'Ошибка')
                    ui.note_not_found()
                else:
                    log.log('Поиск заметки по тексту', 'Успешно')
                    ui.note_found(find_note)
                    action_command = ui.search_submenu_action()
                    if action_command == 1:  # удалить запись
                        log.log('Удаление записи', 'Успешно')
                        csvo.delete_csv(search_input)
                        ui.success()
                    elif action_command == 2:
                        edit_note = ui.input_new_note()
                        csvo.delete_csv(search_input)
                        note = noto.write_note(edit_note)
                        csvo.write_csv(note)
                        log.log('Перезапись заметки', 'Успешно')
                        ui.success()
            elif next_command == 2:  # вывод заметок по дате
                search_date = ui.search_date()
                csvo.print_note_by_date(search_date)
                log.log('Печать заметок по дате', 'Успешно')
        if command == 3:  # добавить новую запись
            input_note = ui.input_new_note()
            note = noto.write_note(input_note)
            csvo.write_csv(note)
            ui.success()
            log.log('Добавить новую заметку', 'Успешно')
        if command == 4:  # завершить работу
            ui.bye()
            log.log('Завершение работы', 'Успешно')
            break
