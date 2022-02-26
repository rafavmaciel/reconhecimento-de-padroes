import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

def gerar_histograma (caminho):
    img = cv.imread(caminho).tolist()
    vetor_pixel_quant = [0 for x in range(256)]
    pixel_list = []
    
    for l in img:
        for c in l:
            index = c[0]
            vetor_pixel_quant[index] += 1
            pixel_list.append(index)
            
           
    
    plt.title('histograma')
    plt.xlabel('valor do pixel')
    plt.ylabel('Frequência Absoluta')
    plt.hist(pixel_list, 256, alpha=0.5,
             histtype='stepfilled', color='steelblue',
             edgecolor='none')
    plt.show()    
    #cv.imshow('fig',img)
    #cv.waitKey(0)

lista_caminhos= ['imagens/Fig0320(1)(top_left).png','imagens/Fig0320(2)(2nd_from_top).png',
                 'imagens/Fig0320(3)(third_from_top).png','imagens/Fig0320(4)(bottom_left).png',
                 'imagens/Fig0323(a)(mars_moon_phobos).png','imagens/Fig0309(a)(washed_out_aerial_image).png',
                 'imagens/Fig0308(a)(fractured_spine).png']
for caminho in lista_caminhos:
    gerar_histograma(caminho)