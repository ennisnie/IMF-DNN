
#运动模糊

import os.path
import glob
import cv2
import numpy as np

def mohu(jpgfile, outdir):
    img = cv2.imread(jpgfile)
    try:
        print(u'正在处理中')

            # 显示进度条
        degree=10
        angle=20
        image = np.array(img)

        # 这里生成任意角度的运动模糊kernel的矩阵， degree越大，模糊程度越高
        M = cv2.getRotationMatrix2D((degree / 2, degree / 2), angle, 1)
        motion_blur_kernel = np.diag(np.ones(degree))
        motion_blur_kernel = cv2.warpAffine(motion_blur_kernel, M, (degree, degree))

        motion_blur_kernel = motion_blur_kernel / degree
        blurred = cv2.filter2D(image, -1, motion_blur_kernel)
        # convert to uint8
        cv2.normalize(blurred, blurred, 0, 255, cv2.NORM_MINMAX)
        blurred = np.array(blurred, dtype=np.uint8)

        cv2.imwrite(os.path.join(outdir, os.path.basename(jpgfile)), blurred)

    except Exception as e:
            print(e)
for jpgfile in glob.glob(r'DVR/*.jpg'):
    mohu(jpgfile, r'blur/')
