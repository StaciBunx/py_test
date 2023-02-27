def write_note(input_note: list) -> dict:
    note = {}
    note['заголовок'] = input_note[0]
    note['текст'] = input_note[1]
    note['дата'] = input_note[2]
    return note
