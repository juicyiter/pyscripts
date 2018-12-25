#! /usr/local/bin/python3
# File:    more_decorations.py
# Author:  JuicyITer <contactme@juicyiter.com>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Library General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA 02111-1307, USA.
# Copyright 2005 Duke University

# History:
## =====================
# 2018-10-22 12:35 JuicyITer <contactme@juicyiter.com> created.
## =====================


from time import sleep
from functools import wraps
import logging

logging.basicConfig()
log = logging.getLogger("retry")

# Define a decorator
def retry(f):
    @wraps(f)
    # Delcare a inner function in it
    def wrapper_function(*args, **kwargs):
        MAX_ATTEMPTS = 5
        for attemp in range(1, MAX_ATTEMPTS + 1):
            try:
                # If no exceptions were raised, retry
                f(*args, **kwargs)

            except Exception:
                log.exception("Attemp %s/%s failed : %s",
                              attemp,
                              MAX_ATTEMPTS,
                              (args, kwargs))
                sleep(1 * attemp)

        # All attemp failed
        log.critical("All %s attempts failed : %s",
                     MAX_ATTEMPTS,
                     (args, kwargs))
    # return the inner function
    return wrapper_function

counter = 0

# 'Under' the decorator
@retry
# which is equal to save_to_database = retry(save_to_database)
def save_to_database(arg):
    print("Write to a database or make a network call or etc.")
    print("This will be automatically retried if exception is thrown.")

    global counter
    counter += 1

    # This will throw an exception in the first call
    # And will work fine until in the forth call (i.e. a retry)
    if counter < 7:
        raise ValueError(arg)


if __name__ == '__main__':
    f = save_to_database("Some bad value")
    print(f.__name__)
