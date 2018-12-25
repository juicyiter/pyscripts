#
#  exceptions_finally.py
#  ERROR
#
#  Created by jit on 21 October 2018.
#  Copyright © 2018 JuicyITer. All rights reserved. 
#

import sys
import time

f = None

try:
    f = open("example.py")

    while True:
        line = f.readline()

        if len(line) == 0:
            break

        print(line, end = ' ')

        sys.stdout.flush()
        # So that the print below will be printed
        # on the screen immediately

        print("Press Ctrl-c now")

        # To make sure it runs a while
        time.sleep(2)
except IOError:
    print("Could not find example.py")

except KeyboardInterrupt:
    print("!! You cancelled the reading from the file")

finally:
    if f:
        f.close()

    print("(Cleaning up: Closed the file!)")

    
