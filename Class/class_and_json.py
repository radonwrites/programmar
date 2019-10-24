#%%
class MyClass:
    """A simple example class""" #shows up on hover later
    i = 12345
    def __init__(self, name):
        self.name = name
    def f(self):
        return 'hello world from ' + self.name

#%%
aClass = MyClass("John")
print(aClass.f())
bClass = MyClass("Lucy")
print(bClass.f())

#%%
import json
data = {
    "president": {
        "name": "Zaphod Beeblebrox",
        "species": "Betelgeusian"
    }
}
#%% 
with open('out.json','w') as fh:
    json.dump(data, fh)

#%%
# Importing data from a json file:
with open('out.json', 'r') as nfh:
    obj = json.load(nfh)
    print(obj)
    print(obj["president"]["name"])

#%%
from PIL import Image
#%%
#'alpha' is basically masking
mode = 'RGBA'
size = (100,100)
color = (10,50,50,255)
ourimage = Image.new(mode, size, color)
ourimage
#%%
ourimage.putpixel((50,50),(255,255,255,100))
ourimage
#%%
# a byte is 8-bits (255 is number of bytes in 8bit or something)
# check if PIL can support 16-bit?
ourimage.save('allblack.png')

#%%