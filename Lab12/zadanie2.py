import zadanie1, numpy as np
from PIL import Image

img = Image.open("Lenna.png")
bw_img = img.convert('L')
img_array = np.array(bw_img)

img_array = zadanie1.obrot(img_array, 90)
img_back = Image.fromarray(img_array)
img_back.show()
img_back.save("Lenna2.png")