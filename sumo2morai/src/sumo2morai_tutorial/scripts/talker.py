#!/usr/bin/env python
# license removed for brevity
import rospy
from sumo2morai_tutorial.msg import NpcGhostCmd, NpcGhostInfo

def talker():
    pub_cmd = rospy.Publisher('morai_msgs', NpcGhostCmd)
    pub_info = rospy.Publisher('morai_msgs', NpcGhostInfo)
    rospy.init_node('sumo2morai', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        hello_str = "hello world %s" % rospy.get_time()
        rospy.loginfo(hello_str)
        pub.publish(hello_str)
        rate.sleep()

def talker():
    pub_cmd = rospy.Publisher('morai_msgs', NpcGhostCmd)
    pub_info = rospy.Publisher('morai_msgs', NpcGhostInfo)
    rospy.init_node('sumo2morai', anonymous=True)
    r = rospy.Rate(10) #10hz
    msg = Person()
    msg.name = "ROS User"
    msg.age = 4

    while not rospy.is_shutdown():
        rospy.loginfo(msg)
        pub.publish(msg)
        r.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException: pass
