"""Sensor-object: Ultrasonic"""

from dependencies.ultrasonic import Ultrasonic
from sensobs.sensob import Sensob


class SensobUltrasonic(Sensob):
    """Class SensobUltrasonic"""

    def __init__(self):
        super().__init__()
        self.ultra_sonic = Ultrasonic()
        self.value = 0

    def update(self):
        """Gets new and updated values from sensor"""
        self.ultra_sonic.update()
        self.value = self.ultra_sonic.get_value() / 100
        print("Sensob_ultrasonic - distance: " + str(self.value))

    def get_value(self):
        """Returns the last collected sensor value"""
        return self.value
