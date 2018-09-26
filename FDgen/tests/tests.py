import unittest
import sys
import os
import  json
from config import  ROOT_DIR
sys.path.append('..\..')
import FDgen
import datetime


class SimpleTestCase(unittest.TestCase):
    def test_mails(self):
        mail = FDgen.get_mail("arzybek", "kazikulov")
        self.assertRegex(mail, "[a-z]\.?[a-z]@[a-z].[a-z]")

    def test_nums(self):
        num = FDgen.get_number("+228")
        self.assertRegex(num, "\+\d{1,4}-\d{2,3}-\d{7}")

    def test_name(self):
        name = FDgen.get_name()
        flag = False
        for i in range(len(FDgen.names)):
            if FDgen.names[i] == name:
                flag = True
        self.assertEqual(flag, True)

    def test_last_name(self):
        last_name = FDgen.get_last_name()
        flag = False
        for i in range(len(FDgen.last_names)):
            if FDgen.last_names[i] == last_name:
                flag = True
        self.assertEqual(flag, True)

    def test_person(self):
        person = FDgen.create_person()
        self.assertRegex(person.name, '^[A-Z][a-z]+')
        self.assertRegex(person.last_name, '^[A-Z][a-z]+')
        self.assertRegex(person.strDate, '\d{2}\.\d{2}\.\d{4}')
        self.assertRegex(str(person.age), '\d+')
        self.assertRegex(person.country, '^[A-Z][a-z]+')
        self.assertRegex(person.city, '^[A-Z][a-z]+')

    def test_password(self):
        birth = datetime.datetime(2000, 1, 8)
        password = FDgen.generate_password("arzybek", "kazikulov", birth)
        self.assertTrue(len(password) > 4)

    def test_address(self):
        street = FDgen.get_address()
        self.assertRegex(street,"[\w\s]+, [\d]+")

    def test_education(self):
        person = FDgen.create_person()
        edu = person.education
        age = person.age
        flag = False
        pEds = os.path.join(ROOT_DIR, 'dicts/educations.json')
        with open(pEds, 'r', encoding='utf-8') as fh:
            educations = json.load(fh)
        for key, value in educations.items():
            ranges = key.split(" ")
            if(age > int(ranges[0]) and age <= int(ranges[1])):
                if(edu in value):
                    flag = True
        self.assertTrue(flag)