#批量改尺寸
import os.path
import glob
import cv2
import numpy as np

def convertjpg(jpgfile, outdir, width=128, height=128):
    src = cv2.imread(jpgfile, cv2.IMREAD_ANYCOLOR)

    try:
        dst = cv2.resize(src, (width, height), interpolation=cv2.INTER_CUBIC)
        cv2.imwrite(os.path.join(outdir, os.path.basename(jpgfile)), dst)
    except Exception as e:
        print(e)

for jpgfile in glob.glob(r'DVR/*.jpg'):
    convertjpg(jpgfile, r'resize/')
