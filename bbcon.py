"""plab2_gruppe20"""

from time import sleep

from arbitrator import Arbitrator
from motob import Motob

from dependencies.zumo_button import ZumoButton

from avoid_line_crossing import AvoidLineCrossing
from avoid_wall import AvoidWall
from default_movement import DefaultMovement
from follow_red import FollowRed

from sensob_border_lines import SensobBorderLines
from sensob_camera import SensobCamera
from sensob_push_button import SensobPushButton
from sensob_ultrasonic import SensobUltrasonic


class BBCON:
    """Behaviour based controller"""

    timestep = 0.001

    def __init__(self):
        self.running = True
        self.behaviours = []
        self.active_behaviours = []
        self.inactive_behaviours = []
        self.sensobs = []
        self.motob = Motob()
        self.arbitrator = Arbitrator(self)
        self.zumo_btn = None
        self.setup()

    def setup(self):
        """Sets up behaviours and sensobs"""
        sensob_border_lines = SensobBorderLines()
        sensob_camera = SensobCamera()
        # sensob_push_button = SensobPushButton()
        sensob_ultrasonic = SensobUltrasonic()
        # self.zumo_btn = sensob_push_button
        self.sensobs.append(sensob_border_lines)
        self.sensobs.append(sensob_camera)
        # self.sensobs.append(sensob_push_button)
        self.sensobs.append(sensob_ultrasonic)
        self.behaviours.append(AvoidLineCrossing(self, [sensob_border_lines]))
        self.behaviours.append(AvoidWall(self, [sensob_ultrasonic]))
        self.behaviours.append(DefaultMovement(self, []))
        self.behaviours.append(FollowRed(self, [sensob_camera, sensob_ultrasonic]))
        for behaviour in self.behaviours:
            self.active_behaviours.append(behaviour)

    def add_behaviour(self, behaviour):
        """Adds a new behaviour to the list of behaviours"""
        if behaviour not in self.behaviours:
            self.behaviours.append(behaviour)

    def add_sensob(self, sensob):
        """Adds a new sensob to the list of sensobs"""
        if sensob not in self.sensobs:
            self.sensobs.append(sensob)

    def activate_behaviour(self, behaviour):
        """Sets an inactive behaviour as active"""
        if (behaviour in self.behaviours and
                behaviour not in self.active_behaviours and
                behaviour in self.inactive_behaviours):
            self.inactive_behaviours.remove(behaviour)
            self.active_behaviours.append(behaviour)

    def deactivate_behaviour(self, behaviour):
        """Sets an active behaviour as inactive"""
        if (behaviour in self.behaviours and
                behaviour in self.active_behaviours and
                behaviour not in self.inactive_behaviours):
            self.active_behaviours.remove(behaviour)
            self.inactive_behaviours.append(behaviour)

    def run_one_timestep(self):
        """Runs one timestep by updating sensors,
        behaviors, arbitrator and motors"""
        print("#####################################")
        self.update_sensobs()
        self.update_behaviours()
        motor_recommendation = self.arbitrator.choose_action()
        self.update_motob(motor_recommendation)
        sleep(self.timestep)
        self.reset_sensobs()

    def update_sensobs(self):
        """Instructs all sensobs to get value from sensors and save it."""
        for sensob in self.sensobs:
            if sensob == self.sensobs[1]:
                if self.behaviours[3].active_flag:
                    sensob.update()
            else:
                sensob.update()


    def reset_sensobs(self):
        """Instructs all sensobs to reset if it needs to"""
        for sensob in self.sensobs:
            sensob.reset()

    def update_behaviours(self):
        """Instructs all behaviours to make a motor recommendation."""
        for behaviour in self.behaviours:
            behaviour.update()

    def update_motob(self, moto_rec):
        """Updates the motobs to do the requested motor recommendation"""
        self.motob.update(moto_rec)

if __name__ == "__main__":
    Z = ZumoButton()
    Z.wait_for_press()
    BB = BBCON()
    while BB.running:
        BB.run_one_timestep()
