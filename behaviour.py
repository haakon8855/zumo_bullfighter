'''plab2_gruppe20'''


class Behaviour:
    '''Behaviour class for recommending actuator action'''

    def __init__(self):
        # TODO self.bbcon = None
        # TODO self.sensob_list = []
        # TODO self.sensob_list.append(sensob)
        self.motor_recommendations = []  # [Direction, speed%], [Turn_direction, degrees]
        self.active_flag = True
        self.halt_request = False

    def consider_deactivation(self):
        pass

    def consider_activation(self):
        pass

    def update(self):
        """Main method in behaviour. If active, it reads from sencors and gives a MR (Motor recommendation)"""
        if self.active_flag:
            self.consider_deactivation()
        else:
            self.consider_activation()

        if self.active_flag:
            self.sense_and_act()

    def sense_and_act(self):
        pass


class AvoidWall(Behaviour):

    def __init__(self):
        super().__init__()
        self.priority = 5
        self.match_degree = 0
        self.weight = self.priority * self.match_degree

    def consider_deactivation(self):
        pass

    def consider_activation(self):
        pass

    def sense_and_act(self):
        pass

    def get_weight(self):
        return self.weight

    def get_mr(self):
        return self.motor_recommendations
