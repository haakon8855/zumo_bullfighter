"""plab2_gruppe20"""

from math import sqrt

from dependencies.motors import Motors


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
        for ltr in robot_dir:
            if ltr not in "LRFBS":
                raise Exception("Må være S L R F eller B")
        if robot_dir == "F":
            speed_list = [motor_value/100, motor_value/100]
            self.motors[0].set_value(speed_list)  # tester direkte med motor1
        elif robot_dir == "B":
            speed_prosentage = -motor_value/100
            speed_list = [speed_prosentage, speed_prosentage]
            self.motors[0].set_value(speed_list)
        elif robot_dir == "R":
            speed_prosentage_left = sqrt(motor_value/180)#motor_value/360
            speed_prosentage_right = -sqrt(motor_value/180)#-motor_value/360
            speed_list = [speed_prosentage_left, speed_prosentage_right]
            self.motors[0].set_value(speed_list)
        elif robot_dir == "L":
            speed_prosentage_left = -sqrt(motor_value/180)#-motor_value/360
            speed_prosentage_right = sqrt(motor_value/180)#motor_value/360
            speed_list = [speed_prosentage_left, speed_prosentage_right]
            self.motors[0].set_value(speed_list)
        elif robot_dir == "FL":
            right_motor_value = int((motor_value/100)*self.motor1.max)
            left_motor_value = int((motor_value/100)*0.5*self.motor1.max)
            self.motors[0].set_left_dir(0)
            self.motors[0].set_right_dir(0)
            self.motors[0].set_right_speed(right_motor_value)
            self.motors[0].set_left_speed(left_motor_value)
        elif robot_dir == "FR":
            right_motor_value = int((motor_value/100)*0.5*self.motor1.max)
            left_motor_value = int((motor_value/100)*self.motor1.max)
            self.motors[0].set_left_dir(0)
            self.motors[0].set_right_dir(0)
            self.motors[0].set_right_speed(right_motor_value)
            self.motors[0].set_left_speed(left_motor_value)
        elif robot_dir in ("BL", "BR"):
            self.motors[0].set_left_dir(1)
            self.motors[0].set_right_dir(1)
            if robot_dir == "BL":
                right_motor_value = int((motor_value/100)*self.motor1.max)
                left_motor_value = int((motor_value/100)*0.4*self.motor1.max)
            if robot_dir == "BR":
                right_motor_value = int((motor_value/100)*0.4*self.motor1.max)
                left_motor_value = int((motor_value/100)*self.motor1.max)
            self.motors[0].set_right_speed(right_motor_value)
            self.motors[0].set_left_speed(left_motor_value)
        elif robot_dir == "S":
            self.motors[0].stop()
