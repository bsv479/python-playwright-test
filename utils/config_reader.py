import configparser


def read_config(section, key):
    config = configparser.ConfigParser(interpolation=configparser.ExtendedInterpolation())
    config.read('config/test_config.ini')
    return config[section][key]
