import datetime


class Person:
    def __init__(self, name, ln, location, mail, num, bd, passwd):
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

    def calc_age(self):
        today = datetime.datetime.today()
        self.age = today.year - self.birth_date.year - (
                    (today.month, today.day) < (self.birth_date.month, self.birth_date.day))

    def __str__(self):
        strRepr = "Name:           {}\n" \
                  "Last name:      {}\n" \
                  "Birth date:     {}\n" \
                  "Age:            {}\n" \
                  "Country:        {}\n" \
                  "City:           {}\n" \
                  "Number:         {}\n" \
                  "E-mail:         {}\n" \
                  "Password:       {}\n".\
            format(self.name, self.last_name, self.strDate, self.age, self.country, self.city, self.number, self.mail, self.password)
        return strRepr
