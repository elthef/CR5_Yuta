#!/usr/bin/env python

import rospy
from dobot_bringup.srv import ServoJ


def move(req):
#    result = req.a +req.b +req.c
 #   rospy.loginfo("Sum of " + str(req.a) + " and " +  str(req.b) +str(req.c)+ " is: " +str(result));
    return req;


if __name__ == "__main__":
    rospy.init_node("test_server");
    rospy.loginfo("Add two ints server node created");

    # create service server
    # name, server type, handle function based on request
    #service = rospy.Service("/ServoJ", ServoJ, """move""");
    service = rospy.Service("/ServoJ", ServoJ, move);

    rospy.loginfo("Service server has been started");

    rospy.spin();