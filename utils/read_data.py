import configparser
import os

import yaml

ini_path = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), "config", "setting.ini")
data_path = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), "data", "data.yaml")

class FileRead:
    def __init__(self):
        self.data_path = data_path
        self.ini_path = ini_path

    def read_ini(self):
        config = configparser.ConfigParser()
        config.read(self.ini_path, encoding='utf-8')
        return config


    def read_data(self):
        f = open(self.data_path, encoding='utf-8')
        data = yaml.safe_load(f)
        return data


base_data = FileRead()
