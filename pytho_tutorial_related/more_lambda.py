#
#  more_lambda.py
#  MORE
#
#  Created by jit on 21 October 2018.
#  Copyright © 2018 JuicyITer. All rights reserved. 
#

points = [{'x' : 2, 'y' : 3},
          {'y' : 1, 'x' : 4}]

points.sort(key = lambda i: i['x']) # based on the value of 'x'

print(points)
