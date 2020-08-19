# This while will keep asking the user for the input if they don't enter a number
while True:
    try:
        print('\nInput a number (integer) you would like to start from')
        n = int(input('> '))
        print('\nNow please input a number (integer) you would like to go to')
        m = int(input('> '))
        break
    except ValueError:
        print('\n\n')
        print('-' * 50)
        print('Invalid input, please input two integers when prompted')
        print('-' * 50)

# iterator variable i
i = n
# while loop that prints out the numbers n to m, one per line. 
# n and m are inputs from the user
while i <= m:
    print(i)
    # iterates the variable i after it has been printed
    i = i + 1