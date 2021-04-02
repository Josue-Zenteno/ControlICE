'''
    Dispatcher
'''

import paho.mqtt.client as mqtt
# pylint: disable=E0401
from Components.manifest_manager import ManifestManager

class Dispatcher:
    '''Dispatcher Class'''
    def __init__(self):
        '''Constructor'''
        self.manifest_manager = ManifestManager()
        self.ip = self.manifest_manager.get_from_manifest("Ip")
        self.topic = self.manifest_manager.get_from_manifest("Topic")

    def dispatch(self, formatted_messages_list):
        '''Publishes all the formatted messages in the
           Consumo topic'''
        publisher = self.create_publisher()
        
        for i in formatted_messages_list:
            publisher.publish(self.topic, i)

    def create_publisher(self):
        '''Creates and binds a new Publisher'''
        publisher = mqtt.Client()
        publisher.connect(self.ip)
        return publisher
