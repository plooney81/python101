import math
import numpy
def getDigit(num, place): return math.floor(abs(num) / (10**place)) % 10
def digitCount(num):
    if num == 0: return 1
    return math.floor(math.log10(abs(num))) + 1
def maxDigit(arr):
    maxDigit = 0
    for num in arr:
        maxDigit = max(maxDigit, digitCount(num))
    return maxDigit
def radixSort(arr):
    end = maxDigit(arr)
    i = 0
    while i < end:
        buckets = [[], [], [], [], [], [], [], [], [], []]
        count = 0
        while count < len(arr):
            num = arr[count]
            buckets[getDigit(num, i)].append(num)
            count += 1
        arr = [item for sublist in buckets for item in sublist] #flattens the buckets list
        i += 1

    return arr

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
    if i >= factor/2:
        list_of_factors
        return list_of_factors
    if factor % i == 0: list_of_factors.extend([i, int(factor/i)])
    list_of_factors.extend(factor_a_number2(factor, i+1))
    return radixSort(list_of_factors)

print('Enter a number you would like to see the factors for? (int)')
print(factor_a_number2(checks_if_int()))
