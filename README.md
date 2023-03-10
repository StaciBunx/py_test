# Промежуточная аттестация - приложение Заметки

## Информация о проекте
Необходимо написать проект, содержащий функционал работы с заметками. Программа должна уметь создавать заметку, сохранять её, читать список заметок, редактировать заметку, удалять заметку.

## Задание
- Реализовать консольное приложение заметки, с сохранением, чтением, добавлением, редактированием и удалением заметок.
- Заметка должна содержать идентификатор, заголовок, тело заметки и дату/время создания или последнего изменения заметки.
- Сохранение заметок необходимо сделать
в формате json или csv формат (разделение полей рекомендуется делать через точку с запятой).
- Реализацию пользовательского интерфейса студент может
делать как ему удобнее, можно делать как параметры запуска программы (команда, данные), можно делать как запрос команды с консоли и последующим вводом данных, как-то ещё, на усмотрение студента.
- При чтении списка заметок реализовать фильтрацию по дате.

## Критерии оценки
Приложение должно запускаться без ошибок, должно уметь сохранять данные в файл, уметь читать данные из файла, делать выборку по дате, выводить на экран выбранную запись, выводить на экран весь список записок, добавлять записку, редактировать ее и удалять.

# Описание приложения Notes (Заметки)

## Функционал
- Сохранять новую заметку в файл (cvs)
- Показывать все заметки из файла в консоли
- Показывать заметки только определенной даты (фильтр)
- Выводить на экран запись по поиску
- Редактировать заметку
- Удалять заметку

### main.py
Запуск программы

### controller.py
Взаимодействие между модулями

### ui.py
Реализация user interface в консоли: меню, приветствие/прощание, статусы и прочее

### operations.py
Операция с файлом cvo

### note_operations.py
Создание словаря заметки с дальнейшей записью в файл csv

### log.py
Логирование

### check.py
Проверка на ввод пустой строки и на правильность выбора в меню приложения
