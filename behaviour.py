'''plab2_gruppe20'''
from math import exp


class Behaviour:
    '''Behaviour class for recommending actuator action'''

    def __init__(self):
        # TODO self.bbcon = None
        # TODO self.sensob_list = []
        # TODO self.sensob_list.append(sensob)
        self.motor_recommendations = []  # [Direction, speed%, Halt], [Turn_direction, degrees, halt]
        self.active_flag = True
        self.halt_request = False
        self.weight = 0

    def consider_deactivation(self):
        pass

    def consider_activation(self):
        pass

    def update(self):
        """Main method in behaviour. If active, it reads from sensors and gives a MR (Motor recommendation)"""
        if self.active_flag:
            self.consider_deactivation()
        else:
            self.consider_activation()

        if self.active_flag:
            self.sense_and_act()

    def sense_and_act(self):
        """Reads from sensor, and sets new MR and weight"""
        pass

    def update_weight(self, priority, match_degree):
        self.weight = priority*match_degree

    def get_weight(self):
        return self.weight

    def get_mr(self):
        return self.motor_recommendations

    def update_mr(self, direction, speed):
        self.motor_recommendations = [direction, speed, self.halt_request]


class AvoidWall(Behaviour):

    def __init__(self):
        super().__init__()
        self.priority = 5   #May change
        self.match_degree = 0

    def consider_deactivation(self):
        pass

    def consider_activation(self):
        pass

    def update(self):
        """Reads from sensors and gives a MR (Motor recommendation)"""
        self.sense_and_act()

    def sense_and_act(self):
        # TODO x = sensor-readings (distance to wall/object)
        self.match_degree = 1/(exp(x))
        self.update_weight(self.priority, self.match_degree)
        self.update_mr("B", 50)


class AvoidLineCrossing(Behaviour):

    def __init__(self):
        super().__init__()
        self.priority = 3   #May change
        self.match_degree = 0

    def sense_and_act(self):
        # TODO check if robot is on line
        self.match_degree = 1
        self.update_weight(self.priority, self.match_degree)
        self.update_mr("R", 180)

    def update(self):
        """Reads from sensors and gives a MR (Motor recommendation)"""
        self.sense_and_act()


class FollowRed(Behaviour):

    def __init__(self):
        super().__init__()
        self.priority = 7  # May change
        self.match_degree = 0

    def sense_and_act(self):
        # TODO x = sensor-readings (distance to wall/object)
        # TODO get information about where it is red
        self.match_degree = 1
        self.update_weight(self.priority, self.match_degree)
        self.update_mr("R", 180)
