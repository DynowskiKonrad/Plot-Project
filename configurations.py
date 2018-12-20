import yaml


def getconfig(configfilename="config.yml"):
    """
    The configs have default values of size and symbol
    If in config file one value is present, then it added on right place in configuration dict
    :param configfilename:
        - Denotes name of configuration file used to determine size of plot and symbols on it
    :return:
        - Returns dictionary compatible with the plotting function
    """
    with open(configfilename, 'r') as f:
        configs = yaml.load(f)
    return configs
