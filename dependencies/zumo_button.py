__author__ = 'keithd'
import wiringpi as wp

class ZumoButton():
    '''Wrapper class for zumo push button'''

    def __init__(self):
        wp.wiringPiSetupGpio()
        wp.pinMode(22, 0)
        wp.pullUpDnControl(22, 2)

    def wait_for_press(self):
        '''Runs an infinite loop until the push button is pressed'''
        read_val = wp.digitalRead(22)
        while read_val:
            read_val = wp.digitalRead(22)
        print("Button pressed!!")
