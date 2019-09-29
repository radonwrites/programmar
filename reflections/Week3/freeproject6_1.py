#%%

# so I learned a thing
# apparently my code last time kinda did work with words...

def doubledouble(brew):
    spell = []
    for ingredient in brew:
        spell = spell + [ingredient * 2]
    return spell

doubledouble(['toil', 'trouble'])

# ... I just had forgotten the quotes

#%%

def witches(brew):
    spell = []
    for ingredient in brew:
        spell = spell + ['A dash of ' + ingredient + '...']
    return spell

witches(['frog','mouse','branch'])

# I tried adding 'amount' to add another word in front of the ingredient, but got 'TypeError: can only concatenate list (not "str") to list'
# still trying to figure that out

# I wouldn't say this function I'm invoking is particularly spellbinding...
# but I am trying to experiment more with stings and understanding concatenation and casting
# the modification here was the turn towards strings and away from numbers (for now)
#%%
