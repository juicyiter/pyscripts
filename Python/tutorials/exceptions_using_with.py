#
#  exceptions_using_with.py
#  IO
#
#  Created by jit on 21 October 2018.
#  Copyright © 2018 JuicyITer. All rights reserved. 
#

# Leaving the closing of the file to be done
# automatically by 'with' statement

with open("example.py") as f:
    for line in f:
        print(line, end = '')

# Behind the scenes

# There is a protocol used by the 'with' statement
# It fetches the file returned by 'open' statement
# It always calls the 'thefile.__enter__ function
# before entering the block of code under it
# and always calls the 'thefile.__exit__ function
# after finishing the block of code.
