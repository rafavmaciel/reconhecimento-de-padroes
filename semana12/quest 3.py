
from PIL import Image
from sklearn.cluster import KMeans
import imageio
import pandas as pd
import matplotlib.pyplot as plt

def transformar_data(lista):
    data=[]
    for l in range(len(lista)):
            for k in range(len(lista[l])):
                data.append(lista[l][k])
    return data

#carregando imagem 
image = Image.open('flor.jpg')
image_vector = imageio.imread("flor.jpg")
data = transformar_data(image_vector)

#iniciando classificador com k 8  e pegando os grupos
y_kmeans8 = KMeans(n_clusters=8, random_state=0).fit(data)
k_maeans8 = y_kmeans8.labels_

#iniciando classificador com k 64  e pegando os grupos
y_kmeans64=KMeans(n_clusters=64, random_state=0).fit(data)
k_maeans64 = y_kmeans64.labels_

#iniciando classificador com k 512 e pegando os grupos
y_kmeans512=KMeans(n_clusters=512, random_state=0).fit(data)
k_maeans512 = y_kmeans512.labels_

#agrupando com base nos centróides
def agrupar_int( y_kmeans):
    lista_cluster=[]
    for k in y_kmeans.cluster_centers_:
        lista_cluster.append([int("%1.f"%k[0]),int("%1.f"%k[1]),int("%1.f"%k[2])])
    return lista_cluster
   

#recontruindo vetor de img
def reconstruir_vetor(lista_cluster,y_kmeans):
    
    new_image=[]
    
    for k in y_kmeans8.labels_:
        new_image.append(lista_cluster[k])
    return new_image



def reconstruir_imagem(new_image_vector,image_vector):
    v=[]
    df=pd.DataFrame(new_image_vector)
    i=0
    f=518
    for d in range(len(image_vector)):
        v.append(df.iloc[i:f,:].values)
        i=f
        f=f+518
    
    return plt.imshow(v)

#inciando funçoes 
lista_cluster=agrupar_int( y_kmeans8)
new_image_vector=reconstruir_vetor(lista_cluster,y_kmeans8)
reconstruir_imagem(new_image_vector,image_vector)  

lista_cluster=agrupar_int(y_kmeans64)
new_image_vector=reconstruir_vetor(lista_cluster,y_kmeans64) 
reconstruir_imagem(new_image_vector,image_vector)

lista_cluster=agrupar_int(y_kmeans512)
new_image_vector=reconstruir_vetor(lista_cluster,y_kmeans512) 
reconstruir_imagem(new_image_vector,image_vector)
