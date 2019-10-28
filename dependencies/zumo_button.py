'''keithd'''

import wiringpi as wp


class ZumoButton():
    '''Wrapper class for zumo push button'''

    def __init__(self):
        self.wpi = wp

    def setup(self):
        '''Sets up the necessary settings for the push button'''
        self.wpi.wiringPiSetupGpio()
        self.wpi.pinMode(22, 0)
        self.wpi.pullUpDnControl(22, 2)


    def wait_for_press(self):
        '''Runs an infinite loop until the push button is pressed'''
        read_val = self.wpi.digitalRead(22)
        while read_val:
            read_val = self.wpi.digitalRead(22)
        print("Button pressed!!")
