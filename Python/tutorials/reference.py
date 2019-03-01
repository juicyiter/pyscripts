##
# reference.py
#
#
# =================================================
# Written by JuicyITer on Friday,  7 September 2018.
# For more information, visit https://juicyiter.com
# =================================================
##

print('Simple Assignment')
shoplist = ['apple', 'orange', 'pear', 'banana']

mylist = shoplist
# mylist is just another name pointing to the same
# object

del shoplist[0]

print('Shoplist is', shoplist)
print('mylist is', mylist)

# The two list above are the same

# make a full copy
mylist = shoplist[:]

del mylist[0]

print('shoplist is', shoplist)
print('mylist is', mylist)
