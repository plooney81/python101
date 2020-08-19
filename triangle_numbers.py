# Print the first 100 triangle numbers
# xn means dots in triangle number n
# triangle number equation is:
#       xn = n (n + 1) / 2

# we want the first 100 triangle numbers, but lets make it to where the program outputs the x number of triangle numbers, where x is a user inputted number.

# prompt the user for how many triangle numbers they would like to see printed out.
print('\nPlease input how many triangle numbers you would like to see printed out')

while True:
    try:
        user_input = int(input('> '))
        break
    except ValueError:
        print('Invalid input please enter an integer')

# we need a counter variable for our next while loop, and we will initialize it to 0
counter = 1

# we want to print out the amount of triangle numbers that the user specifies, so we are going to run the loop until our counter
# reaches that number... (i.e. counter <= user_input)
while counter <= user_input:
    
    # variable to house our triangle number equation
    tri_numb_equ = (counter * (counter + 1)) / 2

    # now we print that triangle number
    print(f'Triangle number {counter} = {tri_numb_equ}')

    # now we iterate the counter variable
    counter += 1