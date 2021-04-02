'''
    Manager
'''
import json
# pylint: disable=E0401
from Components.rest_manager import RESTManager
from Components.xml_manager import XMLManager
from Components.parser import Parser
from Components.formatter import Formatter
from Components.dispatcher import Dispatcher
from Components.manifest_manager import ManifestManager
from time import sleep


class Manager:
    def __init__(self):
        '''Constructor'''
        self.manifest_manager = ManifestManager()
        self.sensors_url = self.manifest_manager.get_from_manifest("Sensors_URL")
        self.rest_manager = RESTManager()
        self.xml_manager = XMLManager()
        self.parser = Parser()
        self.formatter = Formatter()
        self.dispatcher = Dispatcher()
        
    
    def launch_app (self):
        '''Controls the workflow'''
        while True:
            xml = self.rest_manager.get_request(self.get_url("ITSI_Pasillo"))
            dict = self.xml_manager.xlm2dict(xml)
            parsed_dict = self.parser.parse_information(dict)
            _format = self.formatter.format_to_influx(parsed_dict)
            self.dispatcher.dispatch(_format)
            sleep(10)

    def get_url(self, device_name):
        '''Returns the URL for a given sensor'''
        return self.sensors_url[device_name]

