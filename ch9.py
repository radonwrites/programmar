#%%
source = open('gameratdragon.txt', encoding="utf8")
alice = source.read()
print(alice[:1000])

# getting a UnicodeDecodeError for both texts - look into UTF-16 dealie
# alice.txt not found?
#moving on for now

#%%
import re
test = 'Here is a nice string. La la la.'
re.sub(r'\W+', '', test)


# %%
