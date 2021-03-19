import matplotlib.pyplot as plt
import matplotlib.image as img
import numpy as np

def convert_to_grayscale(image):
    gray = np.uint8(0.2989 * image[:,:,0] + 0.5870 * image[:,:,1] + 0.1140 * image[:,:,2])
    return gray

image = img.imread('flowers.jpg')
fig, ax = plt.subplots(1,3)
ax[0].imshow(image[:,:,0], cmap='gray')
ax[0].set_xlabel('Red')
ax[1].imshow(image[:,:,1], cmap='gray')
ax[1].set_xlabel('Green')
ax[2].imshow(image[:,:,2], cmap='gray')
ax[2].set_xlabel('Blue')
fig.suptitle('RGB')
plt.show()
image_gray = convert_to_grayscale(image)
plt.imshow(image_gray, cmap='gray')
plt.show()