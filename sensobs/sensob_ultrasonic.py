from dependencies.ultrasonic import Ultrasonic
from sensob import Sensob

class SensobUltrasonic(Sensob):

    def __init__(self, ultraSonic):
        super().__init__()
        self.ultraSonic = ultraSonic

    def update(self):
        self.ultraSonic.update()
        self.value = self.ultraSonic.get_value() / 100

    def get_value(self):
        return self.value

if __name__ == '__main__':
    ultrasonic = Ultrasonic()
    sensobultra = SensobUltrasonic(ultrasonic)
    while True:
        sensobultra.update()
        print(sensobultra.get_value())
