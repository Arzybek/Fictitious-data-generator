import json
import argparse
import random
import time
import datetime

load = False


def createParser():
    parser = argparse.ArgumentParser(
        description='Генератор фиктивных данных.',
        epilog='(c) rZb.K 2018. Автор программы не несет никакой ответственности за генерируемые данные '
               'и их использование. Все совпадения случайны.'
    )
    parser.add_argument('-c', '--count', type=int, required=True, help='Количество генерируемых данных (in Persons)')
    parser.add_argument('-f', '--file', type=argparse.FileType(mode='a'),
                        required=True, help='Файл для записи данных. Создает новый, если указанного не существует, '
                                            'дозаписывает в конец файла')
    parser.add_argument('-a', '--average', type=int, help='Средний возраст')
    return parser


if (not load):
    load = True
    with open('names.json', 'r', encoding='utf-8') as fh:
        names = json.load(fh)
    with open('last_names.json', 'r', encoding='utf-8') as fh:
        last_names = json.load(fh)
    with open('location.json', 'r', encoding='utf-8') as fh:
        locate = json.load(fh)
    with open('mails.json', 'r', encoding='utf-8') as fh:
        mails = json.load(fh)


def get_name():
    ind = random.randrange(0, len(names) - 1, 1)
    name = names[ind]
    return name


def get_last_name():
    ind = random.randrange(0, len(last_names) - 1, 1)
    last_name = last_names[ind]
    return last_name


def get_location():
    ind_1 = random.randrange(0, len(locate) - 1, 1)
    keys = list(locate.keys())
    key = keys[ind_1]
    ind_2 = random.randrange(0, len(locate[key]) - 1, 1)
    return (key, locate[key][ind_2])


def get_mail(name, last_name):
    name = name.lower()
    last_name = last_name.lower()
    mail = random.randrange(0, len(mails) - 1)
    mail = mails[mail]
    pick = random.randint(0, 1)
    if (pick == 0):
        mail = "{}.{}{}".format(name, last_name, mail)
    else:
        mail = "{}{}".format(last_name, mail)
    return mail


def get_number():
    return random.randrange(70000000000, 80000000000)

def random_date(start, end):
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = random.randrange(int_delta)
    return start + datetime.timedelta(seconds=random_second)


def calc_age(born):
    today = datetime.datetime.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))

if __name__ == "__main__":
    parser = createParser()
    namespace = parser.parse_args()
    file = namespace.file
    for i in range(
            namespace.count
    ):
        name = get_name()
        last_name = get_last_name()
        location = get_location()
        mail = get_mail(name, last_name)
        number = '+{}'.format(get_number())
        now = datetime.datetime.today()
        end = datetime.datetime(now.year-8,now.month,now.day)
        string_end = end.strftime("%d.%m.%Y")
        today = end.strptime(string_end,"%d.%m.%Y")
        start = datetime.datetime.strptime('1.1.1950',"%d.%m.%Y")
        date = random_date(start,today)
        string_date = date.strftime("%d.%m.%Y")
        age = calc_age(date)
        file.write("Name:           {}\n"
                   "Last name:      {}\n"
                   "Birth date:     {}\n"
                   "Age:            {}\n"
                   "Country:        {}\n"
                   "City:           {}\n"
                   "E-mail:         {}\n"
                   "Number:         {}\n".
                   format(name,last_name,string_date,age,location[0],location[1],mail,number))
        file.write("\n")
    file.close()