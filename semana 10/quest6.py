import cv2
import numpy as np
from matplotlib import pyplot as plt

#carrregando img
img = cv2.imread('imagens\Fig1016(a)(building_original).png',cv2.IMREAD_GRAYSCALE)
cv2.imwrite('saidas/quest6/image_orig.jpg', img)

#carregando filtros 
sobel_x =  np.array([[-1,-2,-1],[0,0,0],[1,2,1]])
sobel_y =  np.array([[-1,0,1],[-2,0,2],[-1,0,1]])

img_pros_x = cv2.filter2D(img,-1,sobel_x)
img_pros_y = cv2.filter2D(img,-1,sobel_y)
img_sobel = cv2.add(img_pros_x,img_pros_y)
cv2.imwrite('saidas/quest6/image_sobel_no_blur.jpg', img_sobel)

# com suavisação

g_blur = cv2.GaussianBlur(img,(5,5),cv2.BORDER_DEFAULT)
img_pros_x_gau = cv2.filter2D(g_blur,-1,sobel_x)
img_pros_y_gau = cv2.filter2D(g_blur,-1,sobel_y)
img_sobel_gau = cv2.add(img_pros_x_gau,img_pros_y_gau)
cv2.imwrite('saidas/quest6/image_sobel_with_blur.jpg', img_sobel_gau)

#com limiar sem suavização

thresh, img_sobel_thresh = cv2.threshold(img_sobel,80,255,cv2.THRESH_BINARY)
cv2.imwrite('saidas/quest6/image_sobel_no_blur_lim.jpg', img_sobel_thresh)

#com limiar com suavização

thresh, img_sobel_gau_thresh = cv2.threshold(img_sobel_gau,80,255,cv2.THRESH_BINARY)
cv2.imwrite('saidas/quest6/image_sobel_blur_lim.jpg', img_sobel_gau_thresh)


