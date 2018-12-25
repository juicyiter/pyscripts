# for loop

for i in range(1,10): # include 1 and exclude 10
    print(i)

else: # Note the difference
    print("The for loop is over.")

# By default, range takes a step count of 1.
# If a third number is included to range,
# then it becomes the step count

for i in range(1,10,3): # step count is 3
    print(i)

print("The for loop is over without else.")

# range in a list

for i in list(range(10)):
    print(i)

## Question: how to change count type in list?

for i in list(range(1,10,3)): # is it tedious?
    print(i)