# Генератор фиктивных данных
Версия 1.0
## Описание
Данное приложение является реализацией python-task'а "Генератор фиктивных данных". Генерирует 11 типов данных: имя, фамилия, страна, город, дата рождения, возраст, почта, номер телефона (в международном формате), пароль, полный адрес, образование.
## Требования
* Python3
## Состав
* Консольная версия: generator.py
* Словари: dicts/
* Тесты: tests/
* Пример использования как пакета: example_lib.py 
## Структура
* Config file: config.py
* Person class: person.py
* Last launch params: /tests/last_launch.txt
* Birth dates from last generation (only from last console launch): /tests/dates.txt
## Консольная версия
Справка по запуску: ./generator.py -h/--help

Пример запуска: ./generator.py -c 100 -f file.txt -a 30 -d 5

(c) rZb.K 2018. Автор программы не несет никакой ответственности за генерируемые данные и их использование.
Программа является реализацией задания по курсу python task и не предназначена для использования в каких-либо мошеннических целях. Все совпадения случайны.
