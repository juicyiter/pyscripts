##
# set.py
#
#
# =================================================
# Written by JuicyITer on Friday,  7 September 2018.
# For more information, visit https://juicyiter.com
# =================================================
##

bri = set(["apple", "banana", "orange"])

print("apple" in bri)

print("me" in bri)

bric = bri.copy()

bric.add("pear")

print(bric.issuperset(bri))
# bric now contains bri

bri.remove("apple")

print(bri & bric) # OR bri.intersection(bric)
