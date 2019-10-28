"""Sensor-object: Ultrasonic"""
from dependencies.ultrasonic import Ultrasonic
from sensob import Sensob


class SensobUltrasonic(Sensob):
    """Class SensobUltrasonic"""

    def __init__(self):
        super().__init__()
        self.ultra_sonic = Ultrasonic()

    def update(self):
        self.ultra_sonic.update()
        self.value = self.ultra_sonic.get_value() / 100

    def get_value(self):
        return self.value
