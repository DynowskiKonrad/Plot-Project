def getconfig(configfilename="config.txt"):
    """
    The configs have default values of size and symbol
    If in config file one value is present, then it added on right place in configuration dict
    :param configfilename:
        - Denotes name of configuration file used to determine size of plot and symbols on it
    :return:
        - Returns dictionary compatible with the plotting function
    """
    configs ={
        "xsize": 16,
        "ysize": 9,
        "symbol": 'x',
        "nameofinput": 'data.txt',
        "nameofvalue": 'Wavelength $\lambda$[nm]',
        "nameofarg": "argument $x$",
        "nameofoutput": '0',
        "showlegend": '0'
    }
    with open(configfilename, 'r') as f:
        for line in f.readlines():
            x, y = line.split(' ')
            if x == "xsize" or x == "ysize":
                configs[x] = float(y)
            elif x == "symbol":
                configs[x] = y
    return configs