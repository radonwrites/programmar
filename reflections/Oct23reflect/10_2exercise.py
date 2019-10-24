#from the book
#%%
from PIL import Image

def flip(pngimage):
    width = pngimage.size[0]
    for y in range(pngimage.size[1]):
        for x in range(width):
            half = int(width/2)
            left = pngimage.getpixel((x,y))
            right = pngimage.getpixel((half - 1 - x,y))
            pngimage.putpixel((half - 1 - x,y), left)
            pngimage.putpixel((x,y), right)
#value = float(x)/ourimage.size[0]
#value = int(value*255)
#%%
testimage = Image.open('reflections/Oct23reflect/labdogsflip.png')
flip(testimage)
testimage

# %%

def flop(pngimage):
    height = pngimage.size[0]
    for y in range(pngimage.size[1]):
        for x in range(height):
            hi = pngimage.getpixel((x,y))
            lo = pngimage.getpixel((height - 1 - x,y))
            hi, lo = lo, hi
            pngimage.putpixel((height - 1 - x,y), hi)
            pngimage.putpixel((x,y), lo)

#%%

testimage = Image.open('reflections/Oct23reflect/labdogsflip.png')
flop(testimage)
testimage
# hard to see what I'm doing wrong since the image doesn't change, still working
# %%
