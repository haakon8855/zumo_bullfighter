'''plab2_gruppe20'''

from behaviour import Behaviour


class AvoidLineCrossing(Behaviour):
    '''Creates motor recommendation to prevent the robot from crossing the line'''

    def __init__(self, bbcon, sensob_list):
        super().__init__(bbcon, sensob_list)
        self.priority = 100   #May change
        self.match_degree = 0
        self.sensor_values = []
        self.threshold = 0.6

    def sense_and_act(self):
        self.sensor_values = self.sensob_list[0].get_value()
        if (self.sensor_values[0] < self.threshold or
                self.sensor_values[1] < self.threshold or
                self.sensor_values[2] < self.threshold):
            self.update_mr("L", 150)
            self.match_degree = 1

        elif (self.sensor_values[3] < self.threshold or
              self.sensor_values[4] < self.threshold or
              self.sensor_values[5] < self.threshold): # Rar indentation, må ses på
            self.update_mr("L", 150) # Kjør til venstre
            self.match_degree = 1

        else:
            self.update_mr("F", 50) # Kjør rett fram
            self.match_degree = 0

        self.update_weight(self.priority, self.match_degree)

    def update(self):
        """Reads from sensors and gives a MR (Motor recommendation)"""
        self.sense_and_act()
