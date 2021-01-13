# for loop that prints only odd numbers from 0 to 99
for counter in range(100):
    # boolean var that is true if the counter is even
    is_odd = counter % 2 != 0
    # if our boolean var is true (aka the counter is odd) then we will print that number
    if is_odd:
        print(counter)