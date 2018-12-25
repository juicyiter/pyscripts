number = 23
# get input
guess = int(input("Enter an integer:"))

while guess != number:
    if guess > number:
        print("Sorry, your guessed number was to large.")

    elif guess < number :
        print("Soryy, your guessed number was to small.")
    guess = int(input("Enter an integer again:"))
print("Congratulations, you guessed it!")

