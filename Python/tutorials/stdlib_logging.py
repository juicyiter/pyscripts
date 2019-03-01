#
#  stdlib_logging.py
#  Standard Library
#
#  Created by jit on 21 October 2018.
#  Copyright © 2018 JuicyITer. All rights reserved. 
#

import os
import platform
import logging

if platform.platform().startswith('Windows'):
    logging_file = os.path.join(os.getenv('HOMEDRIVE'),
                                os.getenv('HOMEPATH'),
                                'test.log')

else:
    logging_file = os.path.join(os.getenv('PWD'),
                                'test.log')

    
print('Logging to', logging_file)

logging.basicConfig(
    level = logging.DEBUG,
    format = '%(asctime)s : %(levelname)s : %(message)s',
    filename = logging_file,
    filemode = 'w',
    )

logging.debug("Start of the program")
logging.info("Doing something")
logging.warning("Dying now")
