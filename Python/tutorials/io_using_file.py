#
#  io_using_file.py
#  IO
#
#  Created by jit on 21 October 2018.
#  Copyright © 2018 JuicyITer. All rights reserved. 
#

poem = '''\
Programming is fun
When the work is done
if you wanna make your work also fun:
    use Python!
'''

f = open("poem.txt", "w")

f.write(poem)

f.close()


f = open("poem.txt")
while True:
    line = f.readline()

    if len(line) == 0:
        break

    print(line, end = ' ')


f.close()
