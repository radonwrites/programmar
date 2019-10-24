import re
txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)
# (xoeu)*
#%%
txt = "aaaaaaa"
x = re.search("a*", txt)
print(x)
# x*
# * is 0 or more occurences 
# group of characters needs to be in parantheses
#%%
zipcode1 = "31245"

print(re.search("\d{5}(-\d{4})?", zipcode1))

#%%

zipcode2 = "32124-2432"
print(re.search("\d{5}(-\d{4})?", zipcode2))

#%%
zipcode3 = "3214"
print(re.search("\d{5}-\d{4}", zipcode3))

#%%

zipcode4 = "oue23"
print(re.search("\d{5}-\d{4}", zipcode4))

#%%

def zippy(zip):
    print(re.search("^\d{5}(-\d{4})?$", zip))

#%%
# another option instead of funtion here is to create a variable

zipcode = "^\d{5}(-\d{4})?$"

print(re.search(zipcode, zipcode3))

# if you use search/find in explorer/directory (left bar in VS code) it searches all files
# \d and \w are special and common
# \d = [0-9]
# \d = [0123456789]
# is this releated to calling a file in HTML, with the ./?
# %%

# time of day (with groups for each part of the time)

time1 = "5pm"
time2 = "12:00p"
time3 = "13:00a"
time4 = "00:02pm"

timely = "^([1-9]|1[0-2])(:\d\d)?[ap]m?$"
print(re.search(timely, time1))
print(re.search(timely, time2))
print(re.search(timely, time3))
print(re.search(timely, time4))

# %%
