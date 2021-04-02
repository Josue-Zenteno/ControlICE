'''
    XML Manager
'''

import xmltodict

class XMLManager:
    '''XML Manager Class'''
    @staticmethod
    def xlm2dict (inXML):
        '''Returns a Dictionary with the 
           information of a given XML'''
        return xmltodict.parse(inXML)
