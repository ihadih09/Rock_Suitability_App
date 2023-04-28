# -*- coding: utf-8 -*-
"""
Created on Fri Apr 28 17:40:21 2023

@author: gy20ibs
"""

import numpy as np


def weight_rasters(data, factors):
    weighted_data = []
    for i in range(3):
        weighted_raster = np.multiply(data[i], factors[i])
        weighted_data.append(weighted_raster)
    sum_rasters = np.sum(weighted_data, axis=0)
    min_val = np.min(sum_rasters)
    max_val = np.max(sum_rasters)
    rescaled_raster = (sum_rasters - min_val) / (max_val - min_val) * 255
    return rescaled_raster