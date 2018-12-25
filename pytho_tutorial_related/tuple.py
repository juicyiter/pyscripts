##
 # tuple.py
 # Tuple is like list, but without functionality.
 # You cannot modify tuple like the list.
 # They are immutable like string.
 #
 # Using parentheses to indicate start
 # and end of the tuple.
 # Even though the parentheses are optional.
 # Explicit is better than implicit!
 #
 # =================================================
 # Written by JuicyITer on Wednesday, 22 August 2018.
 # For more information, visit https://juicyiter.com
 # =================================================
 ##

zoo = ("python", "elephant", "penguin")
print("Number of animals in the zoo is", len(zoo), end = ".\n")

new_zoo = "moneky", "camel", zoo     # Parentheses not required but not recommended.
# Append the old zoo to the new zoo
print("Number of cages in the new zoo is", len(new_zoo), end = ".\n")

print("All animal in new zoo are", new_zoo, end = ".\n")
print("Animals brought from old zoo are", new_zoo[2], end = ".\n")
print("Last animal brought from old zoo is", new_zoo[2][2], end = ".\n")
print("Number of animals in the new zoo is", len(new_zoo) - 1 + len(new_zoo[2]), end = ".\n")

# Tuple with 0 or 1 items

myempty = ()
# You have to specify it using a comma following the first
# (and only) item so that Python can
# differentiate between a tuple and
# a pair of parentheses surrounding the object in an expression.
singleton = (2, )
