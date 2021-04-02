'''
    Formatter
'''

import json
# pylint: disable=E0401
from Components.manifest_manager import ManifestManager

class Formatter:
    '''Formater Class'''
    def __init__(self):
        '''Constructor'''
        self.manifest_manager = ManifestManager()
        self.measurements_table_path = self.manifest_manager.get_from_manifest("Measurements_Table")
        self.format_header = self.manifest_manager.get_from_manifest("Format_Header")
        self.measurements_table = self.__get_measurements_table(self.measurements_table_path)

    def format_to_influx(self, processed_dict):
        '''Returns a list with formated messages'''
        return self.__generate_list(processed_dict)

    def __generate_list(self, inDict):
        '''Fills the list with formated messages'''
        format_list = []
        format_list.append(self.__build_message(inDict))
        return format_list

    def __build_message(self, inDict):
        '''Fills a message with the Influx format'''
        message = self.format_header
        for key in inDict.keys():
            message = self.__add_measurement(key, message, inDict)
        return message[:-1]

    def __add_measurement(self, key, partial_message, inDict):
        '''Adds a new measurement to a influx message'''
        return partial_message + "{}={},".format(self.__get_measurement_type(key), inDict[key])

    def __get_measurement_type(self, abbreviation):
        '''Returns the equivalence for a given abbreviation'''
        return self.measurements_table[abbreviation]

    @staticmethod
    def __get_measurements_table(measurements_table_path):
        with open("../Resources/{}".format(measurements_table_path),'r') as measurements_table:
            return json.load(measurements_table)
