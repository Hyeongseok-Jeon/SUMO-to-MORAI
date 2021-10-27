#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import rospy


from geometry_msgs.msg import PoseStamped
from math import pi
from morai_msgs.msg import ObjectStatusList,NpcGhostCmd,NpcGhostInfo
import tf
class ghost_test :

    def __init__(self):
        rospy.init_node('test', anonymous=True)

        rospy.Subscriber("/Object_topic", ObjectStatusList, self.objectCallBack)
        self.ghost_cmd_pub = rospy.Publisher('NpcGhost_Topic',NpcGhostCmd, queue_size=1)
        rospy.spin()
        

  
    def objectCallBack(self,msg):
        ghost_cmd_msg=NpcGhostCmd()

        for npc in msg.npc_list :
            ghost_npc_info=NpcGhostInfo()
            ghost_npc_info.unique_id =npc.unique_id
            ghost_npc_info.name =npc.name
            ghost_npc_info.position.x=npc.position.x
            ghost_npc_info.position.y=npc.position.y
            ghost_npc_info.position.z=npc.position.z
            ghost_npc_info.rpy.z =npc.heading
            ghost_cmd_msg.npc_list.append(ghost_npc_info)

        self.ghost_cmd_pub.publish(ghost_cmd_msg)


        
   
       
            





        # waypint_pose=PoseStamped()
        # x=msg.pose_x
        # y=msg.pose_y
        # z=msg.pose_z
        # if self.is_status== True :
        #     distance=sqrt(pow(x-self.prev_x,2)+pow(y-self.prev_y,2))
        #     if distance > 0.5 :
        #         waypint_pose.pose.position.x=x
        #         waypint_pose.pose.position.y=y
        #         waypint_pose.pose.position.z=z
        #         waypint_pose.pose.orientation.w=1
        #         self.path_msg.poses.append(waypint_pose)
        #         self.path_pub.publish(self.path_msg)
        #         data='{0}\t{1}\n'.format(x,y)
        #         self.f.write(data) 
        #         self.prev_x=x
        #         self.prev_y=y
        #         print(x,y)

                
        # else :
        #     self.is_status=True
        #     self.prev_x=x
        #     self.prev_y=y
            
        

if __name__ == '__main__':
    try:
        test_=ghost_test()
    except rospy.ROSInterruptException:
        pass

    