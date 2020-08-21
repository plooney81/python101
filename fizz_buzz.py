# give a number from user, count all the numbers and replace them if they are divisible by 3 or 5 and then another word if it is divisible by both

print("Give me a number!")
while True:
    try:
        user_input = int(input('> '))
        break
    except ValueError:
        print('Try again')

counter = 1
while counter <= user_input :
    if counter % 3 == 0 and counter % 5 == 0:
            print("fizzbuzz")
    elif counter % 3 == 0:
            print("fizz")
    elif counter % 5 == 0:
            print("buzz")
    else:
        print(counter)
    counter += 1