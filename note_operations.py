def write_note(input_note: list) -> dict:
    note = {}
    note['заголовок'] = input_note[0]
    note['текст'] = input_note[1]
    note['дата'] = input_note[2]
    return note


def print_notes(allnotes: list) -> str:
    """
    Показывает все заметки в консоли
    """
    # notes_clean_list = []
    # count = 0
    # for note in allnotes:
    #     for key, value in note.items():
    #         notes_clean_list.append(f'{key}: {value}')
    #         count += 1
    #         notes_clean_list.append(' ')
    #         notes_clean_list.append(f'Всего заметок: {count}')
    #         string_result = '\n'.join(notes_clean_list)
    #         return string_result
