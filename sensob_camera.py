"""Sensor object - Camera"""
from sensob import Sensob
from imager2 import Imager


class SensobCamera(Sensob):

    def __init__(self, camera):
        super.__init__()
        self.camera = camera

    def update(self):
        """Updates the value, which is the current image"""
        self.value = self.camera.update()

    def sees_red(self):
        """Returns how many red-pixels there are in the current image (in percentage)"""

