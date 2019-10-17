# Write your code here
def factorial(input):
    if(type(input)==type(3.0)):
        raise ValueError('Need integer value')
    if(input==0):
        return 1
    else:
        return input*factorial(input-1)

factorial(5)
#need a base case for recursion to work