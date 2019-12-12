#%%
#adding previously written content for reference
from PIL import Image

def wordpix(image, x, y):
    for x in range():
        for y in range(): 
            #value = float(y)/ourimage.size[0]
            value = int(value*255)
            #ourimage.putpixel((x,y),(value,value,value,255))


mode = 'RGBA'
size = (100,100)
color = 'white'
aimage = Image.new(mode, size, color)

def addvert(image, x, r,g,b,a):
    for y in range(image.size[0]):
        image.putpixel((x,y),(r,g,b,a))
    return image

addvert(aimage, 30, 200,10,10,255)
# %%
#trying to add characters in place of pixels, used the "help" for Image to find 'fromstring' but this function doesn't work yet
mode = 'RGBA'
size = (100,100)
color = 'white'
aimage = Image.new(mode, size)

def chargrid(x,y):
    size = (x,y)
    image = Image.new(size)
    for x in range(x):
        for y in range(x):
            sentence = ("this is a sentence")
            image.fromstring(sentence, "n") #just trying to get something to show up and see what it is
        return image 

#%%
#from textblob import TextBlob
#tried just using nested loop, but it does not place the characters in a grid

def agrid(text,x,y):
    for x in range(x):
        print(text)
        for y in range(y):
            print(text)

# %%
# re-reading the assignment, I decided to go back and just focus on making an image first

def img(x,y,r,g,b,a):
    color = (r,g,b,a)
    image = Image.new('RGBA',(x,y),color)
    half = int(x/2)
    for y in range(half):
        for x in range(y):
            #shade = int(r*10) - this doesn't seem to do anything, also tried shade = (r/2,g/2,b/2,a) but needed to make an integer so decided to work with just one first
            #image.putpixel((x,y), shade)
            tint = int(g*2)
            shade = (r,tint,b,a)
            image.putpixel((half,y), shade)

        return image

#I'm trying to make half of the image a different color but it only added a vertical line and changing the x range changes the location
# %%
