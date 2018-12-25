##
# sequence.py
# Lists, tuples and strings are examples of sequence
# The major features are 'memberships test'(in and not in)
# and indexing operations, which allow us to fetch
# a particular item in the sequence directly
#
# =================================================
# Written by JuicyITer on Friday, 24 August 2018.
# For more information, visit https://juicyiter.com
# =================================================
##

shoplist = ["apple", "orange", "carrot", "banana"]

name = "swaroop"

# Indexing or "subscription" operation

i = 0;
while i<len(shoplist):
    print("Item {} is".format(i), shoplist[i], end = '.\n')
    i = i+1
print("Item -1 is", shoplist[-1], end = ".\n")
print("Item -2 is", shoplist[-2], end = ".\n")
# according from the output, it's more like a 'loop' #

print("Character 0 is", name[0], end = ".\n")

# Slicing on a list #
# Not including the latter #
# The start and end are '' #
print("Item 1 to 3 is", shoplist[1:3], end = ".\n")
print("Item 2 to end is", shoplist[2:], end = ".\n")
print("Item 1 to -1 is", shoplist[1:-1], end = ".\n")
print("Item start to end is", shoplist[:], end = ".\n")

# Slicing on a string #
print("Character 1 to 3 is", name[1:3], end = ".\n")
print("Character 2 to end is", name[2:], end = ".\n")
print("Character 1 to -1 is", name[1:-1], end = ".\n")
print("Character start to end is", name[:], end = ".\n")

# Slicing with steps #
print(shoplist[0::2])
# Let's reverse the list #
print(shoplist[::-1])
