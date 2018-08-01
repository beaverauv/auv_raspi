#!/usr/bin/env python
import rospy
from auv_motor_control.msg import thruster_int
import Adafruit_PCA9685

pwm = Adafruit_PCA9685.PCA9685()
pwm.set_pwm_freq(60)

#Neutral is 380-385, max is 485, min is 280

foreward_Max = 485
reverse_Max = 280
neutral = [380,385]
thruster_List = ['thruster_xy_frontRight', 'thruster_xy_frontLeft', 'thruster_xy_backRight', 'thruster_xy_backLeft', 'thruster_z_frontRight', 'thruster_z_frontLeft', 'thruster_z_backRight', 'thruster_z_backLeft']

def set_All(value):
        for chanel in range(0,8):
                pwm.set_pwm(chanel, 0, value)

def scaleMap(convert,input_min, input_max, output_min, output_max):
        return (convert - input_min) * (output_max - output_min) / (input_max - input_min) + output_min

def thrusterMap(convert):
        if convert < neutral[0]:
                return scaleMap(convert, 0, -100, neutral[0], reverse_Max)
        elif convert > neutral[1]:
                return scaleMap(convert, 0, 100, neutral[1], foreward_Max)
        else:
                return 383

def callback(data):
        print(type(data.thruster_xy_frontLeft))
	pwm.set_pwm(0, 0, thrusterMap(data.thruster_xy_frontLeft))
	pwm.set_pwm(1, 0, thrusterMap(data.thruster_z_frontLeft))
	print(data.thruster_z_frontLeft)
	print(thrusterMap(data.thruster_z_frontLeft))
	pwm.set_pwm(2, 0, thrusterMap(data.thruster_z_backLeft))
	pwm.set_pwm(3, 0, thrusterMap(data.thruster_xy_backLeft))
	pwm.set_pwm(4, 0, thrusterMap(data.thruster_xy_backRight))
	pwm.set_pwm(5, 0, thrusterMap(data.thruster_z_backRight))
	pwm.set_pwm(6, 0, thrusterMap(data.thruster_z_frontRight))
	pwm.set_pwm(7, 0, thrusterMap(data.thruster_xy_frontRight))

def listener():
        rospy.init_node('thruster_ints', anonymous=True)
        rospy.Subscriber('thruster_int', thruster_int, callback)
        rospy.spin()

if __name__ == '__main__':
        print("Started...")
        set_All(neutral[1])
        print("ESC Setup Complete: Starting 'listener()'")
        listener()
        print("Ending...")
        set_All(neutral[1])
