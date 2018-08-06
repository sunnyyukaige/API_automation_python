from configparser import ConfigParser
import os
import sys

class Config(object):
    instance = None

    def get_instance(self):
        if Config.instance is None:
            Config.instance = ConfigParser()
            return Config.instance
        else:
            return Config.instance



    def __init__(self, environment='qa'):
        self.config=self.get_instance()
        if (environment == 'qa'):
            self.cf = self.load_config_file()
        elif (environment == 'staging'):
            self.cf = self.load_staging_config_file()
        else:
            self.cf = self.load_staging_sg_config_file()

    def get_property(self, name):
        return self.cf.get("configuration", name)

    def load_config_file(self):
        config_file = self.get_relative_path("Config", "Configs.ini")
        self.config.read(config_file)
        return self.config

    def load_staging_config_file(self):
        config_file = self.get_relative_path("Config", "Configs_staging.ini")
        self.config.read(config_file)
        return self.config

    def load_staging_sg_config_file(self):
        config_file = self.get_relative_path("Config", "Configs_staging_sg.ini")
        self.config.read(config_file)
        return self.config

    def get_relative_path(self, path, file_name):
        prepath =os.path.dirname(sys.path[0])

        return os.path.join(prepath, path, file_name)
