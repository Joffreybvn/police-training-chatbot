from models.AddressModel import *
from models.PersonModel import *


def generate_address():
    address = Address()
    return address.datas()


def generate_person(b_female):
    person = Person(b_female, generate_address())
    return person.datas()
