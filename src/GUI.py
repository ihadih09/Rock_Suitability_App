# -*- coding: utf-8 -*-
"""
Created on Thu May  4 16:29:07 2023

@author: gy20ibs
"""
#Imported modules
import matplotlib #imports the module matplotlib 
matplotlib.use('TkAgg') #sets the backend of matplotlib to use TkAgg
import matplotlib.pyplot as plt #imports specific submodules from matplotlib
import tkinter as tk #imports the module tkinter and renames it as tk
import tkinter.ttk as ttk #imports specific submodules from tkinter and renames them as ttk
import csv #imports the module csv
import my_modules.io as io #imports the module io from the package my_modules and renames it as io
import my_modules.geometry as geometry #imports the module geometry from the package my_modules and renames it as geometry
import imageio #imports the module imageio
import os #imports the module os
import doctest #imports the module doctest


def plot(g, p, t):
    """
    Redraws the canvas.
    Parameters
    ----------
    g : float
        Weight of geology raster.
    p : float
        Weight of population raster.
    t : float
        Weight of transport raster.
    
    Returns
    -------
    None.
    """
    #global p0
    #if p0 != p:
    figure = plt.figure(0)
    figure.clear()
    
    #Calculate weighted raster
    weighted_rasters = geometry.weight_raster(g, p, t, 
                                              n_rows,n_cols,
                                              geology,population,transport)
    #print(weighted_rasters)
    #plt.imshow(weighted_rasters)
    #plt.show()

    #Rescale the raster to 0-255 range
    rescaled_raster = rescale(0, 255, weighted_rasters)
    #Plot the rescaled raster
    plt.imshow(rescaled_raster)
    plt.show()
    #p0 = p
    #Draw the plot on the canvas
    canvas.draw()
    
    #Export the rescaled raster as a text file
    export_text(rescaled_raster)
    

def exiting():
    # """
    # Exit the program.
    # """
    # root.quit()
    # root.destroy()
    """
    Exit the program.
    """
    root.quit()
    try:
        root.destroy()
    except Exception:
        # Prevents reporting of a harmless Tcl error message:
        # "TclError: can't invoke "destroy" command: application has been destroyed"
        pass

def export_text(output):
    """
    Export the given output to a text file.

    Parameters
    ----------
    output : list
        The list of data to be exported.

    Returns
    -------
    None.

    """
     #Calling the write data function from io
    io.write_data('../data/output/mce_result.txt', output)
    
def export_image():
    """
    Exports images of the result and saves it to the output/images directory.
    """
    #Create directory to write images to if none exists.
    try:
        os.makedirs('../data/output/images/')
    except FileExistsError:
        print("path exists")
    # For storing images
    global ite
    ite = 1
    images = []
    #Set filename and save image
    filename = '../data/output/images/mce_result ' + str(ite) + '.png'
    plt.savefig(filename)
    plt.show()
    plt.close()
    images.append(imageio.imread(filename))
    
def update(x):
    """
    Updates scale_label and canvas.

    Parameters
    ----------
    x : str.
        Number.

    Returns
    -------
    None.

    """
    #print(x)
    #print(type(x))
    #print(scale.get())
    #print(int(float(scale.get())))
    
    #Integerise g,p,t and update the text on the labels
    g = int(float(scaleg.get()))
    scaleg_label.config(text='Set Geology=' + str(g))
    p = int(float(scalep.get()))
    scalep_label.config(text='Set Population=' + str(p))
    t = int(float(scalet.get()))
    scalet_label.config(text='Set Transport=' + str(t))
    #Update the plot with the new values for g, p, and t
    plot(g, p ,t)

  # Define function to update the output label so they add up to 10 and the total is displayed
 # def update_output():
 # g = scaleg.get()
 # p = scalep.get()
 # t = scalet.get()
 # total = g + p + t
 # output_label.config(text=f"Total: {total} (g={g}, p={p}, t={t})")
 
 # # Create the scales
 # scaleg = ttk.Scale(root, from_=0, to=10, command=update_output)
 # scaleg.pack()
 # scaleg_label = ttk.Label(root, text='Set g.')
 # scaleg_label.pack()
 
 # scalep = ttk.Scale(root, from_=0, to=10, command=update_output)
 # scalep.pack()
 # scalep_label = ttk.Label(root, text='Set p.')
 # scalep_label.pack()
 
 # scalet = ttk.Scale(root, from_=0, to=10, command=update_output)
 # scalet.pack()
 # scalet_label = ttk.Label(root, text='Set t.')
 # scalet_label.pack()
 
 # # Create the output label
 # output_label = ttk.Label(root, text='Total: 0 (g=0, p=0, t=0)')
 # output_label.pack()

# Initialise figure
#figure = matplotlib.pyplot.figure(figsize=(7, 7))
#ax = figure.add_axes([0, 0, 1, 1])

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

#execute code inside block    
if __name__ =='__main__':
   
    #Run testing
    doctest.testmod()
    
    #Read geology data
    geology, n_rows, n_cols = io.read_data('../data/input/geology.txt')
    #print(geology)
    
    #plt.imshow(geology)
    #plt.show()
    
    #Read population data
    population, n_rows, n_cols = io.read_data('../data/input/population.txt')
    #print(population)
    
    #plt.imshow(population)
    #plt.show()
    
    #Read transport data
    transport, n_rows, n_cols =io.read_data('../data/input/transport.txt')
    #print(transport)
    
    #plt.imshow(transport)
    #plt.show()
    
    # Create the tkinter window
    root = tk.Tk()
    
    #root.geometry("1000x1000")
    #create the title 
    root.title("Site Suitability Analysis")
    
    #create the label for the whole page
    label=tk.Label(root, text='MCE: Rock Aggregate Site Suitability Analysis', font=('Arial Bold', 16))
    label.pack()
    
    #create the final map frame
    frame_result = tk.Frame(root)
    frame_result.pack(side=tk.TOP,expand=1, padx=10, pady=10)
    #create label for final map frame
    result_label = tk.Label(frame_result, text='Final Map', font=('Arial', 12))    
    result_label.pack()
    #create label for legend of final map frame
    result_label1 = tk.Label(frame_result, text='Legend: Darker Green= Least Suitable, Lighter Green= Most Suitable', font=('Arial', 12))    
    result_label1.pack()
     
    #create a figure to display the final map
    figure = plt.figure(0, figsize=(7, 4))
    #create a canvas to draw the final map 
    canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(figure, master=frame_result)
    canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=1)
    
    
    #create the geology map frame
    frame_g = tk.Frame(root)
    frame_g.pack(side=tk.LEFT, padx=10, pady=10)
    #create label for geology map frame
    g_label = tk.Label(frame_g, text='Geology Map', font=('Arial', 12))    
    g_label.pack()
    
    #create a figure to display geology map
    figure = plt.figure(1, figsize=(6, 4))
    #create a canvas to draw geology map
    canvas1 = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(figure, master=frame_g)
    plt.imshow(geology)
    plt.show()
    canvas1.draw()
    
    
    #create the population map frame
    frame_p = tk.Frame(root)
    frame_p.pack(side=tk.LEFT, padx=10, pady=10)
    #create label population map frame
    p_label = tk.Label(frame_p, text='Population Map', font=('Arial', 12))    
    p_label.pack()
    #create a figure to display population map
    figure = plt.figure(2, figsize=(6, 4))
    #create a canvas to draw population map
    canvas2 = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(figure, master=frame_p)
    plt.imshow(population)
    plt.show()
    canvas2.draw()
    
    
   #create the transport map frame
    frame_t = tk.Frame(root)
    frame_t.pack(side=tk.LEFT, padx=10, pady=10)
    #create label for transport map frame
    t_label = tk.Label(frame_t, text='Transport Map', font=('Arial', 12))    
    t_label.pack()
    #create a figure to display transport map
    figure = plt.figure(3, figsize=(6, 4))
    #create a canvas to draw transport map
    canvas3 = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(figure, master=frame_t) 
    plt.imshow(transport)
    plt.show()
    canvas3.draw()
    
    # # Create a canvas to display the figure
    # canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(figure, master=root)
    # canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=1)
    
    #packing the canvas
    canvas1._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=1)
    # Create a scale
    scaleg = ttk.Scale(frame_g, from_=1, to=10, command=update)
    scaleg.pack()
    #Create a Label widget to display scale value
    scaleg_label = ttk.Label(frame_g, text='Set Geology')
    scaleg_label.pack()
    
    #packing the canvas
    canvas2._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=1)
    # Create a scale
    scalep = ttk.Scale(frame_p, from_=1, to=10, command=update)
    scalep.pack()
    #Create a Label widget to display scale value
    scalep_label = ttk.Label(frame_p, text='Set Population')
    scalep_label.pack()
    
    #packing the canvas
    canvas3._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=1)
    # Create a scale
    scalet = ttk.Scale(frame_t, from_=1, to=10, command=update)
    scalet.pack()
    #Create a Label widget to display scale value
    scalet_label = ttk.Label(frame_t, text='Set Transport')
    scalet_label.pack()
    
   

    
    
    
    # Create a Button widget and link this with the exiting function
    exit_button = ttk.Button(frame_result, text="Exit", command=exiting)
    exit_button.pack(side=tk.RIGHT)
    
    # Create a Button widget and link this with the exiting function
    save_img_button = ttk.Button(frame_result, text="Save as image", command=export_image)
    save_img_button.pack(side=tk.LEFT)
    
    # Create a Button widget and link this with the exiting function
    save_txt_button = ttk.Button(frame_result, text="Save as text file", command=export_text)
    save_txt_button.pack(side=tk.LEFT)
    
    # Exit if the window is closed.
    root.protocol('WM_DELETE_WINDOW', exiting)
    
    # Start the GUI
    root.mainloop()