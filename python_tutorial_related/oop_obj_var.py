#
#  oop_obj_var.py
#  OOP
#
#  Created by jit on 21 October 2018.
#  Copyright © 2018 JuicyITer. All rights reserved. 
#


class Robot:
    """Represents a robot, with a name."""


    # A class variable, counting numbers of robots
    population = 0
    
    def __init__(self, name):
        """Initialize the data"""
        self.name = name
        # The name variable belongs to the object 'self'
        # It's an object variable
        # If the object variable has the same name as the class
        # variabe, the latter will be hided.
        print("Initializing {}".format(self.name))


        # When this person is created, the robot
        # adds to the population
        Robot.population += 1
        # Which is equal to 'self.__class__.population += 1'
        
    def die(self):

        """I am dying."""
        print("{} is being destoryed.".format(self.name))

        Robot.population -= 1

        if Robot.population == 0:
            print("{} is the last one.".format(self.name))

        else:

            print("There are stil {:d} robots working.".format(Robot.population))

    def say_hi(self):
         """Greeting by the robot.


Yeah, they can do that."""
         print("Greeting, my masters call me {}.".format(self.name))


    @classmethod
    # This specifies that the method 'how_many' is class method
    # This is a decorator
    def how_many(cls):
        """Prints current population"""

        print("We have {:d} robots.".format(cls.population))

        
droid1 = Robot("R2_D2")
droid1.say_hi()
Robot.how_many()


droid2 = Robot("R1_D1")
droid2.say_hi()
Robot.how_many()

print("\nRobots can do some work here\n")

print("Work is done, let's destory them")

droid1.die()
droid2.die()

Robot.how_many()
