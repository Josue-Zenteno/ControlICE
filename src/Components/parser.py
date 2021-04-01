'''
    Parser
'''

class Parser:
    '''Parser Class'''
    @staticmethod
    def get_value_list(inDict):
        final_dict = {}
        for dct in inDict['values']['variable'][18:]:
            if dct['id'][-1] == 't':
                final_dict[dct['id']] = dct['value']
        
        return final_dict