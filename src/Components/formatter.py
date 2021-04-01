'''
    Formatter
'''

class Formatter:
    '''Formater Class'''
    def translate_to_influx(self, inDict):
        '''Translate into influx format'''
        return self.generate_individual_list(inDict)
        #return self.unique_format(inDict)


    def unique_format(self, inDict):
        aux_list = []
        final_format = "consumo,location=ITSI"

        for i in inDict.keys():
            final_format = final_format + " {}={}".format(self.get_measurement_type(i), inDict[i])

        aux_list.append(final_format)
        return aux_list

    def generate_individual_list(self, inDict):
        final_list = []

        for i in inDict.keys():
            measurement, tag_set, field_set = self.get_format_parameters(i, inDict)
            final_list.append(self.build_format(measurement, tag_set, field_set))

        return final_list
    
    def get_format_parameters(self, key, inDict):
        measurement = self.get_measurement_type(key)
        tag_set = 'ITSI'
        field_set = inDict[key]
        return measurement, tag_set, field_set

    @staticmethod
    def build_format(measurement, tag_set, field_set):
        return "{},location={} value={}".format(measurement, tag_set, field_set)

    @staticmethod
    def get_measurement_type(abbreviation):
        '''Like a dictionary'''

        if abbreviation == 'vrmst':
            return "voltage"
        elif abbreviation == 'irmst':
            return "current"
        elif abbreviation == 'papt':
            return "apparent_power"
        elif abbreviation == 'pact':
            return "active_power"
        elif abbreviation == 'preact':
            return "reactive_power"
        elif abbreviation == 'freqt':
            return "frequency"
        elif abbreviation == 'fpott':
            return "power_factor"
        elif abbreviation == 'eact':
            return "active_energy"
        elif abbreviation == 'ereactlt':
            return "inductive_reactive_energy"
        elif abbreviation == 'ereactct':
            return "capacitive_reactive_energy"
