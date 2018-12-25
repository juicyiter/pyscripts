#
#  oop_init.py
#  OOP
#
#  Created by jit on 21 October 2018.
#  Copyright © 2018 JuicyITer. All rights reserved. 
#

class Person():
    def __init__(self, name):
        self.name = name

    def say_hi(self):
        print("Hello, my name is", self.name)


p = Person("Ethan")
p.say_hi()

