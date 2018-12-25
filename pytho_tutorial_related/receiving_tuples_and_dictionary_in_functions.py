#
#  receiving_tuples_and_dictionary_in_functions.py
#  MORE
#
#  Created by jit on 22 October 2018.
#  Copyright © 2018 JuicyITer. All rights reserved. 
#

# '*' prefix on the args var, all the arguments passed to the function
# are stored in the args as tuple
# '**' prefix on the args var, all the arguments passed to the funciton
# will be stored in the args as dictionary

def powersum(power, *args):
    '''Return the sum of the each arguments raised to the specified power'''
    total = 0
    for i in args:
        total += pow(i, power)

    return total

print(powersum(2, 3, 4))

print(powersum(2, 10))
