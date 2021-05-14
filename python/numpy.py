# --------------------------------------生成三维点网格坐标-------------------------------------------------------------
# 掌握函数：mgrid()、flatten()、zip()
# np.mgrid[start:end:step， start:end:step]
# ndarray.flatten(order='C')  把矩阵拉成一维的，C’(默认)：按行拉, ‘F’按列拉, ‘A’, ‘K’按照在内存中出现的顺序拉
import numpy as np
# 生成x和y为网格坐标点，z始终为0的 n*3维度的 np array
x_num = 7 # x方向点的个数
y_num = 6
step = 0.15 # 步长
xs, ys= np.mgrid[0.57:(0.57+x_num*step-step/2):step, -0.45:(-0.45+y_num*step-step/2):step]
# xs = array([[0.57, 0.57, 0.57, 0.57, 0.57, 0.57],
#        [0.72, 0.72, 0.72, 0.72, 0.72, 0.72],
#        [0.87, 0.87, 0.87, 0.87, 0.87, 0.87],
#        [1.02, 1.02, 1.02, 1.02, 1.02, 1.02],
#        [1.17, 1.17, 1.17, 1.17, 1.17, 1.17],
#        [1.32, 1.32, 1.32, 1.32, 1.32, 1.32],
#        [1.47, 1.47, 1.47, 1.47, 1.47, 1.47]])
# ys = array([[-4.50000000e-01, -3.00000000e-01, -1.50000000e-01, -5.55111512e-17,  1.50000000e-01,  3.00000000e-01],
#        [-4.50000000e-01, -3.00000000e-01, -1.50000000e-01, -5.55111512e-17,  1.50000000e-01,  3.00000000e-01],
#        [-4.50000000e-01, -3.00000000e-01, -1.50000000e-01, -5.55111512e-17,  1.50000000e-01,  3.00000000e-01],
#        [-4.50000000e-01, -3.00000000e-01, -1.50000000e-01, -5.55111512e-17,  1.50000000e-01,  3.00000000e-01],
#        [-4.50000000e-01, -3.00000000e-01, -1.50000000e-01, -5.55111512e-17,  1.50000000e-01,  3.00000000e-01],
#        [-4.50000000e-01, -3.00000000e-01, -1.50000000e-01, -5.55111512e-17,  1.50000000e-01,  3.00000000e-01],
#        [-4.50000000e-01, -3.00000000e-01, -1.50000000e-01, -5.55111512e-17,  1.50000000e-01,  3.00000000e-01]])
point3D = np.array([(x,y,0) for x,y in zip(xs.flatten(), ys.flatten())])
# ---------------------------------------------------------------------------------------------------------------------
	

# --------------------------------------生成三维点网格坐标-------------------------------------------------------------
# 掌握函数：mgrid()、reshape()
# numpy.reshape(a, newshape, order='C') 重新生成新的维度的矩阵
# newshape:新矩阵的维度，int或者tuple   order：C’, ‘F’, ‘A’，默认是C；C表示排列元素按照元素原来的索引进行，先改变最后一个维度的索引，比如三维的矩阵，一二维度先不变，第三个维度的索引依次+1进行排列，再比如二维情况下是按照‘行’来重排；F表示先改变第一个维度的索引，二维情况下是按照‘列’来重排；A不知道？？？
import numpy as np
# 生成x和y为网格坐标点，z始终为0的 n*3维度的 np array
x_num = 7 # x方向点的个数
y_num = 6
objectp3d = np.zeros((1, x_num * y_num, 3), np.float32)
objectp3d[0, :, :2] = np.mgrid[0:x_num, 0:y_num].T.reshape(-1, 2)  # 维度变化 2*6*9 -> 9*6*2 -> 54*2 注意：array的最后两个维度始终是二维矩阵的形式
# ---------------------------------------------------------------------------------------------------------------------