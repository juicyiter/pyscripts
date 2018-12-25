def say(message, time = 3):
    print(message * time)

say("hello")

say(3) # if message is a number, then it prints the product  

say("hello", 4)

## Note: only those paremeters which are at the end of the
## paremeter list can be set to default.
## For example: say(message = 1, time) is not valid.
