import random
# storing words for the mad lib
# variable has to be defined within interpreter for it to understand
verbs = ["run","skip","frolic","hide","duck","swim"]
nouns = ["The cat","An orange"]
print(verbs)

#%%
print(random.choice(nouns) + " decided to " + random.choice(verbs))
#%%
