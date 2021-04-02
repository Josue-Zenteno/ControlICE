'''
    ControlICE Application
'''
from art import tprint
from Components.manager import Manager

class ControlICE:
    def __init__(self):
        '''Constructor'''
        self.manager = Manager()
        self.__print_app_welcome()

    def launch_controlICE(self):
        '''Launches the application'''
        self.manager.launch_app()

    @staticmethod
    def __print_app_welcome():
        '''Prints App welcome message'''
        print("\n\n")
        tprint("ControlICE",font = "larry3d")
        print("CP.SL:\n- Josue Carlos Zenteno Yave"
                    "\n- Sergio Silvestre Pavon"
                    "\n- Alejandro Riquelme Castaño"
                    "\n- Javier Santana Delgado"
                    "\n- Julio Sanchez de las Heras Martin Consuegra\n")

try:
    controlICE = ControlICE()
    controlICE.launch_controlICE()
except KeyboardInterrupt:
    pass
