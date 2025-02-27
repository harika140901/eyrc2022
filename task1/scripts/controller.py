#!/usr/bin/env python3

import rospy

# publishing to /cmd_vel with msg type: Twist
from geometry_msgs.msg import Twist
# subscribing to /odom with msg type: Odometry
from nav_msgs.msg import Odometry

# for finding sin() cos() 
import math

# Odometry is given as a quaternion, but for the controller we'll need to find the orientaion theta by converting to euler angle
from tf.transformations import euler_from_quaternion
from geometry_msgs.msg import PoseArray

hola_x = 0
hola_y = 0
hola_theta = 0

x_goals = [1, -1, -1, 1, 0]
y_goals = [1, 1, -1, -1, 0]
theta_goals = [pi/4, 3pi/4, -3pi/4, -pi/4, 0]

def task1_goals_Cb(msg):
	global x_goals, y_goals, theta_goals

	x_goals.clear()
	y_goals.clear()
	theta_goals.clear()

	for waypoint_pose in msg.poses:
		x_goals.append(waypoint_pose.position.x)
		y_goals.append(waypoint_pose.position.y)

		orientation_q = waypoint_pose.orientation
		orientation_list = [orientation_q.x, orientation_q.y, orientation_q.z, orientation_q.w]
		theta_goal = euler_from_quaternion (orientation_list)[2]
		theta_goals.append(theta_goal)


def odometryCb(msg):
	global hola_x, hola_y, hola_theta

	# Write your code to take the msg and update the three variables

def main():
	# Initialze Node
	# We'll leave this for you to figure out the syntax for 
	# initialising node named "controller"
	rospy.init_node('controller', anonymous=True)
	# Initialze Publisher and Subscriber
	# We'll leave this for you to figure out the syntax for
	# initialising publisher and subscriber of cmd_vel and odom respectively
	pub = rospy.Publisher('/hola_bot/cmd_vel', Twist, queue_size=10)
	sub = rospy.Subscriber('/hola_bot/odom', Twist, queue_size=10)
	# Declare a Twist message
	vel = Twist()
	# Initialise the required variables to 0
	# <This is explained below>
	vel.linear.x=0
    vel.linear.y=0
    vel.linear.z=0
    vel.angular.x = 0
    vel.angular.y = 0
	# For maintaining control loop rate.
	rate = rospy.Rate(100)

    # declare that the node subscribes to task1_goals along with the other declarations of publishing and subscribing
	rospy.Subscriber('task1_goals', PoseArray, task1_goals_Cb)
    
	# Initialise variables that may be needed for the control loop
	# For ex: x_d, y_d, theta_d (in **meters** and **radians**) for defining desired goal-pose.
	# and also Kp values for the P Controller
	x_d = 0
	y_d = 0
	theta_d = 0
	Kp = 0
	#
	# 
	# Control Loop goes here
	#
	#
    while not rospy.is_shutdown():

    # Find error (in x, y and theta) in global frame
	ex = hola_x - x_d
	ey = hola_y - y_d
	etheta = hola_theta - theta_d
    # the /odom topic is giving pose of the robot in global frame
    # the desired pose is declared above and defined by you in global frame
    # therefore calculate error in global frame

    # (Calculate error in body frame)
    # But for Controller outputs robot velocity in robot_body frame, 
    # i.e. velocity are define is in x, y of the robot frame, 
    # Notice: the direction of z axis says the same in global and body frame
    # therefore the errors will have have to be calculated in body frame.
    # 
    # This is probably the crux of Task 1, figure this out and rest should be fine.

    # Finally implement a P controller 
    # to react to the error with velocities in x, y and theta.

    # Safety Check
    # make sure the velocities are within a range.
    # for now since we are in a simulator and we are not dealing with actual physical limits on the system 
    # we may get away with skipping this step. But it will be very necessary in the long run.

    vel.linear.x = vel_x
    vel.linear.y = vel_y
    vel.angular.z = vel_z

    pub.publish(vel)
    rate.sleep()


if __name__ == "__main__":
	try:
		main()
	except rospy.ROSInterruptException:
		pass