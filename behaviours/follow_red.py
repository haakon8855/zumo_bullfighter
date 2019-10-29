'''plab2_gruppe20'''

from behaviour import Behaviour


class FollowRed(Behaviour):
    """Class for following red"""

    def __init__(self, bbcon, sensob_list):
        super().__init__(bbcon, sensob_list)
        self.priority = 20  # May change
        self.match_degree = 0
        self.sensob_camera = sensob_list[0]
        self.values = []

    def update(self):
        """Reads from sensors and gives a MR (Motor recommendation)"""
        self.sense_and_act()

    def sense_and_act(self):
        values = self.sensob_camera.get_value()
        if values[0] > values[1] and values[0] > values[2]:
            self.update_mr("L", 25)
            self.match_degree = values[0]
        elif values[1] >= values[0] and values[1] >= values[2]:
            self.update_mr("F", 50)
            self.match_degree = values[1]
        elif values[2] >= values[0] and values[2] > values[1]:
            self.update_mr("R", 25)
            self.match_degree = values[2]
        self.update_weight(self.priority, self.match_degree)
