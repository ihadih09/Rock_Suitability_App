# -*- coding: utf-8 -*-
"""
Created on Fri Apr 28 17:40:22 2023

@author: gy20ibs
"""
#Imported modules
import csv


# Read input data
def read_data(filepath):
    """
    Reads a csv file and returns the data as a list of lists.

    Parameters
    ----------
    filepath : str
        The path to the csv file to be read.
    
    Returns
    -------
    data : list of lists
        The data contained in the csv file.
    n_rows : int
        The number of rows in the data.
    n_cols : int
        The number of columns in the data.

    """
    f = open(filepath, newline='')
    data = []
    for line in csv.reader(f, quoting=csv.QUOTE_NONNUMERIC):
        row = []
        for value in line:
            row.append(value)
            #print(value)
        data.append(row)
    f.close()
    n_rows = len(data)
   # print("n_rows", n_rows)
    n_cols0 = len(data[0])
   # print("n_cols", n_cols0)
    #print(data)
    for row in range(1, n_rows):
        n_cols = len(data[row])
        if n_cols != n_cols0:
            print("Warning")
    return data, n_rows, n_cols
    f.close()
    #print(data)


#Write the data in a csv file
def write_data(filepath, rescaled_raster):
    """
    Writes rescaled raster data to a CSV file.

    Parameters
    ----------
    filepath : str
        The path to the output CSV file.
    rescaled_raster : list of lists
        The rescaled raster data to be written to the file.

    Returns
    -------
    None.
    """
    f = open(filepath, 'w', newline='')
    writer = csv.writer(f,delimiter=',',quoting=csv.QUOTE_NONNUMERIC)
    for row in rescaled_raster:
        writer.writerow(row)