from random import random, choice

class Person():

    def __init__(self, b_female, address):

        first_name_f = ['Olivia', 'Emma', 'Mila', 'Louise', 'Alice', 
                            'Lina', 'Juliette', 'Anna', 'Elena', 'Lucie']
        first_name_m = ['Arthur', 'Liam', 'Louis', 'Jules', 'Lucas', 
                            'Victor', 'Gabriel', 'Jean', 'Mark', 'Stefen']
        last_name = ['Mitchell', 'Wilkins', 'Lane', 'Moegi', 'Derlin',
                            'Thurio', 'Hotah', 'Grievous', 'Holmes', 'Potter']
        
        if b_female :
            first_name = first_name_f
        else :
            first_name = first_name_m

        self.b_female = b_female        
        self.first_name = choice(first_name)
        self.last_name = choice(last_name)
        self.address = address
        # self.birthdate = birthdate
        # self.email = email
        # self.phone = phone
        # self.natnum = natnum


    def datas(self):
        return {'Identity' : {'be_female' : self.b_female, 'first_name' : self.first_name, 
                'last_name' : self.last_name, 'address' : self.address},
                'Description' : None}

