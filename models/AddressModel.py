from random import randint, choice

class Address():

    def __init__(self):

        address_road = ['Walker Street', 'The Square', 'Regent Street', 'Croft Lane', 
                        'Church Avenue', 'Alma Road', 'South Drive', 'Eastgate']
        address_city_and_zip = [('Viroinval',5670), ('Meise',1860), ('Oudenaarde',9700), 
                                ('Jodoigne',1370), ('Wanze',4520), ('Momignies',6592), 
                                ('Brussels',1000), ('Antwerpen',2060), ('Beerse', 2340)]

        self.street = choice(address_road)
        self.number = randint(1, 99)
        self.address_city_and_zip = choice(address_city_and_zip)
        self.zipcode = self.address_city_and_zip[1]
        self.city = self.address_city_and_zip[0]

    def datas(self):
        return {'street' : self.street, 
                'number' : self.number, 
                'zipcode' : self.zipcode, 
                'city' : self.city}