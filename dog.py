#!/usr/bin/env python3

class Dog:
    def __init__(self,name='',age=0,sex=''):
        self.name = name
        self.age = age
        self.sex = sex
        self.hungry_status = True
    def sleep(self):
        self.hungry_status = False
        print('doggy go sleep now')
    def sound(self):
        return 'awuuuuuuuuu'
    def up(self):
        self.hungry_status = True
        print('doggy is up now')
    def hungry(self):
        if self.hungry_status:
            return f'the hunger status is {self.hungry_status}'
        else:
            return f'the hunger status is {self.hungry_status}'


Lassy = Dog('Lassy', 2, 'f')

print(Lassy.sound())
Lassy.sleep()
Lassy.up()
print(Lassy.hungry())