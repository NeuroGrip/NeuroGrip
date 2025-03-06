import rospy
from geometry_msgs.msg import Pose
import numpy as np
from autolab_core import RigidTransform
from frankapy import FrankaArm

class RobotState:
    RESET = 0
    MOVE_TO_PICKUP = 1
    PICKUP= 2
    MOVE_TO_DROPOFF = 3
    DROPOFF = 4

class FrankaMoveIt:
    def __init__(self):
        self.franka_arm = FrankaArm()
        self.fsm = RobotState.RESET
        
    def move_to_reset_position(self):
        # Reset position on top of pickup grid on the table
        reset_pose = RigidTransform(rotation=np.array(
                                    [[ 0.99981387, -0.01266928, 0.01387308],
                                     [-0.01286038, -0.99981281, 0.01377354],
                                     [0.01369598, -0.01394939, -0.9998089 ]]),
                                    translation=np.array([0.57575525, 0.32240383, 0.36945362]),
                                    from_frame='franka_tool', to_frame='world')

        self.move_arm(reset_pose)
        self.franka_arm.open_gripper()
        
    def move_to_pickup_position(self, x, y):
        # Move to 5cm above the object
        pose = RigidTransform(rotation=np.array(
                                    [[ 0.99981387, -0.01266928, 0.01387308],
                                     [-0.01286038, -0.99981281, 0.01377354],
                                     [0.01369598, -0.01394939, -0.9998089 ]]),
                                    translation=np.array([x, y, 0.1]),
                                    from_frame='franka_tool', to_frame='world')
        
        self.move_arm(pose)
        self.franka_arm.open_gripper()
    
    def pickup(self):
        # Pick up the object and return to the reset position
        pass
    
    def move_to_dropoff_position(self):
        # Move to 5cm in front of the dropoff location
        # {0, 1, 2, 3} corresponds to {top-left, top-right, bottom-left, bottom-right} respectively
        
        # TODO: If the dropoff location is taken, return the item to the rejected items bin
        
        pass
    
    def dropoff(self):
        # Drop off the object and return to the reset position
        pass

    def move_arm(self, pose):
        self.franka_arm.goto_pose(pose)
        
        
if __name__ == "__main__":

    fa = FrankaMoveIt()
    rate = rospy.Rate(10)

    while not rospy.is_shutdown():
        fa.main()
        rate.sleep()