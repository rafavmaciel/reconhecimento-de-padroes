import cv2
import numpy as np
from matplotlib import pyplot as plt

#carrregando img
img = cv2.imread('imagens\Fig1007(a)(wirebond_mask).png',cv2.IMREAD_GRAYSCALE)
cv2.imwrite('saidas/quest4/image_orig.jpg', img)

#carregando filtros 
sobel_x =  np.array([[-1,-2,-1],[0,0,0],[1,2,1]])
sobel_y =  np.array([[-1,0,1],[-2,0,2],[-1,0,1]])
sobel_45 =  np.array([[0,1,2],[-1,0,1],[-2,-1,0]])
sobel_135=np.array([[-2, -1, 0],[-1, 0, 1],[0, 1, 2]])
sobel_30=np.array([[1, 1, 1, 1, 0],  [1, 1, 0, 0, 0], [0, 0, 0, -1, -1],[0, -1, -1, -1, -1]])

img_pros_x = cv2.filter2D(img,-1,sobel_x)
img_pros_y = cv2.filter2D(img,-1,sobel_y)
img_pros_45 = cv2.filter2D(img,-1,sobel_45)
img_pros_135 = cv2.filter2D(img,-1,sobel_135)
img_pros_30 = cv2.filter2D(img,-1,sobel_30)
cv2.imwrite('saidas/quest4/img_pros_x.jpg', img_pros_x)
cv2.imwrite('saidas/quest4/img_pros_y.jpg', img_pros_y)
cv2.imwrite('saidas/quest4/img_pros_45.jpg', img_pros_45)
cv2.imwrite('saidas/quest4/img_pros_135.jpg', img_pros_135)
cv2.imwrite('saidas/quest4/img_pros_30.jpg', img_pros_30)



