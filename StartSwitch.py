#!/usr/bin/env python

#<node pkg ="auv_raspi" name = "StartSwitch" type = "StartSwitch.py" output="screen">
#</node>

import rospy
from std_msgs.msg import Bool
# import RPi.GPIO as GPIO

def talker():
	rospy.init_node('StartNode', anonymous=True)
	pub = rospy.Publisher('start', Bool, queue_size=0)
	rate = rospy.Rate(10) # 10hz

	runOnce = 0;
	while not rospy.is_shutdown():
		if True:
			if(runOnce == 0):
				rospy.loginfo("Starting Mission")
				runOnce = 1
			pub.publish(True)
		else:
			pub.publish(False)

		rate.sleep()


if __name__ == '__main__':
	# GPIO.setmode(GPIO.BCM)
	# GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
	try:
		talker()
	except rospy.ROSInterruptException:
		pass
