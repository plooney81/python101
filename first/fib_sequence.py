# given an input from the user print out the fibinachi sequence up to that number

print('\nPlease input a number you would like to see the fibinachi sequence for')
print('e.g.If we inputted 5, then the program would output the fibinachi sequence from 0 to 5')
# checks to see if the user actually inputted an integer...if not, then it asks again
while True:
    try:
        user_input = int(input('> '))
        break
    except ValueError:
        print('\nInvalid input, please try again')

# initiate an empty list to house our fibinachi numbers
fib_list = []

# initiate our counter variable at zero
counter = 0

# while loop that goes until the counter is less than or equal to the user_input
while counter <= user_input:
    # If the counter is 0 or 1, then we just append the counter variable to our fib_list
    if counter == 0 or counter == 1:
        fib_list.append(counter)
    # if the counter isn't 0 or 1, then we append the addition of the previous two numbers in the list
    else:
        fib_list.append(fib_list[counter - 1] + fib_list[counter - 2])
    # print the counter (or the index) and then print the fib number corresponding to that index
    print(f'{counter} => {fib_list[counter]}')
    # we then iterate the counter
    counter += 1