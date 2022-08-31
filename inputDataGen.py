from faker import Faker
import random


class InputFieldGenerator:
    fkr = Faker('en_US')

    def get_rdn_num(self, lBorder, uBorder):
        return str(random.randint(lBorder, uBorder))

    def get_full_name(self):
        full_name = self.fkr.name().split()

        if len(full_name) > 2:
            self.GetName()
        else:
            return full_name

    def get_email(self):
        return self.fkr.email()

    def get_city(self):
        return self.fkr.city()

    def get_state(self):
        return self.fkr.state()

    def get_zip(self):
        return self.get_rdn_num(10000, 99999)

    def get_phone(self):
        return "+370" + self.get_rdn_num(10000000, 99999999)

    def get_text(self):
        return self.fkr.text()