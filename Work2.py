def my_function(given_number):
    List = []
    for i in range(1,given_number):
        if (i%3==0 or i%7==0):
            List.append(i)
    print(sum(List))    
    return


my_function(10000)