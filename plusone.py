#%%
def addOne(value):
    return value + 1

#%%

# take result and assign it back to variable
# save result in same variable you pass it in
#this shows parameter vs argument? variable?
# variables store values, functions don't
#%%
def keepAdding(x):
    return x+1
#%%
x = 5
#%%
keepAdding(x)
#%%
x = keepAdding(x)
print(x)

#%%
# write function that takes two arguments and takes the first to the power of the second (multiplier)
# double is ... something, it's in the book
# 'for' iterates over some range and... does something?
for x in [2,3,4]:
    print(x)

#%%
sum = 0 
secondSum = 0
for x in range(100):
    sum = sum + x
    secondSum = secondSum + x*x

#%%
def double(input):
    for x in input:
        print(x*x*x)
# specify an array with brackets
#%%
def exponent(x,y):
    z = x
    for n in range(1,y):
        z = z*x
        return z

# getting an error for "unused variable 'n'" - why? why is it there anyway?
#%%
