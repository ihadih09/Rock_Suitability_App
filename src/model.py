# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import my_modules.io as io
import matplotlib
from matplotlib import pyplot as plt
import my_modules.geometry as geometry

geology =io.data[0]
#print(geology)

plt.imshow(geology)
plt.show()

population =io.data[1]
#print(population)

plt.imshow(population)
plt.show()

transport =io.data[2]
#print(transport)

plt.imshow(transport)
plt.show()

factors = [0.5, 0.3, 0.2]
rescaled_raster = geometry.weight_rasters(io.data, factors)
print(rescaled_raster)

plt.imshow(rescaled_raster, cmap= 'Blues')
plt.show()

n_cols = io.write_data(rescaled_raster)