# -*- coding: utf-8 -*-
"""
Created on Thu May 11 09:13:10 2023

@author: ihadi
"""
#Imported modules
import doctest

#First testing
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
     
    Testing
    --------
    # >>> a = [[10], [2]]
    # >>> min = 1
    # >>> max = 2
    # >>> rescale(min, max, a)
    # [[2.0], [1.0]]
    """
    # Calculate the maximum and minimum
    max_data = data[0][0]
    min_data = data[0][0]
    n_rows = len(data)
    n_cols = len(data[0])
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

#Run testing
doctest.testmod()

#Second Testing
#A function defining the weighted raster values
def weight_raster(geo_w, pop_w , tra_w, n_rows,n_cols,geology,population,transport):
    """
    Calculates the weighted sum of values in three rasters.

    Parameters
    ----------
    geo_w : float
        Weight of geology raster.
    pop_w : float
        Weight of population raster.
    tra_w : float
        Weight of transport raster.
    n_rows : int
        Number of rows in the rasters.
    n_cols : int
        Number of columns in the rasters.
    geology : list
        2D list representing geology raster.
    population : list
        2D list representing population raster.
    transport : list
        2D list representing transport raster.

    Returns
    -------
    weighted_data : list
        2D list representing the weighted raster.

    Testing
    --------
    >>> geology = [[1, 2], [3, 4]]
    >>> population = [[5, 6], [7, 8]]
    >>> transport = [[9, 10], [11, 12]]
    >>> weight_raster(0.3, 0.4, 0.3, 2, 2, geology, population, transport)
    [[5.0, 6.0], [7.0, 8.0]]
    """
    #calculate weighted sum of values at position (i, j) in each raster
    weighted_data= []
    for i in range (n_rows):
        row=[]
        for j in range(n_cols):
            weight= geology[i][j] * geo_w + population[i][j] * pop_w + transport[i][j] * tra_w
            row.append(weight)
        weighted_data.append(row)
        
    return weighted_data

#Run testing
doctest.testmod()