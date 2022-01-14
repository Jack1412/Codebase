# 读取路径下带有固定后缀的文件
# 方法一
import imp
import os
path = './'
suffix = '.pkl'
dirs = os.listdir(path)
for filename in dirs:
    if os.path.splitext(filename)[1] == suffix:
        pass
    pass

# 方法二
import glob
path = './'
suffix = '.pkl'
img_list = sorted(glob.glob(path + '*' + suffix))
NUM_IMGS = len(img_list)
for i in range(NUM_IMGS):
    pass