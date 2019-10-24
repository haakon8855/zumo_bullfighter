from PIL import Image

class CameraTest:

    def __init__(self, image_path):
        self.image = Image.open(image_path)

    def update(self):
        return self.image.convert("RGB")

if __name__ == '__main__':
    a = CameraTest("el-matador.png")
    print(a.update())