##
# dictionary.py
# Associate keys with values.
# Keys must be unique and immutable.
# Values can be immutable and mutable.
#
# =================================================
# Written by JuicyITer on Wednesday, 22 August 2018.
# For more information, visit https://juicyiter.com
# =================================================
##

ab = {
    # This is an address book.
    "JuicyITer" : "home@juicyiter.com",
    "Swaropp" : "swaroop@swaroop.com",
    "Larry" : "larry@wan.org",
    "Spammer" : "spammer@hotmail.com"
}

print("JuicyITer's address is", ab["JuicyITer"], end = ".\n")

# Deleting a key-value pair
del ab["Spammer"]

print("There are {} contacts in the address book\n".format(len(ab)))

for name, address in ab.items():
    print("Contact {} at {}".format(name, address), end = ".\n")

# Adding a key-value pair
ab["Guido"] = "guido@python.org"

if "Guido" in ab:
    print("Guido's address is", ab["Guido"])

    for name, address in ab.items():
        print("Contact {} at {}".format(name, address), end = ".\n")

    # Adding a key-value pair
    ab["Guido"] = "guido@python.org"

    if "Guido" in ab:
        print("Guido's address is", ab["Guido"], end = ".\n")
