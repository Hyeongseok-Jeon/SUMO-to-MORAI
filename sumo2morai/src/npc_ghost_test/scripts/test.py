#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import optparse
import rospy

from geometry_msgs.msg import PoseStamped
from math import pi
from morai_msgs.msg import ObjectStatusList,NpcGhostCmd,NpcGhostInfo

if 'SUMO_HOME' in os.environ:
    tools = os.path.join(os.environ['SUMO_HOME'], 'tools')
    sys.path.append(tools)
else:
    sys.exit("please declare environment variable 'SUMO_HOME'")

from sumolib import checkBinary  # Checks for the binary in environ vars
from traci.main import _vehicle, _vehicletype
import traci
vehicle = _vehicle.VehicleDomain()
vehicletype = _vehicletype.VehicleTypeDomain()


def get_options():
    opt_parser = optparse.OptionParser()
    opt_parser.add_option("--nogui", action="store_true",
                         default=False, help="run the commandline version of sumo")
    options, args = opt_parser.parse_args()
    return options

def run():
    rospy.init_node('test', anonymous=True)
    ghost_cmd_pub = rospy.Publisher('NpcGhost_Topic',NpcGhostCmd, queue_size=1)
    step = 0
    while traci.simulation.getMinExpectedNumber() > 0:
        traci.simulationStep()
        VehList = vehicle.getIDList()
        num_of_ego = len(VehList)
        
        ghost_cmd_msg=NpcGhostCmd()
        for i in range(num_of_ego):
            ghost_npc_info=NpcGhostInfo()
            ghost_npc_info.unique_id =int(VehList[i])
            ghost_npc_info.name ='2016_Hyundai_Ioniq'
            ghost_npc_info.position.x=vehicle.getPosition3D(VehList[i])[0]+137
            ghost_npc_info.position.y=vehicle.getPosition3D(VehList[i])[1]+241
            ghost_npc_info.position.z=vehicle.getPosition3D(VehList[i])[2]
            ghost_npc_info.rpy.z =90-vehicle.getAngle(VehList[i])
            ghost_cmd_msg.npc_list.append(ghost_npc_info)
        
        ghost_cmd_pub.publish(ghost_cmd_msg)
        step += 1

    traci.close()
    sys.stdout.flush()


class ghost_test :

    def __init__(self):
        rospy.init_node('test', anonymous=True)

        rospy.Subscriber("/Object_topic", ObjectStatusList, self.objectCallBack)
        self.ghost_cmd_pub = rospy.Publisher('NpcGhost_Topic',NpcGhostCmd, queue_size=1)
        rospy.spin()
        
    def objectCallBack(self,msg):
        print('a')
        ghost_cmd_msg=NpcGhostCmd()

        for npc in msg.npc_list :
            ghost_npc_info=NpcGhostInfo()
            ghost_npc_info.unique_id =npc.unique_id
            ghost_npc_info.name ='2016_Hyundai_Ioniq'
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
    options = get_options()

    if options.nogui:
        sumoBinary = checkBinary('sumo')
    else:
        sumoBinary = checkBinary('sumo-gui')

    # traci starts sumo as a subprocess and then this script connects and runs
    traci.start([sumoBinary, "-c", "sumo/sumocfgs/VenturaFRW.sumocfg",
                 "--step-length", "0.01"])
    try:
        run()
    except rospy.ROSInterruptException:
        pass

    
