while True:
    try:
        x = int(input('Enter a number:'))
        print(f'The number you entered is {x}')
        break
    except ValueError:
        print('Oops, seems you entered a invalid number! Please try again.')
