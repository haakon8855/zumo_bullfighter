'''plab2_gruppe20'''

from behaviour import Behaviour
import math


class AvoidWall(Behaviour):
    '''Creates motor recommendation to prevent the robot from running into a wall'''

    def __init__(self, ultraSonic):
        super().__init__()
        self.priority = 5   # May change
        self.match_degree = 0
        self.ultrasonic = ultraSonic

    def update(self):
        """Reads from sensors and gives a MR (Motor recommendation)"""
        self.sense_and_act()

    def sense_and_act(self):
        distance = self.ultrasonic.get_value()
        self.match_degree = 1/(math.exp(distance))
        self.update_weight(self.priority, self.match_degree)
        self.update_mr("B", 50)
