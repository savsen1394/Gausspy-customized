# import necessary libraries and plotting functions

import os

from astropy.io import fits

%matplotlib inline
import matplotlib
import matplotlib.pyplot as plt
from pylab import cm

from astropy.wcs import WCS

from gausspyplus.plotting import get_points_for_colormap, shiftedColorMap


def get_cmap_rchi2(vmin, vmax):
    orig_cmap = matplotlib.cm.RdBu_r
    start, stop = get_points_for_colormap(vmin, vmax, central_val=1.)
    midpoint = (1 - vmin) / (vmax - vmin)
    return shiftedColorMap(orig_cmap, start=0., midpoint=midpoint, stop=stop)


def add_style(ax):
    ax.set_xlabel('Galactic Longitude')
    ax.set_ylabel('Galactic Latitude')


if not os.path.exists('decomposition_grs'):
    !mkdir decomposition_grs
