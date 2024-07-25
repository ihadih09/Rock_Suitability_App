# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#Imported modules
import my_modules.io as io #imports the module io from the package my_modules and renames it as io
import matplotlib  #imports the module matplotlib 
matplotlib.use('TkAgg') #sets the backend of matplotlib to use TkAgg
from matplotlib import pyplot as plt #imports the pyplot module from matplotlib and renames it as plt
import my_modules.geometry as geometry #imports the module geometry from the package my_modules and renames it as geometry



#A function defining the rescaled data
def rescale(min_val, max_val, data):
    """
    Rescales a 2D array of data to fit between minimum and maximum values.

    Parameters
    ----------
    min_val : float
        The minimum value to rescale the data to.
    max_val : float
        The maximum value to rescale the data to.
    data : list[list[float]]
        A 2D array of data to be rescaled.

    Returns
    -------
    result : list[list[float]]
        A 2D array of the rescaled data.
    """
    # Calculate the maximum and minimum
    max_data = data[0][0]
    min_data = data[0][0]
    for i in range (n_rows):
        for j in range(n_cols):
            max_data = max(max_data, data[i][j])
            min_data = min(min_data, data[i][j])
    # Rescale the data
    result = []
    for i in range (n_rows):
        row=[]
        for j in range(n_cols):
            #row.append((data[i][j] - min_data)/(max_data - min_data))
            row.append((((data[i][j] - min_data)/(max_data - min_data))
                        *(max_val - min_val)) + min_val)
        result.append(row) 
    return result
    
#Read geology data and plot it    
geology, n_rows, n_cols = io.read_data('../data/input/geology.txt')
#print(geology)
plt.imshow(geology)
plt.show()

#Read population data and plot it
population, n_rows, n_cols = io.read_data('../data/input/population.txt')
#print(population)
plt.imshow(population)
plt.show()

# Read transport data and plot it
transport, n_rows, n_cols =io.read_data('../data/input/transport.txt')
#print(transport)
plt.imshow(transport)
plt.show()

#Set the weights for geology, population and transport
geo_w= 0.5
pop_w =0.6
tra_w =0.7

#Use the weight_raster function to create a weighted raster 
#from the geology, population, and transport data with given weights
weighted_rasters = geometry.weight_raster(geo_w, pop_w, tra_w, 
                                          n_rows,n_cols,
                                          geology,population,transport)

#Display the weighted raster using matplotlib's imshow function
print(weighted_rasters)
plt.imshow(weighted_rasters)
plt.show()

#Rescale the weighted raster values to a range between 0 and 255
rescaled_raster = rescale(0, 255, weighted_rasters)

#Display the rescaled raster using matplotlib's imshow function
print(rescaled_raster)
plt.imshow(rescaled_raster)
plt.show()

#Write the rescaled raster data to an output file using io.write_data function
io.write_data('mce_result.txt',rescaled_raster)



