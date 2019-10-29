'''plab2_gruppe20'''

from math import exp

from behaviour import Behaviour


class AvoidWall(Behaviour):
    '''Creates motor recommendation to prevent the robot from running into a wall'''

    def __init__(self, bbcon, sensob_list):
        super().__init__(bbcon, sensob_list)
        self.priority = 5.5   # May change
        self.match_degree = 0
        self.ultrasonic = sensob_list[0]
        self.distance = 1000

    def sense_and_act(self):
        self.distance = self.ultrasonic.get_value()
        self.match_degree = 1/(exp(self.distance))
        self.update_weight(self.priority, self.match_degree)
        self.update_mr("BR", 30)
