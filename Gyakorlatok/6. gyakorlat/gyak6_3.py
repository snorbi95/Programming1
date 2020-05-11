import matplotlib.pyplot as plt
import matplotlib.image as img
import numpy as np

def rgb2gray(image):
    gray = np.uint8(0.2989 * image[:,:,0] + 0.5870 * image[:,:,1] + 0.1140 * image[:,:,2])
    return gray

image = img.imread('flowers.jpg') #kep beolvasasa
gray = rgb2gray(image) #megfelelo sulyokkal szurkeskalassa konvertalva
plt.subplot(1,2,1) #reszdiagram definialasa
plt.imshow(image) #kep megjelenites
plt.subplot(1,2,2)
plt.imshow(gray,cmap='gray')
plt.show()