# ----------------------------OpenCV 背景差分法 Background Subtraction Methods(BS)-------------------------------------
# 掌握函数或类：createBackgroundSubtractorMOG2类, createBackgroundSubtractorKNN类
import numpy as np
import cv2 as cv

cap = cv.VideoCapture(0)	# read from a video file
backSub = cv.createBackgroundSubtractorMOG2()  # 类初始化
# backSub = cv.createBackgroundSubtractorKNN() # 另一种前背景分割方法

while(1):
    ret, frame = cap.read()
    fgmask = backSub.apply(frame) # 调用apply函数
    cv.imshow('frame',fgmask)
    k = cv.waitKey(30) & 0xff
    if k == 27:
        break
cap.release()
cv.destroyAllWindows()


# ----------------------------腐蚀与膨胀-------------------------------------
# 掌握函数或类：膨胀 cv2.dilate(src, kernel[, anchor[, iterations[, borderType[, borderValue]]]])
import numpy as np
import cv2

img = cv2.imread('这里放图片的名字或路径', 1)
cv2.imshow('Original', img)

kernel = np.ones((5, 5), 'uint8')

dilate_img = cv2.dilate(img, kernel, iterations=1)
cv2.imshow('Dilated Image', dilate_img)
cv2.waitKey(0)
cv2.destroyAllWindows()



# ----------------------------滤波-------------------------------------
# cv2.GussianBlur()函数

# 语法：GaussianBlur（src，ksize，sigmaX [，dst [，sigmaY [，borderType]]]）-> dst
# ——src输入图像；图像可以具有任意数量的通道，这些通道可以独立处理，但深度应为CV_8U，CV_16U，CV_16S，CV_32F或CV_64F。
# ——dst输出图像的大小和类型与src相同。
# ——ksize高斯内核大小。 ksize.width和ksize.height可以不同，但​​它们都必须为正数和奇数，也可以为零，然后根据sigma计算得出。
# ——sigmaX X方向上的高斯核标准偏差。
# ——sigmaY Y方向上的高斯核标准差；如果sigmaY为零，则将其设置为等于sigmaX；如果两个sigmas为零，则分别从ksize.width和ksize.height计算得出；为了完全控制结果，而不管将来可能对所有这些语义进行的修改，建议指定所有ksize，sigmaX和sigmaY。



# ------------------------OpenCV包含用于检测带有背景移除的移动对象的工具：--------------------

mask = backSub.apply(frame)  # 提取动态物体   
mask = cv.dilate(mask, None)     # 膨胀
mask = cv.GaussianBlur(mask, (15, 15),0)      #高斯滤波
ret,mask = cv.threshold(mask,0,255,cv.THRESH_BINARY | cv.THRESH_OTSU)   # 阈值化



HoughCircles()函数原型
1.  void cv::HoughCircles(InputArray  image,
2.                            OutputArray  circles,
3.                            int  method,
4.                            double  dp,
5.                            double  minDist,
6.                            double  param1 = 100,
7.                            double  param2 = 100,
8.                            int  minRadius = 0,
9.                            int  maxRadius = 0 
10.                           )

image：待检测圆形的输入图像，数据类型必须是CV_8U的单通道灰度图像。
circles：检测结果的输出量，每个圆形用三个参数描述，分别是圆心的坐标和圆的半径
method：检测圆形的方法标志，目前仅支持HOUGH_GRADIENT方法。
dp：离散化时分辨率与图像分辨率的反比。
minDist：检测结果中两个圆心之间的最小距离。
param1：使用HOUGH_GRADIENT方法检测圆形时，传递给Canny边缘检测器的两个阈值的较大值。
param2：使用HOUGH_GRADIENT方法检测圆形时，检测圆形的累加器阈值，阈值越大检测的圆形越精确。
minRadius：检测圆的最小半径
maxRadius：检测圆的最大半径。

#----------------------------给图片加文字------------------------------------------
# # cv2.putText() 参数：图片，添加的文字，左上角坐标，字体，字体大小，颜色，字体粗细
cv2.putText(dds_image, 'avm_time: %d' % self.avm_t, (20, 20),
            cv2.FONT_HERSHEY_SIMPLEX, 1.7, (0, 0, 0), 6)
cv2.putText(avm_image, 'xpu_time: %d' % self.dds_model.xpu_time, (20, 20),
            cv2.FONT_HERSHEY_SIMPLEX, 1.7, (0, 0, 0), 6)



