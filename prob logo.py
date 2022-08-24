import os
import time
from PIL import Image
logo=Image.open('logo.png')
logo = logo.convert('RGBA')    
logo=logo.resize((300,300))    ###logo resize to (300,300)
logo.save('logo.png')
X,Y=logo.size

os.makedirs('withlogo', exist_ok = True)  ###create a new folder named 'with logo'
for file in os.listdir('.'):
    if ( file.endswith('.jpeg') or file.endswith('.jpg')\
    or file.endswith('.png') or file.endswith('.PNG'))\
    and not (file=='logo.png'):  ###select all the pics and avoid the logo 
        im=Image.open(file)
        X1,Y1=im.size
        if Y1>Y and X1>X :
            if Y1>X1:
                im=im.resize((X,int((X/X1)*Y1)))   ###resize
                Y1,X1=im.size
            else:
                im=im.resize((int((Y/X1)*Y1),Y))
                Y1,X1=im.size
        if X1<X*2 and Y1<Y*2:
            im=im.resize((int(X*2),int(Y*2)))     ###if the logo pixels more than half the pic
            Y1,X1=im.size
        im.paste(logo,(X1-X,Y1-Y),logo)
        im.save(os.path.join('withlogo',"Logo"+file))  ###save the pic in the new folder
        im.show()  ###afficher les images avec logo
        time.sleep(0.9)
