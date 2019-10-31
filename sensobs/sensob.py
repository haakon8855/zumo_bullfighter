'''plab2_gruppe20'''


class Sensob():
    '''Sensor object'''

    def __init__(self):
        self.value = None
        self.list_sensors = []

    def update(self):
        """Gets new and updated values from sensor"""

    def get_value(self):
        """Returns the last collected sensor value"""
        return self.value

    def reset(self):
        """Resets sensor values if it is needed"""
