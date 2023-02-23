def write_note(input_note: list) -> dict:
    note = {}
    note['заголовок'] = input_note[0]
    note['текст'] = input_note[1]
    note['дата'] = input_note[2]
    return note


def print_notes(allnotes: list):
    """
    Показывает все заметки в консоли
    """
    for note in allnotes:
        print(note)
