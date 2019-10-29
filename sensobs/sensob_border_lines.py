'''plab2_gruppe20'''

from sensob import Sensob
from dependencies.reflectance_sensors import ReflectanceSensors


class SensobBorderLines(Sensob):
    '''Sensob class for ir-sensor to prevent driving outside boundaries'''

    def __init__(self):
        super().__init__()
        self.ir_wrapper = ReflectanceSensors(False, 400, 3000)
        self.values = [0, 0, 0, 0, 0, 0]
        self.threshold = 0.1

    def update(self):
        '''Updates the values from the IR sensor array'''
        self.values = self.ir_wrapper.update()
        print("IR-sensors - array values: " + str(self.values))
        return self.values

    def get_value(self):
        '''Returns value of IR sensor arrays'''
        return self.values

    def reset(self):
        '''Resets IR sensor array'''
        self.ir_wrapper.reset()
