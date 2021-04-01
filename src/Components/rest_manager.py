'''
    REST Manager that acts as a client for Wibee API
'''

import requests

class RESTManager:
    '''REST Manager Class'''
    @staticmethod
    def get_request(url):
        '''HTTP GET Request'''
        response = requests.get(url)

        if response.status_code != 200:
            print("Status code != 200")

        return response.content
