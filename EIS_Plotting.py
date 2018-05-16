##Author: Gokulanand Iyer
##Date Started: 3/31/18
##Notes: Plating experiments with EIS run in between intervals of equal charge passed. Plot of EIS curves for experiments

from pithy import *
import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import glob

#Function for Parsing and ploting EIS data from a webserver.
def parse_graph(file,name,color,point,size):
    fn = file
    tmp = pd.DataFrame(columns=['A','B'])
    with open(fn, 'r') as f:
        for line in f:
            try:
                data = line.split()
                tmp1 = data[0]
                tmp2 = data[1]
                foo = pd.DataFrame({'A':[tmp1],'B':[tmp2]})
                frames = [tmp,foo]
                tmp = pd.concat(frames)
            except Exception as E: 
                print E
    
    plt.scatter(tmp.loc[:,'A'],tmp.loc[:,'B'],s=size,marker=point,color=color,label = name)

    return



#Example of the function, parsing and plotting from drops.

###################################################

##Plating 5 microns at 50mAcm2

fils7 = glob.glob("/pithy/drops/gokul/EIS/0404/50mAcm2_voltage*")

for match in fils7:
    lab =  match[36:51]
    foo = genfromtxt(match)
    foo = foo.T
    x = foo[0]
    y = foo[1]
 
    
    plot(x,y,'.',label=lab)

    
title(r'$500 mA/cm^2$')
xlabel('$time$')
ylabel('$V$')
foo = plt.legend(loc = 'upper left',prop={'size': 12})
showme()
clf()


