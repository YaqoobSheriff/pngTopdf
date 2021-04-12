from PIL import Image
from os import listdir
#change path to your preferred path containing images
path = 'C:/userScreenShots/user2'
imagelist = listdir(path)
finallist = []


for i in range(len(imagelist)):
        path1 = path + '/'+ imagelist[i]
        image = Image.open(path1)
        im1 = image.convert('RGB')
        finallist.append(im1)

print(finallist)

one = finallist[0]
finallist.pop(0)
one.save(r'C:\Users\admin\Desktop\finalPdfs\allimmages.pdf',save_all=True, append_images=finallist)
#Change the path to your desired location to store pdf file