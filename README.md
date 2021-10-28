# SUMO-to-MORAI

This repository is to interlock SUMO simulator to MORAI simulator
Traffic flow generated from SUMO simulator is visualized in MORAI Simulator via ROS communication

Overall repository is based on Unbuntu 18.04.6 LTS and ROS Melodic

Table of Contents
=================
  * [SUMO Install](#SUMO-install)
  * [ROS Install](#ROS-install)
  * [Training](#Training)
  * [Testing](#testing)
  * [Licence](#licence)
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

SUMO Version 1.10.0 is used

## Prepare Data
In this repository, small amount of the raw data and corresponding post-processed sample of Argoverse Motion Forecasting dataset is included.
If you want to use full data, please download from [Argoverse](https://www.argoverse.org/tasks.html#forecasting-link) official website

Since the PfP requires future trajectory of the ego vehicle, the test set is not used.

[Confidential] Because of the internal issue, the source code for data processing is blocked.
For academical use, please contact "Anonymous"

## Training
### Training with single GPU
```sh
python train.py
```

### Training with multigpus using horovod
```sh
# single node with 4 gpus
horovodrun -np 4 -H localhost:4 python train.py
```

## Testing

![img](misc/fig4.png)


