'''plab2_gruppe20'''


class Behaviour:
    '''Behaviour class for recommending actuator action'''

    def __init__(self, bbcon, sensob_list):
        self.bbcon = bbcon
        self.sensob_list = sensob_list
        self.motor_recommendations = []  # [Direction, speed%, Halt],
                                         # [Turn_direction, degrees, halt]
        self.active_flag = True
        self.halt_request = False
        self.weight = 0
        self.last_flag = True

    def consider_deactivation(self):
        """Contemplates if it is to deactivate itself"""

    def consider_activation(self):
        """Contemplates if it is to activate itself"""

    def update(self):
        """Main method in behaviour. If active, it reads
           from sensors and gives a MR (Motor recommendation)"""
        if self.active_flag:
            self.consider_deactivation()
        else:
            self.consider_activation()

        if self.active_flag:
            if self.last_flag:
                self.sense_and_act()
        self.last_flag = self.active_flag

    def sense_and_act(self):
        """Reads from sensor, and sets new MR and weight"""

    def update_weight(self, priority, match_degree):
        """Updates weight variable"""
        self.weight = priority*match_degree

    def get_weight(self):
        """Returns weight variable"""
        return self.weight

    def get_mr(self):
        """Returns the calculated motor recommendations"""
        return self.motor_recommendations

    def update_mr(self, direction, speed):
        """Calculates and sets motor recommendations"""
        self.motor_recommendations = [direction, speed, self.halt_request]
