'''plab2_gruppe20'''

from behaviour import Behaviour


class AvoidLineCrossing(Behaviour):
    '''Creates motor recommendation to prevent the robot from crossing the line'''

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
