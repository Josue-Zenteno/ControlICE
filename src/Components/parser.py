'''
    Parser
'''

class Parser:
    '''Parser Class'''
    def parse_information(self, raw_measurements_dict):
        '''Returns a Dictionary that contains only the
           relevant information given for the sensors'''
        return self.__dump_relevant_info(raw_measurements_dict)

    @staticmethod
    def __dump_relevant_info(inDict):
        '''Dumps into a new Dictionary only the total
           measurement values (not partials) and ignores
           sensor configuration values'''
        outDict = {}
        for internal_dict in inDict['values']['variable'][18:]:
            if internal_dict['id'][-1] == 't':
                outDict[internal_dict['id']] = internal_dict['value']
        return outDict