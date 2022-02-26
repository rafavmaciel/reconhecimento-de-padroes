# -*- coding: utf-8 -*-
"""
Created on Sat Nov  6 18:19:46 2021

@author: rafav
"""
import cv2
import numpy as np
from matplotlib import pyplot as plt

#carrregando img
img = cv2.imread('imagens\Fig0340(a)(dipxe_text).png',cv2.IMREAD_GRAYSCALE)
cv2.imwrite('saidas/quest2/image_orig.jpg', img)

#gerando o desfoque gaussiano 5x5
g_blur = cv2.GaussianBlur(img,(5,5),cv2.BORDER_DEFAULT)
cv2.imwrite('saidas/quest2/image_desfocada.jpg', g_blur)

#subtraindo as imgs 
img_sub = cv2.subtract(img, g_blur)
cv2.imwrite('saidas/quest2/mascara.jpg', img_sub)
#percorrendo os pixels
rows,cols = img.shape
k_vals = [1,2,5,10,15,20,25,30,35]
nova_img = np.zeros((138,320))

for k in k_vals:
    for i in range(rows):
        for j in range(cols):
            nova_img[i,j] = img[i,j] + (k*(img_sub[i,j]))
            cv2.imwrite('saidas/quest2/imagem_resutante_'+ str(k) +'.jpg', nova_img)
            