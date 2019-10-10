# [Exercise 7-3] Categorical, Imperative
#%%
def smarts(word):
    if len(word) >= 8:
        verdict = 'smart!'
    if len(word) < 8:
        verdict = 'eh.'
    return verdict

#%%
