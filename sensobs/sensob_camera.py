"""Sensor object - Camera"""

from sensob import Sensob

from dependencies.imager2 import Imager
from dependencies.camera import Camera

#from camera_test import CameraTest
#from imager2 import Imager


class SensobCamera(Sensob):
    """Camera sensob for detecting red pixels"""

    def __init__(self):
        super().__init__()
        self.camera = Camera()
        self.image = None       # self.image is an Image object
        self.imager = Imager()
        self.value = []

    def update(self):
        """Gets new and updated values from sensor"""
        self.update_image()
        print("Sensob_camera - values of red in the image: " +
              str(self.calculate_value()))
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
            for x in range(int(int(self.imager.xmax)/3)*(side),
                           int(int(self.imager.xmax)/3)*(side+1)):
                for y in range(int(self.imager.ymax)):
                    #print("x = " + str(x) + " y = " + str(y))
                    r, g, b = self.imager.get_pixel(x, y)
                    if r > 140 and g < 120 and b < 120:
                        red_pixels += 1
            list_sides[side] = red_pixels / total_pixels
        self.value = list_sides
        return list_sides

    def get_pixel(self, x, y):
        """Returns a pixel given by x and y"""
        return self.image.getpixel((x, y))
