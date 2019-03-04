import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import matplotlib as pt
import numpy as np
#%matplotlib inline
img = mpimg.imread("/Users/Kyle_Staples/Documents/GitHub/IS834/Test/xSixth_Floor.png")
implot = plt.imshow(img)
plt.scatter(x = [500,1000], y = [800,800], c='r', s=40)
plt.show()
