from Components.rest_manager import RESTManager
from Components.xml_manager import XMLManager
from Components.parser import Parser
from Components.formatter import Formatter
from Components.dispatcher import Dispatcher

ITSI_PASILLO_URL = 'http://172.24.106.5/services/user/values.xml?id=ITSI+Pasillo'
ITSI_CITISIM_URL = 'http://172.24.106.6/services/user/values.xml?id=ITSI+Citisim'

rest_manager = RESTManager()
xml_manager = XMLManager()
parser = Parser()
formatter = Formatter()
dispatcher = Dispatcher()

while True:
    xml = rest_manager.get_request(ITSI_PASILLO_URL)
    dict = xml_manager.xlm2dict(xml)
    parsed_dict = parser.get_value_list(dict)
    _format = formatter.translate_to_influx(parsed_dict)
    dispatcher.dispatch(_format)

