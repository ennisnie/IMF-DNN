import os.path
import glob
import cv2
import numpy as np

def riluo(jpgfile, outdir):
    img = cv2.imread(jpgfile)
    try:
        print(u'正在处理中')
        w = img.shape[1]
        h = img.shape[0]

        for xi in range(0, w):
            for xj in range(0, h):
                img[xj, xi, 0] = int(img[xj, xi, 0] * 0.7)
                img[xj, xi, 1] = int(img[xj, xi, 1] * 0.7)

            # # 显示进度条
            # if xi % 10 == 0:
            #     print('.')
        cv2.imwrite(os.path.join(outdir, os.path.basename(jpgfile)), img)

    except Exception as e:
            print(e)
for jpgfile in glob.glob(r'DVR/*.jpg'):
    riluo(jpgfile, r'sunset/')
