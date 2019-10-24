"""plab2_gruppe20"""

from dependencies.motors import Motors
import time as t


class Motob:
    """Motor object"""

    def __init__(self):
        """append the motors in motors"""
        self.motor1 = Motors()
        self.motors = []  # liste over motorer objektet styrer
        self.value = []  # most recent motor recommendation eks ["L", 40] eller ["F", 50]
        self.motors.append(self.motor1)

    def update(self, motor_recommendation):
        """recives a motor recommendation and opperatiolaze"""
        self.value = motor_recommendation
        self.operationalize(motor_recommendation)

    def operationalize(self, motor_recommendation):
        """execute the motor recommendation"""
        robot_dir = motor_recommendation[0]
        motor_value = motor_recommendation[1]
        if robot_dir not in "LRFBS":
            raise Exception("Må være S L R F eller B")
        if robot_dir == "F":
            print("in F")
            self.motor1.forward(motor_value/100, 2)
           # speed_list = [motor_value/100, motor_value/100]
           # self.motor1.set_value(speed_list)  # tester direkte med motor1
        elif robot_dir == "B":
            speed_prosentage = -motor_value/100
            speed_list = [speed_prosentage, speed_prosentage]
            self.motors[0].set_value(speed_list)
        elif robot_dir == "R":
            speed_prosentage_left = motor_value/360  # dette blir feil men bruker midlertidig
            speed_prosentage_right = -motor_value/360
            speed_list = [speed_prosentage_left, speed_prosentage_right]
            self.motors[0].set_value(speed_list)
        elif robot_dir == "L":
            speed_prosentage_left = -motor_value/360
            speed_prosentage_right = motor_value/360
            speed_list = [speed_prosentage_left, speed_prosentage_right]
            self.motors[0].set_value(speed_list)
        elif robot_dir == "S":
            self.motors[0].stop()
        else:
            print("why dis no work")



if __name__ == '__main__':
    testobj = Motob()
    rec = ["F", 50]
    rec2 = ["B", 50]
    rec3 = ["R", 180]
    rec4 = ["L", 180]
    rec5 = ["S", 0]
    testobj.update(rec)
    print("jepp")
    t.sleep(1)
    print("jepp")
    testobj.update(rec2)
    print("jepp")
    t.sleep(1)
    testobj.update(rec3)
    print("jepp")
    t.sleep(1)
    testobj.update(rec4)
    print("jepp")
    t.sleep(1)
    testobj.update(rec5)
    print("jepp end")








