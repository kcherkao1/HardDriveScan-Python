import cv2
from PIL import Image
import os
img_count = 0
file_count =0
paths =[]
pics_more=[]
for path, dirnames, filenames in os.walk('C:\\Users\\Admin\\Desktop'):
    if path not in paths :
        paths.append(path)
for i in paths:
    #print (i)
    for file in os.listdir(i):
        img = cv2.imread(os.path.join(i,file))
        file_count +=1
        #print(file)
        if file.endswith('.png') or file.endswith('.jpg') or file.endswith('.PNG')\
           or file.endswith('.jpeg'):
            img_count+=1
        if img_count*2 >= file_count and i not in pics_more:
            pics_more.append(i)
        img_count = 0
        file_count =0

#print(paths)
#print(file_count,img_count)
for i in range (len(pics_more)):
    print(pics_more[i])

