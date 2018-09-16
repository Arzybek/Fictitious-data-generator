import json
import argparse
import random
import datetime
from config import needed, mails
from person import Person

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
    with open('./dicts/names.json', 'r', encoding='utf-8') as fh:
        names = json.load(fh)
    with open('./dicts/last_names.json', 'r', encoding='utf-8') as fh:
        last_names = json.load(fh)
    with open('./dicts/location.json', 'r', encoding='utf-8') as fh:
        locate = json.load(fh)
    with open('./dicts/codes.json', 'r', encoding='utf-8') as fh:
        codes = json.load(fh)


def get_name():
    ind = random.randrange(0, len(names) - 1, 1)
    name = names[ind]
    return name

def make_sub():
    length = random.randrange(1, 5)
    sub = ""
    for i in range(length):
        i = random.randrange(0, 10)
        sub = sub + str(i)
    return sub

def generate_password(name,last_name,date):
    words_file = "./dicts/words.txt"
    words = open(words_file).read().splitlines()
    choice = random.randrange(0,4)
    passwd = ""
    if(choice==0):
        index = random.randrange(0,len(words))
        passwd = words[index]
    elif(choice==1):
        index = random.randrange(0,len(words))
        sub = make_sub()
        passwd = words[index]+sub
    elif(choice==2):
        sub = make_sub()
        choose = random.randrange(0,2)
        if(choose==0):
            passwd = name + sub
        else:
            passwd = last_name + sub
    elif(choice==3):
        passwd = "{}{}{}".format(date.day,date.month,date.year)
    if(len(passwd)>4):
        return passwd
    else:
        index = random.randrange(0, len(words))
        passwd = passwd + words[index]
        return  passwd


def get_last_name():
    ind = random.randrange(0, len(last_names) - 1, 1)
    last_name = last_names[ind]
    return last_name


def get_location():
    ind_1 = random.sample(needed, 1)[0]
    iDict = codes[ind_1]
    country = iDict["name"]
    dial_code = iDict["dial_code"]
    cities = locate[country]
    city = cities[random.randrange(0, len(cities) - 1, 1)]
    return (country, city, dial_code)


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


def get_number(dial_code):
    iCode = random.randrange(10, 1000)
    iNum = random.randrange(1000000, 10000000)
    number = "{}-{}-{}".format(dial_code, iCode, iNum)
    return number


def random_date(start, end):
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = random.randrange(int_delta)
    return start + datetime.timedelta(seconds=random_second)


def create_person():
    name = get_name()
    last_name = get_last_name()
    location = get_location()
    mail = get_mail(name, last_name)
    number = get_number(location[2])
    now = datetime.datetime.today()
    end = datetime.datetime(now.year - 8, now.month, now.day)
    string_end = end.strftime("%d.%m.%Y")
    today = end.strptime(string_end, "%d.%m.%Y")
    start = datetime.datetime.strptime('1.1.1950', "%d.%m.%Y")
    date = random_date(start, today)
    passwd = generate_password(name,last_name,date)
    profile = Person(name, last_name, location, mail, number, date, passwd)
    return profile


if __name__ == "__main__":
    parser = createParser()
    namespace = parser.parse_args()
    file = namespace.file
    for i in range(
            namespace.count
    ):
        person = create_person()
        file.write(str(person))
        file.write("\n")
    file.close()