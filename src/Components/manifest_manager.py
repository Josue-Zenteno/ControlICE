'''
    Manifest Manager
'''

import json

MANIFEST_PATH = '../manifest.json'

class ManifestManager:
    @staticmethod
    def get_from_manifest(key):
        '''Returnsthe value of a given key in teh manifest.json'''
        with open(MANIFEST_PATH,'r') as manifest:
            manifest_dict = json.load(manifest)
            return manifest_dict[key]