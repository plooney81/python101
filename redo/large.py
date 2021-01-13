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
    print(count)

# triangle_number_iteratively()

# Factor a number Recursively
def factor_a_number(factor, i=1, list_of_factors=[]):
    if i == factor:
        list_of_factors.append(factor) 
        return list_of_factors
    if factor % i == 0: list_of_factors.append(i)
    return factor_a_number(factor, i+1)
# print('Enter a number you would like to see the factors for? (int)')
# print(factor_a_number(checks_if_int()))

# Factor a number Recursively2
def factor_a_number2(factor, i=1):
    list_of_factors = []
    if i >= factor/2: return list_of_factors
    if factor % i == 0: list_of_factors.extend([i, int(factor/i)])
    list_of_factors.extend(factor_a_number2(factor, i+1))
    return list_of_factors

print('Enter a number you would like to see the factors for? (int)')
print(factor_a_number2(checks_if_int()))