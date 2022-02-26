import cv2
import numpy as np
from matplotlib import pyplot as plt

#carrregando img
img = cv2.imread('imagens\Fig0340(a)(dipxe_text).png',cv2.IMREAD_GRAYSCALE)
cv2.imwrite('saidas/quest3/image_orig.jpg', img)

roberts_x = np.array([[-1,0],[0,1]])
roberts_y = np.array([[0,-1],[1,0]])

img_pros_x = cv2.filter2D(img,-1,roberts_x)
img_pros_y = cv2.filter2D(img,-1,roberts_y)
cv2.imwrite('saidas/quest3/filtro_roberts_x.jpg', img_pros_x)
cv2.imwrite('saidas/quest3/filtro_roberts_y.jpg', img_pros_y)

img_add = cv2.add(img_pros_x, img_pros_y)
cv2.imwrite('saidas/quest3/filtro_roberts.jpg', img_add)

