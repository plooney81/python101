print('Groceries List')

list = []

counter = 0

def print_list():
    counter2 = 1
    # print the items nicely
    for groceries in list:
        print(f'Item {counter2} is {groceries}')
        counter2 += 1
    main_menu()

def print_list2():
    counter2 = 1
    # print the items nicely
    for groceries in list:
        print(f'Item {counter2} is {groceries}')
        counter2 += 1


def main_menu():
    while True:
        try:
            main_input = int(input('What would you like to do 1).Add 2).Print 3).Remove\n> '))
            if main_input < 1 and main_input > 3:
                raise ValueError
            break   
        except ValueError:
            print('Invalid input please try again')
    
    if main_input == 1:
        add_function()
    elif main_input == 2:
        print_list()
    else: 
        remove_function()

# Function for adding inputs
def add_function():
    counter = 0
    # while loop
    while True:
        if counter != 0:
            user_input = input("Would you like to add another item?\n> ").lower()
        else:
            user_input = "yes"

        if user_input == "yes":
            item = input("What's the item? ")
            list.append(item)
        elif user_input == "no":
            main_menu()
        else:
            print('Invalid input, please input either yes or no')
        
        counter += 1

def remove_function():
    counter2 = 0
    # ask if the user want to remove an item
    while True:
        print_list2()
        if counter2 != 0:
            wants_to_remove = input("Do you want to remove another item?\n> ").lower()
        else:
            wants_to_remove = 'yes'
        if wants_to_remove == 'yes' and len(list) > 0:
            # which item do you want to remove?
            remove_item = input('What item do you want to remove? (use the index from above)\n> ')
            while True:
                try:
                    remove_item = int(remove_item)
                    if remove_item < 0 and remove_item > len(list):
                        raise ValueError
                    else:
                        break
                except ValueError:
                    print(f'Invalid input, please input an integer between 0 and {len(list)}')
            list.pop(remove_item-1)
        elif wants_to_remove == 'no':
            # do something else
            main_menu()
        elif len(list) == 0:
            print('There is nothing left in here')
            main_menu()
        counter2 += 1
main_menu()