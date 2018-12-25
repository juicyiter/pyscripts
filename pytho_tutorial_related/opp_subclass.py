#
#  opp_subclass.py
#  OOP
#
#  Created by jit on 21 October 2018.
#  Copyright © 2018 JuicyITer. All rights reserved. 
#

class schoolMember:
    """ Superclass, representing a school member. """
    def __init__(self, name, age):
        self.name = name;
        self.age = age;

        print("(Initialized a school member: {})".format(self.name));

    """Member details"""
    def tell(self):
        print("Name: \"{}\" Age: \"{}\"".format(self.name, self.age), end = ' ');

        
class teacher(schoolMember):
    """ Subclass, representing a teacher. """
    def __init__(self, name, age, salary):
        schoolMember.__init__(self, name, age);

        self.salary =  salary;

        print("(Initialized a teacher: {})".format(self.name));

    """ Teacher details """
    def tell(self):
        schoolMember.tell(self);

        print("Salary: \"{:d}\"".format(self.salary));

class student(schoolMember):
    """ Subclass, representing a student """
    def __init__(self, name, age, marks):
        schoolMember.__init__(self, name, age);

        self.marks = marks;

        print("(Initialized a student: {})".format(self.name));

    """ Student details """
    def tell(self):
        schoolMember.tell(self);

        print("Marks: \"{:d}\"".format(self.marks));

t = teacher("Mrs. Shrividya", 40, 30000);
s = student("Ethan", 22, 75);

print()

members = [t, s]

for member in members:
    member.tell()
