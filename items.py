#!/usr/bin/env python3
import csv


class Item:
    discount = 0.2
    pay_rate = 1-discount
    all = []

    def __init__(self,name:str,price:float,quantity = 0): 
        assert price >= 0 , f'Price {price} must be greater then zero!'
        assert quantity >= 0 , f'Price {quantity} must be greater then zero!'
        #Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity
        #Actions to execute
        Item.all.append(self)
        
    
    def calc_total_price(self):
        total_price = self.quantity * self.price
        return total_price


    def apply_discount(self):
        final_price = self.price * Item.pay_rate
        return final_price
    
    @classmethod
    def import_from_csv(cls):
        csv_file = open('items.csv','r')
        reader = csv.DictReader(csv_file)
        items = list(reader)
        for item in items:
            print(item)

    def __repr__(self):
        return f"Item('{self.name}',{self.price},{self.quantity})" #repr : representing your object 



#item1 = Item("Phone",1000,3)
#item2 = Item("Laptop",1500,3)
#item3 = Item("cable",100,5)
#item4 = Item("Mouse",50,5)
#item5 = Item("Keyboard",70,3)
Item.import_from_csv()
#print(item1.apply_discount())
#print(item1.calc_total_price())
#print(Item.pay_rate)
#print(item1.pay_rate)
#print(item1.__dict__) # will show the belonging atribute: {'name': 'Laptop', 'price': 1500, 'quantity': 3}


