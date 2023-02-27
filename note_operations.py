def write_note(input_note: list) -> dict:
    note = {}
    note['идентификатор'] = input_note[0]
    note['заголовок'] = input_note[1]
    note['текст'] = input_note[2]
    note['дата'] = input_note[3]
    return note
