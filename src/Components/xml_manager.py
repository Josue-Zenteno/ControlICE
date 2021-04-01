'''
    XML Manager
'''

import xmltodict

class XMLManager:
    '''XML Manager Class'''
    @staticmethod
    def xlm2dict (xml):
        return xmltodict.parse(xml)

