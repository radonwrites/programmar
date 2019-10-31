# old school filter exercise attempt - turn image green
#%%

from PIL import Image

def blur(img):
    blurred = Image.new('RGB', img.size, 'white')
    for x in range(1, img.size[0] - 1):
        for y in range(1, img.size[1] - 1):
            (r, g, b) = img.getpixel((x,y))
            change = differ(img, (x, y))/2.0
            change = int(round(change))
            blurred.putpixel((x, y), (r + change, g + change, b + change))
    return blurred

#%%
#turns image red
img = Image.open('Labs/lab2/cat.png')

def tint(img):
    tinted = Image.new('RGBA', img.size, 'white')
    for x in range(1, img.size[0] - 1):
        for y in range(1, img.size[1] - 1):
            (r, g, b, a) = img.getpixel((x,y))
            tinted.putpixel((x, y), (r - 100, g + 100, b - 100, a))
    return tinted

# %%
