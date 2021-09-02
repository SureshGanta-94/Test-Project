#import math library
import math
def factorial(n):
    return(math.factorial(n))

#input number
Number = int(input("Factorial Number: "))
Factorial = factorial(Number)

#Printing factorial number
print("The Factorail value of {0} is {1}".format(Number, Factorial) )