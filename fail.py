import os
from PIL import Image

SQUARE_FIT_SIZE = 300
SQUARE_FIT_SIZE_LOGO = 30
LOGO_FILENAME = 'logo1.png'

logoIm = Image.open(LOGO_FILENAME)
logoWidth, logoHeight = logoIm.size

if logoWidth > SQUARE_FIT_SIZE_LOGO and logoHeight > SQUARE_FIT_SIZE_LOGO:
    if logoWidth > logoHeight:
        logoHeight = int((SQUARE_FIT_SIZE_LOGO / logoWidth) * logoHeight)
        logoWidth = SQUARE_FIT_SIZE_LOGO
    else:
        logoWidth = int((SQUARE_FIT_SIZE_LOGO / logoHeight) * logoWidth)
        logoHeight = SQUARE_FIT_SIZE_LOGO
    logoIm = logoIm.resize((logoWidth, logoHeight))

os.makedirs('withlogo', exist_ok = True)  #making new directory to save the combined image

for filename in os.listdir('.'):
    if not(filename.lower().endswith('.png') or filename.lower().endswith('.gif')\
    or filename.lower().endswith('.jpg') or filename.lower().endswith('bmp')) or filename == LOGO_FILENAME :
         continue                       #skip non-image files and the logo file itself
    im = Image.open(filename)
    width, height = im.size

#Check if image needs to be resized.
    if width > SQUARE_FIT_SIZE and height > SQUARE_FIT_SIZE:
        if width > height:
            height = int((SQUARE_FIT_SIZE / width) * height)
            width = SQUARE_FIT_SIZE
        else:
            width = int((SQUARE_FIT_SIZE / height) * width)
            height = SQUARE_FIT_SIZE
        #Resize the image.
        print('Resizing %s...' % (filename))
        im = im.resize((width, height))

    #ADD the logo.
    print('Adding logo to %s...' % (filename))
    im.paste(logoIm, (width - logoWidth, height - logoHeight), logoIm)


    #save changes
    im.save(os.path.join('withlogo', filename))
    im.show()
