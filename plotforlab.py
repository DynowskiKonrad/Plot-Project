import numpy as np
import matplotlib.pyplot as pplt
from scipy.stats import linregress as linreg
from configurations import getconfig


def least_squares_plot(configs):
    """
    This function is plotting a points with its errors on the 2D plane.
    :param configs:
    It is a dictionary containing the informations of:
        - Horizontal size of the plot
            * By default: "xsize": 16
        - Vertical size of the plot
            * By default: "ysize": 9
        - Symbol used to denote the point
            * By default: "symbol": 'x'
        - Name of input file
            * By default: "nameofinput": 'data.txt'
        - Name of y axis
            * By default: "nameofvalue": "$X$ value"
        - Name of x axis
            * By default: "nameofarg": "argument $x$"
        - Name of output file with extension
            * By default: "nameofoutput": '0'
        - If show legend:
            * By default: "showlegend": '0'

    """
    arrofdata = np.loadtxt(configs['nameofinput'])
    x = arrofdata[:, 0]
    y = arrofdata[:, 1]
    a, b, r, _, da = linreg(x, y)
    a, b = a.round(), b.round()
    basex = np.linspace(min(x), max(x), 10000)

    pplt.figure(figsize=(configs['xsize'], configs['ysize']))
    pplt.errorbar(x, y, yerr=da, marker=configs['symbol'], color=(200/255, 80/255, 80/255),
                  label=configs['nameofvalue'], ls='')
    pplt.plot(basex, basex * a + b, label="regression line, a = {0}, b = {1}".format(a, b))
    pplt.xlabel(configs['nameofarg'])
    pplt.ylabel(configs['nameofvalue'])
    pplt.tight_layout(0.1)

    if configs['showlegend'] != '0':
        leg = pplt.legend()
        leg.draggable()

    if configs['nameofoutput'] != '0':
        pplt.savefig(configs['nameofoutput'])
    else:
        pplt.show()


least_squares_plot(getconfig())
