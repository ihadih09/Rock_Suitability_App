# -*- coding: utf-8 -*-
"""
Created on Fri Apr 28 17:40:22 2023

@author: gy20ibs
"""


import csv

def read_raster_files(file_path):
    data = []
    for i in range(1, 4):
        file_name = f"{file_path}/file{i}.txt"
        with open(file_name, 'r') as f:
            reader = csv.reader(f)
            rows = []
            for row in reader:
                rows.append([float(val) for val in row])
            data.append(rows)
    return data

file_path = '../data/input'
data = read_raster_files(file_path)

def write_data(rescaled_raster):
    f = open('../data/output/outputF.txt', 'w', newline='')
    writer = csv.writer(f,delimiter=',',quoting=csv.QUOTE_NONNUMERIC)
    for row in rescaled_raster:
        writer.writerow(row)
