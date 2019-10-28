'''plab2_gruppe20'''

from sensob import Sensob
from dependencies.reflectance_sensors import ReflectanceSensors


class SensobBorderLines(Sensob):
    '''Sensob class for ir-sensor to prevent driving outside boundaries'''

    def __init__(self):
        super().__init__()
        self.ir_wrapper = ReflectanceSensors()
        self.values = [0, 0, 0, 0, 0, 0]
        self.threshold = 0.1

    def update(self):
        '''Updates the values from the IR sensor array'''
        self.values = self.ir_wrapper.update()
        return self.values
        # Dette skal være i behaviour-klassen for "ikke kjør ut av banen"
        # if (values[0] < self.threshold or
        #         values[1] < self.threshold or
        #         values[2] < self.threshold):
        #     pass  # Kjør til høyre
        # elif (values[3] < self.threshold or
        #       values[4] < self.threshold or
        #       values[5] < self.threshold): # Rar indentation, må ses på
        #     pass  # Kjør til venstre
        # else:
        #     pass  # Kjør rett fram

    def get_value(self):
        '''Returns value of IR sensor arrays'''
        return self.values

    def reset(self):
        '''Resets IR sensor array'''
        self.ir_wrapper.reset()
