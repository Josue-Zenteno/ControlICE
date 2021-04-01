'''
    Dispatcher
'''
import paho.mqtt.client as mqtt

class Dispatcher:
    '''Dispatcher Class'''
    def dispatch(self, inFormat):
        publisher = self.create_publisher()
        
        for i in inFormat:
            publisher.publish('Consumo', i)


    @staticmethod
    def create_publisher():
        publisher = mqtt.Client()
        publisher.connect('localhost')
        return publisher
