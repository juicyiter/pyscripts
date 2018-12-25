def total(a = 5, *numbers, **phonebook):
    print("a", a)

    # iterate through all the items in tuple
    # All the positional arguments from the '*numbers' point till the end
    # are collected as a "tuple" called 'numbers'.
    for single_item in numbers:
        print("Single_item", single_item)


    # iterate through all the items in dictionary
    # All keyword arguments from that point till the end
    # are collected as a "dictionary" called 'phonebook'

    for first_part, second_part in phonebook.items():
        print(first_part, second_part)


print( total(10, 1, 2, 3, Jack = 1123, John = 2231, Inge = 1643) )

# *numbers is like an "array" in C, and **phonebook is like a "structure" in C?
