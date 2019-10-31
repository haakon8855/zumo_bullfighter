"""plab2_gruppe20"""


class Arbitrator():
    """Arbitrator class used to choose actuator"""

    def __init__(self, BBCON):
        self.bbcon = BBCON

    def choose_action(self):
        """Chooses the action with the highest priority"""
        mr_list = []
        best_weight = 0
        best_index = 0
        print("-------------------")
        for i, behaviour in enumerate(self.bbcon.active_behaviours):
            weight = behaviour.get_weight()
            moto_rec = behaviour.get_mr()
            print(i, weight, moto_rec)
            mr_list.append(tuple((weight, moto_rec)))
            if weight > best_weight:
                best_weight = weight
                best_index = i
        print("-------------------")

        action = self.bbcon.active_behaviours[best_index].get_mr()
        print("Chose: ", action)
        action = self.strip_last_elem(action)
        return action

    @staticmethod
    def strip_last_elem(in_list):
        """Removes the last element in a 3-element list"""
        return in_list[:2]
