from datetime import datetime as dt

def log(operation, result):
    '''
    Записывает время, операцию и результат
    '''
    time = dt.now().strftime('%d.%m.%Y - %H:%M')
    with open('log.txt', 'a', encoding = 'UTF-8') as file:
        file.write(f'{time}: \t{operation}: \t {result}\n')