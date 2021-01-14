# Fibonacci Sequence

# 1. Understand the Problem
#   Restate: Output the fibonnaci sequence from 0 to a user inputted number
#   Inputs: From looking at the article about the Fibonnaci sequence, we can assume that our inputs should only be of type int
#   Outputs: This one is up to interpretation, I would ask the interviewer if they were looking for anything in particular, if not
#       then I would either print out the numbers one by one, or save them in a list and simply print the list out at the end
#   Labeling: fib_list, will probably need a counter variable. The function name could be fibonacci_sequence, the number the 
#       user inputs we can name user_input

#2. Exploring Concrete Examples
#   Small: fibonacci_sequence(4) --> [0, 1, 1, 2, 3] or
        # n => fibSequence(n)
        # 0 => 0
        # 1 => 1
        # 2 => 1
        # 3 => 2
        # 4 => 3
#   More Complex: fibonacci_sequence(10) --> [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
#   Edge Cases: fibonacci_sequence('ten') --> ?
#   Edge Cases: fibonacci_sequence() --> ?

#3. Break it down
#   1. Ask the user for a number
#   2. Check that the user inputted a valid number (int)
#   3. Create a Loop which starts at 0 and goes to the user inputted number, lets use a counter variable to keep track of the loops iterations
#   4. If the counter variable is 0 or 1, then we just append the counter variable to a list 
#   5. Else, we take the previous two numbers in the sequence, add them together, and then append their sum to our list
#   6. Iterate the counter
#   7. Outside the loop, return our list

# Helper function that checks if an input is an integer or not
def check_if_integer():
    while True:
        try:
            return int(input('> '))
        except ValueError:
            print('\nInvalid input, try again with an integer')

#4. Simply/Solve
def fibonacci_sequence():
    print('Input an integer. The integer will serve as an endpoint for the fibonacci sequence you would like me to output')
    user_input = check_if_integer()

    counter = 0
    fib_list = []
    while counter <= user_input:
        if counter == 0:
            fib_list.append(0)
        elif counter == 1:
            fib_list.append(1)
        else:
            prev_number = fib_list[counter - 1]
            second_prev_number = fib_list[counter - 2]
            new_number = prev_number + second_prev_number
            fib_list.append(new_number)
        counter = counter + 1
    return fib_list

# print(fibonacci_sequence())

#5. Look back and Refactor
def fibonacci_sequence2():
    print('Input an integer. The integer will serve as an endpoint for the fibonacci sequence you would like me to output')
    user_input = check_if_integer()

    counter = 0
    fib_list = []
    while counter <= user_input:
        if counter == 0 or counter == 1:
            fib_list.append(counter)
        else:
            fib_list.append(fib_list[counter - 1] + fib_list[counter - 2])
        counter += 1
    return fib_list
    
# print(fibonacci_sequence2())

# Recursively
def fibonacci_sequence3(num):
    if num <= 1: return num
    return fibonacci_sequence3(num - 1) + fibonacci_sequence3(num - 2)

print(fibonacci_sequence3(5))