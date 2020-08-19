# given a number from the user, output all of the factors of that number.

# first we need to get our user input, so lets prompt them to give us a number they would like to see the factors of

print('\nPlease input a number that you would like to see all of the factors of')

# While loop to make sure that the user inputs an INTEGER
while True:
    try:
        user_input = int(input('> '))
        break
    except ValueError:
        print('Invalid input, please input an Integer')

# lets initialize an empty list to house our factors of the number
factors = []

# we need a counter variable, lets initiate it at 1
counter = 1

# we need to loop through until our counter variable equals the number the user inputted above so (i.e. counter <= user_input or counter < user_input + 1)
while counter <= user_input:
    # initialize a boolean variable to see if the remainder of that counter var is 0
    # if it is 0 then we know its a factor
    is_remainder_zero = user_input % counter == 0
    if is_remainder_zero:
        factors.append(counter)
    counter += 1

# find the length of the list factors
length_of_list = len(factors)

# while loop to print out all of our factors from the list named factors
i = 0
while i < length_of_list:
    print(f'Factor {i + 1} for {user_input} is {factors[i]}')
    i += 1