#!/usr/bin/env python

import rospy
from std_msgs.msg import Float32
import ms5837

def talker():
	pub = rospy.Publisher('depth', Float32, queue_size=10)
	rospy.init_node('Depth Sensor', anonymous=True)
	rate = rospy.Rate(10) # 10hz

	while not rospy.is_shutdown():
		if sensor.read():
			pub.publish(sensor.depth())
	        else:
                	print "Sensor read failed!"
		rate.sleep()

if __name__ == '__main__':
	try:
		sensor = ms5837.MS5837_30BA() # Default I2C bus is 1 (Raspberry Pi 3)
		if not sensor.init():
        		print "Sensor could not be initialized"
		talker()
	except rospy.ROSInterruptException:
		pass
