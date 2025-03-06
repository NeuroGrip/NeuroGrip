from dotenv import load_dotenv
from gpt_parser import Parser
import os
import matplotlib.pyplot as plt
import numpy as np

import rospy
from sensor_msgs.msg import Image

from single_image_capture import ImageCapture

from segment import Segment

from franka_control import FrankaMoveIt

from calibration import pick_up

# from autolab_core import RigidTransform

if __name__ == "__main__":
    load_dotenv()

    api_key = os.getenv("OPENAI_API_KEY")
    parser = Parser(api_key)

    seg = Segment()
    image_path = "captured_image.jpg"

    # initialize franka
    fa = FrankaMoveIt()
    rate = rospy.Rate(10)

    while not rospy.is_shutdown():
        # get input from user
        print("Please enter a command:")
        sentence = input("> ")
        parsed_result = parser.parse_sentence(sentence)
        print(parsed_result)

        # TODO: go to the photo taking position
        fa.move_to_reset_position()

        # capture image
        if not rospy.core.is_initialized():
            rospy.init_node("neurogrip", anonymous=True)
        topic_name = "/camera/color/image_raw"
        capture = ImageCapture(topic_name, image_path)

        while not capture.is_done() and not rospy.is_shutdown():
            rospy.sleep(0.1)

        # segment image
        results, center_point = seg.segment(image_path, parsed_result["object"], viz=True)
        
        print(center_point)
        
        x, y = pick_up([center_point[1], center_point[0]])
        
        print(x, y)

        # TODO: start picking!!!
        fa.move_to_pickup_position(x, y)
