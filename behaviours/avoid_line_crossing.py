"""plab2_gruppe20"""

from behaviour import Behaviour


class AvoidLineCrossing(Behaviour):
    """Creates motor recommendation to prevent the robot from crossing the line"""

    def __init__(self, bbcon, sensob_list):
        super().__init__(bbcon, sensob_list)
        self.priority = 500   #May change
        self.match_degree = 0.01002
        self.sensor_values = []
        self.threshold = 0.6
        self.rotation = False
        self.rotate_left = True

    def sense_and_act(self):
        """Reads from sensor, and sets new MR and weight"""
        self.sensor_values = self.sensob_list[0].get_value()
        if not self.rotation:
            if (self.sensor_values[0] < self.threshold or
                    self.sensor_values[1] < self.threshold or
                    self.sensor_values[2] < self.threshold):
                self.update_mr("B", 35)
                self.match_degree = 0.01002
                self.rotation = True
                self.rotate_left = False
            elif (self.sensor_values[3] < self.threshold or
                  self.sensor_values[4] < self.threshold or
                  self.sensor_values[5] < self.threshold): # Rar indentation, må ses på
                self.update_mr("B", 35)
                self.match_degree = 0.01002
                self.rotation = True
                self.rotate_left = True
            else:
                self.update_mr("F", 50) # Kjør rett fram
                self.match_degree = 0
        else:
            if not self.rotate_left:
                self.update_mr("R", 100)
                self.match_degree = 1
                self.rotation = False
            else:
                self.update_mr("L", 100)
                self.match_degree = 1
                self.rotation = False

        self.update_weight(self.priority, self.match_degree)
