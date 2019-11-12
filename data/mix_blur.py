##深度学习过程中，需要制作训练集和验证集、测试集。

import os, random, shutil
def moveFile(fileDir1,fileDir2):
    pathDir = os.listdir(fileDir1)    #取图片的原始路径
    filenumber=len(pathDir)
    rate=0.5    #自定义抽取图片的比例，比方说100张抽10张，那就是0.1
    picknumber=int(filenumber*rate) #按照rate比例从文件夹中取一定数量图片
    sample = random.sample(pathDir, picknumber)  #随机选取picknumber数量的样本图片
    print (sample)
    for name in pathDir:
        if name in sample:
            shutil.copyfile(os.path.join(fileDir1,name), os.path.join(tarDir,name))
        elif name not in sample:
            shutil.copyfile(os.path.join(fileDir2,name), os.path.join(tarDir,name))
    return

if __name__ == '__main__':
    for i in  range(1,21):
        jpgdir = os.path.join(r"test",str(i)) 
        typ='blur'
        fileDir1=  os.path.join(jpgdir,typ)#源图片文件夹路径
        fileDir2 = os.path.join(jpgdir,r'dvr_66x200')
        savedir= os.path.join(jpgdir,r'mixed')   #源图片文件夹路径
        if 'mixed' not in os.listdir(jpgdir):
	        os.mkdir(savedir)
        tarDir = os.path.join(savedir,typ)   #移动到新的文件夹路径
        if typ not in os.listdir(savedir):
	        os.mkdir(tarDir)
        moveFile(fileDir1,fileDir2)
















	

