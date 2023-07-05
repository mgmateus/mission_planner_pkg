#!/usr/bin/env python3
"""This is an example of how to do mission planning using BaseController. Do not run this module!"""
import rospy
from check_machines import check_flight, check_navigation, check_waypoints_navigation

if __name__ == "__main__":
    rospy.init_node("mission_plane_0_node")

    # Create a SMACH state machine
    height = 0.6
    target = [0.25, 0.0, 0.6]
    path = [[1.2, 0.0, height], [1.2, 0.0, 1.0], [0.0, 0.0, 1.0]]
    sm_mission = check_waypoints_navigation(height, target)
    
    # Execute SMACH plan
    outcome = sm_mission.execute()

