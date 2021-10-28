# SUMO-to-MORAI

This repository is to interlock SUMO simulator to MORAI simulator
Traffic flow generated from SUMO simulator is visualized in MORAI Simulator via ROS communication

Overall repository is based on Unbuntu 18.04.6 LTS and ROS Melodic

Table of Contents
=================
  * [SUMO Install](#SUMO-install)
  * [ROS Install](#ROS-install)
  * [SUMO simulation configuration](#SUMO-simulation-configuration)
  * [Building ROS Package](#Building-ROS-Package)
  * [Running the Simulations](#Running-the-Simulations)
  * [Citation](#citation)



## SUMO-Install
```sh
sudo add-apt-repository ppa:sumo/stable
sudo apt-get update
sudo apt-get install sumo sumo-tools sumo-doc
```

SUMO Version 1.10.0 is used

## ROS-Install
```sh
sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'
sudo apt install curl
curl -s https://raw.githubusercontent.com/ros/rosdistro/master/ros.asc | sudo apt-key add -
sudo apt update
sudo apt install ros-melodic-desktop-full
echo "source /opt/ros/melodic/setup.bash" >> ~/.bashrc
source ~/.bashrc
sudo apt install python-rosdep python-rosinstall python-rosinstall-generator python-wstool build-essential
sudo rosdep init
rosdep update
```

More detailed description, please refer to [ROS](http://wiki.ros.org/melodic/Installation/Ubuntu)

## SUMO-simulation-configuration
This repository is tested only for the openDRIVE based map format.

In order to get *test_map*.xord files for the map, please contect [MORAI](https://www.morai.ai/)

If you already have *test_map*.xord files, you need to move *test_map*.xord files to *sumo2morai/sumo/xords*


Then *test_map*.xord file has to be converted to SUMO net file with following command

```sh
netconvert --opendrive sumo2morai/sumo/xords/test_map.xord -o sumo2morai/sumo/nets/test_map.net.xml
```

Using the SUMO net file, random trips can be generated in route file as belows.

```sh
python /usr/share/sumo/tools/randomTrips.py -n sumo2morai/sumo/nets/test_map.net.xml -e 3600 -r sumo2morai/sumo/routes/test_map.rou.xml
```
More detail information on the random trip of SUMO simulator, please refer [SUMO-randomTrips.py](https://sumo.dlr.de/docs/Tools/Trip.html#randomtripspy)

Finally, in *sumo2morai/sumo/sumocfgs/*, please make *test_map.sumocfg* file with text editor.

```
<configuration>

<input>
<net-file value="../nets/test_map.net.xml"/>
<route-files value="../routes/test_map.rou.xml"/>
</input>
<time>
<begin value="0"/>
<end value="3600"/>
</time>

</configuration>
```

## Building-ROS-Package
For specifying the map and trips generated in [SUMO simulation configuration](#SUMO-simulation-configuration), 

find Line 123 in *test.py* in *src/npc_ghost_test/scrips* which is follows.

```sh
traci.start([sumoBinary, "-c", "sumo/sumocfgs/test_map.sumocfg","--step-length", "0.01"])
```

you need to modify above command with your custom map name as

```sh
traci.start([sumoBinary, "-c", "sumo/sumocfgs/KAIST_Munji_Campus.sumocfg","--step-length", "0.01"])
```


In *sumo2morai/*, 
```sh
catkin_make
source devel/setup.bash
```

## Running-the-Simulations
1. Run MORAI Simulator and select *test_map*
2. In *new terminal*
```
roscore
```
3. In *new terminal*,
```
cd <repository_root>/sumo2morai
source devel/setup.bash
roslaunch rosbridge_server rosbridge_websocket.launch
```
4. In *new terminal*,
```
cd <repository_root>/sumo2morai
source devel/setup.bash
rosrun npc_ghost_test test.py
```
