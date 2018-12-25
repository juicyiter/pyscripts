#
#  io_pickle.py
#  IO
#
#  Created by jit on 21 October 2018.
#  Copyright © 2018 JuicyITer. All rights reserved. 
#

import pickle

shoplistFile = 'shoplist.data'

shoplist = ['apple', 'mango', 'carrot']

f = open(shoplistFile, 'wb')

pickle.dump(shoplist,f)

f.close()

del shoplist

f = open(shoplistFile, 'rb')

storedList = pickle.load(f)

print(storedList)

f.close()

