# Fizz Buzz

#1. Understand the problem
#   Restate: Loop through a series of numbers from 0 to user input
#   Inputs: User defined INTEGER
#   Outputs: Strings or INTs?
#   Labeling: Do we need an list to house our end values?

#2. Exploring Concrete Examples
#   Small: fizz_buzz(15) --> Output:
#       1, 2, fizz, 4, buzz, fizz, 7, 8, fizz, buzz, 11, fizz, 13, 14, fizzbuzz
#   More Complex: fizz_buzz(100) --> Ummmm
#   Edge Cases: fizz_buzz() or fizz_buzz(undefined) or fizz_buzz(null)

#3. Break it down:
#   1) Ask user to input an integer called user_input
#   2) Check if input is valid --> if not...keep asking
#   3) Create a loop that starts from 1 and goes to user_input
#   4) For each iteration of the loop, check if the number is divisible by 3 and 5
#   5) If divisible by 3 print 'fizz'
#   6) If divisible by 5 print 'buzz'
#   7) If divisible by 3 and 5 print 'fizzbuzz'
#   8) else...just print the number

# Check if Int helper function
def check_if_integer():
    while True:
        try:
            return int(input('> '))
        except ValueError:
            print('Invalid input, please enter an integer')


#4. Simplify/Solve:
def fizz_buzz(end_val):
    if(not end_val): return None
    for i in range(1, end_val+1):
        if(i % 3 == 0 and i % 5 == 0):
            print('fizzbuzz')
        elif(i % 3 == 0):
            print('fizz')
        elif(i % 5 == 0):
            print('buzz')
        else:
            print(i)
        

# print('Please enter an integer')
# fizz_buzz(check_if_integer())

#5. Look back and Refactor:
def fizz_buzz2(end_val):
    if(not end_val): return None
    for i in range(1, end_val+1):
        output = ''
        if i % 3 == 0: output += 'fizz'
        if i % 5 == 0: output += 'buzz'
        if len(output) < 1: output = i
        print(output)
        

# print('Please enter an integer')
# fizz_buzz2(check_if_integer())

# Recursively
def fizz_buzz3(end_val, counter=1):
    if counter == end_val: return
    output = ''
    if counter % 3 == 0: output += 'fizz'
    if counter % 5 == 0: output += 'buzz'
    if len(output) < 1: output = counter
    print(output)
    return fizz_buzz3(counter + 1)

print('Please enter an integer')
fizz_buzz3(check_if_integer())