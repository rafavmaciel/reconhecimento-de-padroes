# -*- coding: utf-8 -*-
"""
Created on Sat Nov  6 18:19:46 2021

@author: rafav
"""
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('imagens\Fig0338(a)(blurry_moon).png',cv2.IMREAD_GRAYSCALE)
cv2.imwrite('saidas/image_orig.jpg', img)

#carregando os filtros 
laplaciano = np.array([[0,-1,0],[-1,4,-1],[0,-1,0]])
laplaciano_2 = np.array([[-1,-1,-1],[-1,8,-1],[-1,-1,-1]])

# aplicando o filtro laplaciano 
img_pros = cv2.filter2D(img,-1,laplaciano)
img_pros_2 = cv2.filter2D(img,-1,laplaciano_2)
cv2.imwrite('saidas/filtro_laplaciano_1.jpg', img_pros)
cv2.imwrite('saidas/filtro_laplaciano_2.jpg', img_pros_2)

# o centro do filtro é positivo , logo tem que fazer abtração
img_add = cv2.add(img, img_pros)
img_add_2 = cv2.add(img, img_pros_2)
cv2.imwrite('saidas/imagem_resultante_1.jpg', img_add)
cv2.imwrite('saidas/imagem_resultante_2.jpg', img_add_2)
cv2.waitKey(0)
cv2.destroyAllWindows()

#cv2.imshow('imagem resultante',img_sum)