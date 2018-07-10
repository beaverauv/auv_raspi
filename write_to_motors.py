#!/usr/bin/env python
import rospy
from std_msgs.msg import int32
import include/Adafruit_PCA9685
import time

pwm = Adafruit_PCA9685.PCA9685()
pwm.set_pwm_freq(60)

#Neutral is 380-385, max is 485, min is 280

foreward_Max = 485
reverse_Max = 280
neutral = [380,385]
thruster_List = [thruster_xy_frontRight, thruster_xy_frontLeft, thruster_xy_backRight, thruster_xy_backLeft, thruster_z_frontRight, thruster_z_frontLeft, thruster_z_backRight, thruster_z_backLeft]

def setup_ESC():
    for value in range(reverse_Max, foreward_Max):
        for chanel in range(0,8):
            pwm.set_pwm(chanel, 0, value)
        time.sleep(0.1)
    for value in range(foreward_Max, reverse_Max):
        for chanel in range(0,8):
            pwm.set_pwm(chanel, 0, value)
        time.sleep(0.1)

def scaleMap(convert,input_min, input_max, output_min, output_max):
    return (float(convert) - input_min) * (output_max - output_min) / (input_max - input_min) + output_min

def thrusterMap(convert):
    if convert < neutral[0]:
        return scaleMap(convert, 0, -100, neutral[0], reverse_Max)
    elif convert > neutral[1]:
        return scaleMap(convert, 0, 100, neutral[1], foreward_Max)
    else:
        return 383
    
def callback(data):
    for thruster in range(0,8):
        pwm.set_pwm(thruster, 0, thrusterMap(data.thruster_List[thruster]))
    
def listener():
    rospy.init_node('thruster_int', anonymous=True)
    rospy.Subscriber("thrusterinteger", int32, callback)
    rospy.spin()

if __name__ == '__main__':
        listener()
        setup_ESC()