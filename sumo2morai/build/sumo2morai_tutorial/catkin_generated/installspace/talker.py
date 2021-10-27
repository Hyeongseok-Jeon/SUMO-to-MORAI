#!/usr/bin/env python2
# license removed for brevity
import os
import sys
import optparse
import rospy
from morai_msgs.msg import NpcGhostCmd, NpcGhostInfo

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
    print('a')
    print('b')
    step = 0
    r = rospy.Rate(10) #10hz

    while traci.simulation.getMinExpectedNumber() > 0:
        traci.simulationStep()
        print(step)
        VehList = vehicle.getIDList()
        num_of_ego = len(VehList)
        
        ghost_cmd_msg=NpcGhostCmd()
        ghost_npc_info=NpcGhostInfo()
        ghost_npc_info.unique_id =int(VehList[0])
        ghost_npc_info.name = '2016_Hyundai_Genesis_DH'
        ghost_npc_info.position.x=vehicle.getPosition3D(VehList[0])[0]
        ghost_npc_info.position.y=vehicle.getPosition3D(VehList[0])[1]
        ghost_npc_info.position.z=vehicle.getPosition3D(VehList[0])[2]
        ghost_npc_info.rpy.z =vehicle.getAngle(VehList[0])
        ghost_cmd_msg.npc_list.append(ghost_npc_info)

        ghost_cmd_pub.publish(ghost_cmd_msg)

        r.sleep
        # camera_index =
        #for i in range(len(VehList)):
        #    print("Id : " + VehList[i] + "    position=" + str(vehicle.getPosition3D(VehList[i])[0]))
        # vehicle.getParameter(0, )
        # det_vehs = traci.inductionloop.getLastStepVehicleIDs("det_0")
        # for veh in det_vehs:
        #     print(veh)
        #     traci.vehicle.changeLane(veh, 2, 25)

        # if step == 100:
        #     traci.vehicle.changeTarget("1", "e9")
        #     traci.vehicle.changeTarget("3", "e9")

        step += 1

    traci.close()
    sys.stdout.flush()


if __name__ == '__main__':
    options = get_options()

    # check binary
    if options.nogui:
        sumoBinary = checkBinary('sumo')
    else:
        sumoBinary = checkBinary('sumo-gui')

    traci.start([sumoBinary, "-c", "sumo/sumocfgs/VenturaFRW.sumocfg",
                 "--step-length", "0.01"])
    try:
    	run()
    except rospy.ROSInterruptException: pass

'''
#!/usr/bin/env python
# license removed for brevity
import sys
sys.path.append('/opt/ros/melodic/lib/python2.7/dist-packages/')
sys.path.append('/home/jhs/Desktop/SUMO-to-MORAI/sumo2morai/src/')

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

'''
