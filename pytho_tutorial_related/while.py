number = 23

# modified while loop related to if.py
running = True

while running:
    guess = int(input("Enter an integer:"))

    if guess == number:
        print("Congratulations, you guessed it!")

        # change running state
        running = False
    elif guess > number:
        print("Sorry, your guessed number was too large.")

    else :
        print("Sorry, your guessed number was too small.")
