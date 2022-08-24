import PIL
import os
count = 0
file_count =0
paths =[]
for path, dirnames, filenames in os.walk('C://'):
	for i in filenames:
		file_count +=1
		if i.endswith('.png') or i.endswith('.jpg'):
			count+=1
			if path not in paths and count > file_count:
				paths.append(path)
			print("picture name is "+str(i)+" and the path is :"+path)
print("files found : "+str(count))


os.listdir('.')
