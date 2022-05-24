# MT matrix format:
    # 1 row per bead per frame, sorted by frame number then x position (roughly)
    # columns:
    # 1:2 - X and Y positions (in pixels)
    # 3   - Integrated intensity(mass)
    # 4   - Rg squared of feature
    # 5   - eccentricity
    # 6   - frame #
    # 7   - time of frame
#dataframe format used in trackpy    
# df = pd.DataFrame(data, columns = ['y', 'x', 'mass', 'size', 'ecc', signal , raw_mass, 'ep', 'frame'])     
        
import warnings
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.pyplot import plot, draw, show
from pandas import DataFrame, Series
import pims
import trackpy as tp
import time
import threading

ps  = 25
dispDistance = (ps+1)/2                 # Distance a particle is allowed to move between 2 consecutive frames 

if __name__ == "__main__":

    fname  = '/home/sagar/Documents/processedData/activeGlasses/features/UV5_1/brightField/featuresUV5_1.npy'
    data = np.load(fname)
    data1 = data
    
    # Last frame - staring frame + 1
    # Be careful about which column of the data contains frame information.    
    goodEnough = 100
    totalFrames = int(data[:,2][len(data[:,2])-1] - data[:,2][0] + 1)

    print("Starting linking particles with ps = ",ps," goodenough = ", goodEnough, "Total Frames = ", totalFrames)

    for i in range(0, (totalFrames-10)):
        data = data1
        data = data[np.where(data[:,2] <= int(goodEnough)*(i+1))]
        data =  data[np.where(data[:,2] > int(goodEnough)*i)]


        df = pd.DataFrame({'y':data[:,1], 'x':data[:,0],'frame':data[:,2]})

        t = tp.link(df, dispDistance)
        t1 = tp.filter_stubs(t, goodEnough)
        
        traj = tp.compute_drift(t1)
        t2 = tp.subtract_drift(t1,traj)


        column0 = t2['x'].tolist()
        column1 = t2['y'].tolist()  
        column2 = t2['frame'].tolist()
        column3 = t2['particle'].tolist()
        
        finalData = [column0, column1, column2, column3]    
        finalData = np.array(finalData)

        finalData = np.transpose(finalData)
        np.save('100frames/linkedData'+str(i), finalData)
