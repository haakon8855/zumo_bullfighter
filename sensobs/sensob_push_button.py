'''plab2_gruppe20'''

from sensob import Sensob
from dependencies.zumo_button import ZumoButton


class SensobPushButton(Sensob):
    '''Sensob class for zumo push button'''

    def __init__(self):
        super().__init__()
        self.button_wrapper = ZumoButton()

    def wait_for_press(self):
        '''Calls the wrappers method of same name, runs an infinite loop until button is pressed'''
        self.button_wrapper.wait_for_press()

    def get_value(self):
        """Returns the last collected sensor value"""
        return self.value
