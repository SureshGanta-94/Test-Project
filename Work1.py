def divisible_five(given_number):
    my_list = []
    for i in range(1,given_number):
        if(i % 5 == 0):
            my_list.append(i)
    print(my_list)
    return my_list

divisible_five(121)