from __future__ import division, unicode_literals, print_function  # for compatibility with Python 2 and 3

import matplotlib as mpl
import matplotlib.pyplot as plt

import numpy as np
import pandas as pd
from pandas import DataFrame, Series  # for convenience
import pims
import trackpy as tp

mpl.rc('figure',  figsize=(10, 5))
mpl.rc('image', cmap='gray')

frames = pims.open('/home/sagar/Documents/Data/ActiveGlasses/C1_CT212_2.64_3.18_1-1_15FPS_3HP_I500mA_UV5_1/Images/*.tif')
f = tp.locate(frames[0], 29, separation = 19, minmass = 2000)
# tp.annotate(f, frames[0], plot_style={'markersize': 1, 'marker':'+'});
# tp.subpx_bias(f)
# plt.show()
# exit()
f = tp.batch(frames[:], 29, separation = 19, minmass=2000);
data = f.to_numpy()
np.save("ff_UV5_1",data)
print(data)
