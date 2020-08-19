# program that calculates the tip amount the user should leave based on two pieces of information that is provided from the user
# 1). The total bill amount 
# 2). The level of service which can be three possible options (a.good, b.fair, or c.bad)
#       good = 20% tip
#       fair = 15% tip
#       bad = 10% tip
# 3). Then we add an option to see if there are multiple people to divide up the check evenly

# prompt the user first for the bill amount
print('Input your bill amount')

# while loop for input validation, only way it will stop looping is if user inputs valid number
while True:
    try:
        bill_amount = float(input('> '))
        break
    except ValueError:
        print('Invalid input. Please enter a valid number')

# prompt the user for the service level
print('Input the level of service based on the following values')
print('1 --> good (20% tip)')
print('2 --> fair (15% tip)')
print('3 --> bad (10% tip)')

# another while loop for input validation, only way it will stop looping is if user inputs valid number
while True:
    try:
        service_level = int(input('> '))
        break
    except ValueError:
        print('Invalid input. Please enter an integer from 1 to 3')

# based on the service_level value the user inputted, we can then calculate the total_bill amount
if service_level == 1:
    total_bill = bill_amount * 1.20
elif service_level == 2:
    total_bill = bill_amount * 1.15
elif service_level == 3:
    total_bill = bill_amount * 1.10
else:
    print('This should\'nt be happening')

# prompt the user to enter the number of people who participated in dinner
print('Input the amount of people who participated in dinner')
while True:
    try:
        numb_of_people = int(input('> '))
        break
    except ValueError:
        print('Invalid input. Please enter an integer')

# divide the total_bill by the number of people
divided_bill = total_bill / numb_of_people

#finally we print the new total with the tip included
print(f'The bill for each of the {numb_of_people} is ${divided_bill}')