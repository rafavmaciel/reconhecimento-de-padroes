import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('imagens\equacoes.png',cv2.IMREAD_GRAYSCALE)
cv2.imwrite('saidas/quest7/image_orig.jpg', img)

#calculando o negativo
rows,cols = img.shape
for i in range(rows):
        for j in range(cols):
            img[i,j] = 255 -img[i,j]
cv2.imwrite('saidas/quest7/negativo.jpg', img)



#tratando
#suavizando
thresh, img_sobel_thresh = cv2.threshold(img,80,255,cv2.THRESH_BINARY)
cv2.imwrite('saidas/quest7/image_result.jpg', img_sobel_thresh)
