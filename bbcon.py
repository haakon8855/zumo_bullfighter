'''plab2_gruppe20'''

from time import sleep

from arbitrator import Arbitrator
from motob import Motob


class BBCON():
    '''Behaviour based controller'''

    timestep = 0.5

    def __init__(self):
        self.running = True
        self.behaviours = []
        self.active_behaviours = []
        self.inactive_behaviours = []
        self.sensobs = []
        self.motob = Motob()
        self.arbitrator = Arbitrator(self)

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

    def run_one_timestep(self):
        '''Runs one timestep by updating sensors,
        behaviors, arbitrator and motors'''
        self.update_sensobs()
        self.update_behaviours()
        motor_recommendation, halt = self.arbitrator.choose_action()
        if halt:
            self.running = False
        self.update_motob(motor_recommendation)
        sleep(self.timestep)
        self.reset_sensobs()

    def update_sensobs(self):
        '''Instructs all sensobs to get value from sensors and save it.'''
        for sensob in self.sensobs:
            sensob.update()

    def reset_sensobs(self):
        '''Instructs all sensobs to reset if it needs to'''
        for sensob in self.sensobs:
            sensob.reset()

    def update_behaviours(self):
        '''Instructs all behaviours to make a motor recommendation.'''
        for behaviour in self.active_behaviours:
            behaviour.update()

    def update_motob(self, moto_rec):
        '''Updates the motobs to do the requested motor recommendation'''
        self.motob.update(moto_rec)


if __name__ == "__main__":
    BB = BBCON()
    while BB.running:
        BB.run_one_timestep()
