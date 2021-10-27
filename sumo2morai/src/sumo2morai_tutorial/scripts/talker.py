#!/usr/bin/env python
# license removed for brevity
import os
import sys
import optparse
import rospy
import roslibpy
import time
from sumo2morai_tutorial.msg import NpcGhostCmd

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
    client = roslibpy.Ros(host='localhost', port=9090)
    client.run()
    talker = roslibpy.Topic(client, '/NpcGhost_Topic', 'sumo2morai_tutorial/msg')
    '''
pub_cmd = rospy.Publisher('NpcGhost_Topic', NpcGhostCmd)
    rospy.init_node('sumo2morai', anonymous=True)

    r = rospy.Rate(10) #10hz
'''
    step = 0
    msg_cmd = NpcGhostCmd()

    while traci.simulation.getMinExpectedNumber() > 0:
        traci.simulationStep()
        print(step)
        VehList = vehicle.getIDList()
        num_of_ego = len(VehList)


        msg_cmd.header.seq = 0
        msg_cmd.header.stamp = time.time()
        msg_cmd.header.frame_id = 'test'

        msg_cmd.npc_list.append(int(VehList[0]))
        msg_cmd.npc_list.append('2016_Hyundai_Genesis_DH')
        msg_cmd.npc_list.append([vehicle.getPosition3D(VehList[0])[0], vehicle.getPosition3D(VehList[0])[1], vehicle.getPosition3D(VehList[0])[2]])
        msg_cmd.npc_list.append([0, 0, vehicle.getAngle(VehList[0])])

        talker.publish(msg_cmd)
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
