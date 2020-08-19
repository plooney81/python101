# print the multiplication table for numbs 1 up to 10

# initiate our outer loop counter as 1
outer_number = 1
# we want the outer loop to loop 10 times so we could say <= 10 or < 11
while outer_number <= 10:

    # we need to reinitiate the inner loop counter for every outer loop sequence so the inner loop sequeuence will actual complete, 
    # if we initiate the inner_number up top (i.e. under the outer_number initiation) then it will only print out the table for the first outer number
    inner_number = 1
    while inner_number <= 10:
        multiplication = outer_number * inner_number
        print(f'{outer_number} X {inner_number} = {multiplication}')
        inner_number += 1

    outer_number += 1