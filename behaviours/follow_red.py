'''plab2_gruppe20'''

from behaviour import Behaviour


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
