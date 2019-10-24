'''plab2_gruppe20'''


class Behaviour():
    '''Behaviour class for recommending actuator action'''

    def __init__(self, priority):
        pass
        #TODO self.bbcon = None
        #TODO self.sensob_list = []
        #TODO self.sensob_list.append(sensob)
        self.motor_recmmendations = [] # [Direction, speed%], [Turn_direction, degrees]
        self.active_flag = True
        self.halt_request = False
        self.priority = priority


