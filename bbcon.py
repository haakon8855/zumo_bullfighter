'''plab2_gruppe20'''

from arbitrator import Arbitrator


class BBCON():
    '''Behaviour based controller'''

    timestep = 0.5

    def __init__(self):
        self.behaviours = []
        self.active_behaviours = []
        self.inactive_behaviours = []
        self.sensobs = []
        self.motobs = []
        self.arbitrator = Arbitrator()

    def add_behaviour(self, behaviour):
        '''Adds a new behaviour to the list of behaviours'''
        if behaviour not in self.behaviours:
            self.behaviours.append(behaviour)

    def add_sensob(self, sensob):
        '''Adds a new sensob to the list of sensobs'''
        if sensob not in self.sensobs:
            self.sensobs.append(sensob)

    def activate_behaviour(self, behaviour):
        '''Sets an inactive behaviour as active'''
        if (behaviour in self.behaviours and
                behaviour not in self.active_behaviours and
                behaviour in self.inactive_behaviours):
            self.inactive_behaviours.remove(behaviour)
            self.active_behaviours.append(behaviour)

    def deactivate_behaviour(self, behaviour):
        '''Sets an active behaviour as inactive'''
        if (behaviour in self.behaviours and
                behaviour in self.active_behaviours and
                behaviour not in self.inactive_behaviours):
            self.active_behaviours.remove(behaviour)
            self.inactive_behaviours.append(behaviour)
