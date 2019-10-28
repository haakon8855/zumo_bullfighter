"""Sensor object - Camera"""

from sensob import Sensob

from dependencies.imager2 import Imager
from sensobs.camera import Camera

#from camera_test import CameraTest
#from imager2 import Imager

class SensobCamera(Sensob):
    """Camera sensob for detecting red pixels"""

    def __init__(self, camera, imager):
        super().__init__()
        self.camera = camera
        self.image = None       # self.image is an Image object
        self.imager = imager

    def update(self):
        self.update_image()
        return self.calculate_value()


    def update_image(self):
        """Updates the value, which is the current image"""
        self.image = self.camera.update()
        self.imager.set_image(self.image)

    def calculate_value(self):
        """Returns how many red-pixels there are in the current image (in percent)"""
        self.imager.get_image_dims()
        total_pixels = int(self.imager.xmax) * int(self.imager.ymax) / 3
        list_sides = [0, 0, 0]
        for side in range(3):
            red_pixels = 0
            for x in range(int(int(self.imager.xmax)/3)*(side), int(int(self.imager.xmax)/3)*(side+1)):
                for y in range(int(self.imager.ymax)):
                    #print("x = " + str(x) + " y = " + str(y))
                    r, g, b = self.imager.get_pixel(x, y)
                    if r > 140 and g < 120 and b < 120:
                        red_pixels += 1
            list_sides[side] = red_pixels / total_pixels
        return list_sides

    def get_pixel(self, x, y):
        return self.image.getpixel((x, y))
