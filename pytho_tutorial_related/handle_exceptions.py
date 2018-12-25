#
#  handle_exceptions.py
#  IO
#
#  Created by jit on 21 October 2018.
#  Copyright © 2018 JuicyITer. All rights reserved. 
#

try:
    text = input("Enter some string -->")

except EOFError:
    print("Why did you put an EOF on me?")

except KeyboardInterrupt:
    print("You cancelled the operation.")

else:
    print("You entered {}".format(text))
    
