import rospy
import smach
from flight_pkg.base_controller import BaseController


class Armed(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes = ['armed', 'wait_for_auto_mode'], output_keys = ['armed', 'mode'])
        rospy.Subscriber("/mavros/state", State, self._state_callback)
        
        self.__armed = False  
        self.__mode = 'STABILIZE' 
        self.__base_controller = BaseController()   
    
    def _state_callback(self, msg):
        self.__armed = msg.armed
        self.__mode = msg.mode

    def execute(self, status):
        if self.__armed:
            status.armed = self.__armed
            status.mode = self.__mode
            return 'armed'
        return 'wait_for_auto_mode' 


class TakeOff(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes = ['takeoff', 'wait_for_auto_mode'], input_keys = ['armed', 'mode'])
        self.__base_controller = BaseController()   

    def execute(self, status):
        if status.armed and status.mode != 'STABILIZE':
            self.__base_controller.takeoff()
            return 'takeoff'
        return  'wait_for_auto_mode'

  
