import os.path
import glob
import cv2
import numpy as np

def rota(jpgfile, outdir):
    img = cv2.imread(jpgfile)
    img_info=img.shape
    image_height=img_info[0]
    image_weight=img_info[1]
    im_rotate=cv2.getRotationMatrix2D((image_weight*0.5,image_height*0.5,),5,1)    #center angle 3scale

    dst = cv2.warpAffine(img, im_rotate, (image_weight,image_height))
    cv2.imwrite(os.path.join(outdir, os.path.basename(jpgfile)), dst)

for jpgfile in glob.glob(r'DVR/*.jpg'):
#for jpgfile in glob.glob(r'D:\kitti\data_object_image_2\training\image_2\*.png'):
        rota(jpgfile, r'rota2/')
