#!/usr/bin/env python3
import rospy from geometry.msgs import Twist
from turtlesim.msg import Pose

def pose_callback(msg):
	print(msg.theta)
rospy.init_node('turtle_revolve', anonymous=True)
velocity_publisher = rospy.Publisher('/turtle/cmd/vel', Twist, queue_size=10)
vel_msg=Twist()

velocity_publisher.publish(vel_msg)

rospy.Subscriber("/turtle1/pose, Pose, pose_callback)


