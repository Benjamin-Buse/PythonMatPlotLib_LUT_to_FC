import matplotlib

#create own
#cmap=matplotlib.colors.LinearSegmentedColormap.from_list(name='testmap',colors=['red','blue'],N=255)

#read existing colour tables
#cmap = matplotlib.colormaps('Spectral')
#cmap = matplotlib.colormaps['gist_earth']
cmap = matplotlib.colormaps['nipy_spectral']
cmap = matplotlib.colormaps['gist_ncar']
#list all color maps avaliable
#list(matplotlib.colormaps)

#colourtable is 0 to 1, so applying it to range of interest
norm = matplotlib.colors.Normalize(vmin=0, vmax=255)

import pandas as pd
import tkinter
import tkinter.filedialog
savelocation = tkinter.filedialog.asksaveasfilename(title="select save location")
f = open(savelocation,"a")
f.write(" False color description for MicroImage"+"\n")
f.write(" BEGIN Items"+"\n")
f.write(" Interpolate=0"+"\n")
for x in range(0,255):
    #cmap() returns rgba; [] specifies r or g or b or a; norm(x) is 0 to 255 given as 0 to 1 for color map
    r = cmap(norm(x))[0]
    g = cmap(norm(x))[1]
    b = cmap(norm(x))[2]
    #rgb are in range 0 to 1
    rgbdecimal = int(b*255) * 65536 + int(g*255) * 256 + int(r*255)
    f.write(" Item= "+str(x)+" "+str(x)+" "+str(rgbdecimal)+"\n")
f.write(" END Items")
f.close()