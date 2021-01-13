def checks_if_int():
    while True:
        try:
            return int(input('> '))
        except ValueError:
            print('\nInvalid input, please enter an integer')

# Triangle Numbers
def triangle_number(numb, i = 1, count = 1):
    if i == numb: return count
    return triangle_number(numb, i + 1, count + i + 1)

# print('What triangle number would you like to find? (int)')
# print(triangle_number(checks_if_int()))

def triangle_number_iteratively():
    print('What triangle number would you like to find? (int)')
    numb = checks_if_int()
    i = 1
    count = 1
    while i < numb:
        i += 1
        count += i
    print(count) #prints the count

triangle_number_iteratively()