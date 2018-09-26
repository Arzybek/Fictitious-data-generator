import json
import argparse
import random
import datetime
from config import needed, mails, avg_age, dispersion, ROOT_DIR, max_avg_age, max_disp
from person import Person
import math
import os

load = False

log_file = ""


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
    parser.add_argument('-a', '--average', type=int, help='Средний возраст', required=True)
    parser.add_argument('-d', '--dispersion', type=int, help='Разброс возраста', required=False)
    return parser


def _reopen_log_file():
    global log_file
    pLog = os.path.join(ROOT_DIR, 'tests/dates.txt')
    reopen = open(pLog, "w")
    reopen.close()
    log_file = open(pLog, "a")


if (not load):
    load = True
    pNames = os.path.join(ROOT_DIR, 'dicts/names.json')
    pLast_names = os.path.join(ROOT_DIR, 'dicts/last_names.json')
    pLocation = os.path.join(ROOT_DIR, 'dicts/location.json')
    pCodes = os.path.join(ROOT_DIR, 'dicts/codes.json')
    pWords = os.path.join(ROOT_DIR, 'dicts/words.txt')
    pStreets = os.path.join(ROOT_DIR, 'dicts/streets.txt')
    with open(pNames, 'r', encoding='utf-8') as fh:
        names = json.load(fh)
    with open(pLast_names, 'r', encoding='utf-8') as fh:
        last_names = json.load(fh)
    with open(pLocation, 'r', encoding='utf-8') as fh:
        locate = json.load(fh)
    with open(pCodes, 'r', encoding='utf-8') as fh:
        codes = json.load(fh)
    with open(pWords, 'r', encoding='utf-8') as fh:
        words = fh.read().splitlines()
    with open(pStreets, 'r', encoding='utf-8') as fh:
        streets = fh.read().splitlines()
    _reopen_log_file()


def get_name():
    ind = random.randrange(0, len(names), 1)
    name = names[ind]
    return name


def get_address():
    ind = random.randrange(0, len(streets))
    street = streets[ind]
    rnd_choice = random.random()
    if (rnd_choice >= 0.7 and rnd_choice < 0.8):
        street = street + " Lane"
    elif (rnd_choice >= 0.8 and rnd_choice <= 0.9):
        street = street + " Avenue"
    elif (rnd_choice > 0.9):
        street = street + " Road"
    elif (rnd_choice >= 0.6 and rnd_choice < 0.7):
        street = street + " Drive"
    else:
        street = street + " St"
    rnd_num = random.random()
    num_house = 0
    if (rnd_num <= 0.5):
        num_house = random.randrange(1, 51)
    elif (rnd_num > 0.5 and rnd_num <= 0.8):
        num_house = random.randrange(100, 171)
    else:
        num_house = random.randrange(500, 601)
    street = street + ", {}".format(num_house)
    return street


def _make_sub():
    length = random.randrange(1, 5)
    sub = ""
    for i in range(length):
        i = random.randrange(0, 10)
        sub = sub + str(i)
    return sub


def generate_password(name, last_name, date):
    choice = random.randrange(0, 4)
    passwd = ""
    if (choice == 0):
        index = random.randrange(0, len(words))
        passwd = words[index]
    elif (choice == 1):
        index = random.randrange(0, len(words))
        sub = _make_sub()
        passwd = words[index] + sub
    elif (choice == 2):
        sub = _make_sub()
        choose = random.randrange(0, 2)
        if (choose == 0):
            passwd = name + sub
        else:
            passwd = last_name + sub
    elif (choice == 3):
        letter = name[0].upper()
        passwd = "{}{}{}{}".format(date.day, date.month, date.year, letter)
    if (len(passwd) > 4):
        return passwd
    else:
        index = random.randrange(0, len(words))
        passwd = passwd + words[index]
        return passwd


def get_last_name():
    ind = random.randrange(0, len(last_names), 1)
    last_name = last_names[ind]
    return last_name


def get_location():
    ind_1 = random.sample(needed, 1)[0]
    iDict = codes[ind_1]
    country = iDict["name"]
    dial_code = iDict["dial_code"]
    cities = locate[country]
    city = cities[random.randrange(0, len(cities), 1)]
    return (country, city, dial_code)


def get_mail(name, last_name):
    name = name.lower()
    last_name = last_name.lower()
    mail = random.randrange(0, len(mails))
    mail = mails[mail]
    pick = random.randint(0, 1)
    if (pick == 0):
        mail = "{}.{}{}".format(name, last_name, mail)
    else:
        mail = "{}{}".format(last_name, mail)
    return mail


def get_number(dial_code):
    iCode = random.randrange(10, 1000)
    iNum = random.randrange(1000000, 10000000)
    number = "{}-{}-{}".format(dial_code, iCode, iNum)
    return number


def get_avg_age(age, disp):
    age = int(random.gauss(age, disp))
    age = int(math.fabs(age))
    log_file.writelines(str(age) + "\n")
    return age


def create_person():
    name = get_name()
    last_name = get_last_name()
    location = get_location()
    mail = get_mail(name, last_name)
    number = get_number(location[2])

    if (avg_age > max_avg_age):
        print("Age is too big")
        raise ValueError
    if (dispersion > avg_age or dispersion >= max_disp):
        print("Dispersion is bigger than average age")
        raise ValueError

    age = get_avg_age(avg_age, dispersion)
    now = datetime.datetime.today()
    year_date = datetime.datetime(now.year - age, 1, 1)
    count_seconds_in_year = 365 * 24 * 60 * 60
    delta_sec = random.randrange(count_seconds_in_year)
    birth_date = year_date + datetime.timedelta(seconds=delta_sec)

    passwd = generate_password(name, last_name, birth_date)
    adress = get_address()
    profile = Person(name, last_name, location, mail, number, birth_date, passwd, adress)
    return profile


if __name__ == "__main__":
    parser = createParser()
    namespace = parser.parse_args()
    file = namespace.file
    avg_age = namespace.average
    if (namespace.dispersion):
        dispersion = namespace.dispersion
    pLastLaunch = os.path.join(ROOT_DIR, 'tests/last_launch.txt')
    log_launch = open(pLastLaunch, 'w')
    log_launch.writelines([str(avg_age), '\n', str(dispersion)])
    log_launch.close()
    for i in range(
            namespace.count
    ):
        person = create_person()
        file.write(str(person))
        file.write("\n")
    file.close()
    log_file.close()
