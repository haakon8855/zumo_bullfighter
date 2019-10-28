'''plab2_gruppe20'''

from behaviour import Behaviour


class AvoidWall(Behaviour):
    '''Creates motor recommendation to prevent the robot from running into a wall'''

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
