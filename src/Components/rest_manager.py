'''
    REST Manager
'''

import requests

class RESTManager:
    '''REST Manager Class
       Client for Wibee API'''
    @staticmethod
    def get_request(url):
        '''Makes an HTTP GET Request to a given URL'''
        response = requests.get(url)

        if response.status_code != 200:
            print("Status code != 200")

        return response.content
