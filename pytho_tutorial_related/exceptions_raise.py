#
#  exceptions_raise.py
#  ERROR
#
#  Created by jit on 21 October 2018.
#  Copyright © 2018 JuicyITer. All rights reserved. 
#

class shortInputException(Exception):
    def __init__(self, length, atLeast):
        Exception.__init__(self)

        self.length = length
        self.atLeast = atLeast

    
try:
    text = input("Enter something -->")
    if(len(text) < 3):
        raise shortInputException(len(text), 3)

except shortInputException as ex:
    print("shortInputException: The input was" +
          " {0} long, expected at least {1}.".format(ex.length, ex.atLeast))

except EOFError:
    print("Why did you put an EOF on me?")

else:
    print("No exception was raised.")
    
