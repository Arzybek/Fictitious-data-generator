import datetime
import random
import os
import json
from config import ROOT_DIR


class Person:
    def __init__(self, name, ln, location, mail, num, bd, passwd, address):
        self.name = name
        self.last_name = ln
        self.country = location[0]
        self.city = location[1]
        self.mail = mail
        self.number = num
        self.birth_date = bd
        self.strDate = self.birth_date.strftime("%d.%m.%Y")
        self.password = passwd
        self.calc_age()
        self.address = address
        self.calc_education()

    def calc_age(self):
        today = datetime.datetime.today()
        self.age = today.year - self.birth_date.year - (
                (today.month, today.day) < (self.birth_date.month, self.birth_date.day))

    def calc_education(self):
        pEds = os.path.join(ROOT_DIR, 'dicts/educations.json')
        with open(pEds, 'r', encoding='utf-8') as fh:
            educations = json.load(fh)
        for key, value in educations.items():
            ranges = key.split(" ")
            if (self.age > int(ranges[0]) and self.age <= int(ranges[1])):
                choice = random.choice(value)
                if(choice=="-"):
                    choice = random.choice(value)
                self.education = choice
                break

    def __str__(self):
        strRepr = "Name:           {}\n" \
                  "Last name:      {}\n" \
                  "Birth date:     {}\n" \
                  "Age:            {}\n" \
                  "Country:        {}\n" \
                  "City:           {}\n" \
                  "Number:         {}\n" \
                  "E-mail:         {}\n" \
                  "Password:       {}\n" \
                  "Address:        {}\n" \
                  "Education:      {}\n". \
            format(self.name, self.last_name, self.strDate, self.age, self.country, self.city, self.number, self.mail,
                   self.password, self.address, self.education)
        return strRepr
