#!/usr/bin/env python

import rospy
from dobot_bringup.srv import *
import time



if __name__ == "__main__":
    rospy.init_node("test_client");

    rospy.loginfo("Wait for ros service .............");
    rospy.wait_for_service("/ServoJ");
    rospy.loginfo("Find ros service. Start connect now..");

# create client now, catch exceptio if cannot connect
try:
    #define an object wit client using rosserice name and service type
    my_test=rospy.ServiceProxy("/dobot_bringup/srv/ServoJ",ServoJ);

    #use the client object now
    #responce = my_test("{j1: 0.0, j2: 0.0, j3: 0.0, j4: 0.0, j5: 0.0, j6: 0.0}");
    responce = my_test(0.0,0.0,0.0,0.0,0.0,0.0);
    rospy.loginfo( responce);

except rospy.ServiceException as res:
    #rospy.logwarn("Service failed:" + str(e));
    rospy.logwarn(str(res));
time.sleep(2)
try:
    #define an object wit client using rosserice name and service type
    my_test=rospy.ServiceProxy("/dobot_bringup/srv/ServoJ",ServoJ);

    #use the client object now
    #responce = my_test("{j1: 0.0, j2: 0.0, j3: 0.0, j4: 0.0, j5: 0.0, j6: 0.0}");
    responce = my_test(30.0,50.0,20.0,10.0,-90.0,0.0);
    rospy.loginfo( responce);

except rospy.ServiceException as res:
    #rospy.logwarn("Service failed:" + str(e));
    rospy.logwarn(str(res));

time.sleep(2)
try:
    #define an object wit client using rosserice name and service type
    my_test=rospy.ServiceProxy("/dobot_bringup/srv/ServoJ",ServoJ);

    #use the client object now
    #responce = my_test("{j1: 0.0, j2: 0.0, j3: 0.0, j4: 0.0, j5: 0.0, j6: 0.0}");
    responce = my_test(30.0,50.0,20.0,20.0,-90.0,0.0);
    rospy.loginfo( responce);

except rospy.ServiceException as res:
    #rospy.logwarn("Service failed:" + str(e));
    rospy.logwarn(str(res));
rospy.spin()