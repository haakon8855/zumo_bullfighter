'''plab2_gruppe20'''

from behaviour import Behaviour


class DefaultMovement(Behaviour):
    '''Default movement when nothing else matters'''

    def __init__(self):
        super().__init__()
        self.priority = 5
        self.match_degree = 1
        self.update_weight(self.priority, self.match_degree)
        self.update_mr("FR", 50)

    def update(self):
        """Gives a default motor recommendation"""
        self.sense_and_act()
