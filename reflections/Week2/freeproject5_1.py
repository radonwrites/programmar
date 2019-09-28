# the task here is to modify the double() function
# here is the original function
#%%
def double(sequence):
    result = []
    for element in sequence:
        result = result + [element * 2]
    return result

#%%
# something that is confusing me is what language matters and what doesn't
# the terms 'sequence', 'result', 'element' all sounded like the necessary words for the function to... function
# so first I wanted to replace those words and see if it worked
def doubledouble(brew):
    spell = []
    for ingredient in brew:
        spell = spell + [ingredient * 2]
    return spell

#it does!
#%%
#now, can use words in my brew instead of numbers?

# I tried this: doubledouble([toil, trouble])

#%%
# nope
# but I want to make a spell! 

def witchesbrew(brew):
    spell = []
    for ingredient in brew:
        spell = spell + [ingredient * 2]
    return spell

# with help from the internet I tried to quickly make this thing but it didn't work:
# ingredient = [1:"frog", 2:"mouse", 3:"basil", 4:"mice", 6:"mushroom"]

#%%
# maybe next time, in the meantime I'll just tweak this equation
# I'm still confused about how it works... why is spell = spell necessary?
# it is though - I get '10' from [3, 5] otherwise
# and spell - [ingredient * 2] is a TypeError, just fyi

def numericalbrew(brew):
    spell = []
    for ingredient in brew:
        spell = spell + [ingredient*ingredient] + [ingredient/2] 
    return spell

# not the most inspiring experimentation, but here we are
# for now!
# to be continued??
#%%
