"""Sensor object - Camera"""
import timeit
from sensob import Sensob
from imager2 import Imager
from PIL import Image
from camera_test import CameraTest


class SensobCamera(Sensob):

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
        """Returns how many red-pixels there are in the current image (in percentage)"""
        self.imager.get_image_dims()
        total_pixels = int(self.imager.xmax) * int(self.imager.ymax)
        red_pixels = 0
        for x in range(int(self.imager.xmax)):
            for y in range(int(self.imager.ymax)):
                #print("x = " + str(x) + " y = " + str(y))
                r, g, b = self.imager.get_pixel(x, y)
                if r > 140 and g < 120 and b < 120:
                    red_pixels += 1
        return red_pixels/total_pixels

    def get_pixel(self, x, y):
        return self.image.getpixel((x, y))

if __name__ == '__main__':
    camera_test = CameraTest("el-matador.png")
    imager = Imager()
    sensob_camera = SensobCamera(camera_test, imager)
    sensob_camera.update_image()
    start = timeit.timeit()
    print(sensob_camera.calculate_value())
    end = timeit.timeit()
    print(end-start)
