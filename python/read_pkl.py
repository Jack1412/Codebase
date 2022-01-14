# 读取 .pkl 文件

import joblib

filename = "00003200_EM.pkl"
clf = joblib.load(filename)
print (clf.keys())

joints3d_data = clf['joints3d']
shape_data = clf['shape']
pose_data = clf['pose']
trans_data = clf['trans']