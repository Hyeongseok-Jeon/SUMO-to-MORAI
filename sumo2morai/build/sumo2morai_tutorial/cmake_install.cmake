# Install script for directory: /home/jhs/Desktop/SUMO-to-MORAI/sumo2morai/src/sumo2morai_tutorial

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/home/jhs/Desktop/SUMO-to-MORAI/sumo2morai/install")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

# Install shared libraries without execute permission?
if(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)
  set(CMAKE_INSTALL_SO_NO_EXE "1")
endif()

# Is this installation the result of a crosscompile?
if(NOT DEFINED CMAKE_CROSSCOMPILING)
  set(CMAKE_CROSSCOMPILING "FALSE")
endif()

# Set default install directory permissions.
if(NOT DEFINED CMAKE_OBJDUMP)
  set(CMAKE_OBJDUMP "/usr/bin/objdump")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/sumo2morai_tutorial/msg" TYPE FILE FILES
    "/home/jhs/Desktop/SUMO-to-MORAI/sumo2morai/src/sumo2morai_tutorial/msg/NpcGhostCmd.msg"
    "/home/jhs/Desktop/SUMO-to-MORAI/sumo2morai/src/sumo2morai_tutorial/msg/NpcGhostInfo.msg"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/sumo2morai_tutorial/cmake" TYPE FILE FILES "/home/jhs/Desktop/SUMO-to-MORAI/sumo2morai/build/sumo2morai_tutorial/catkin_generated/installspace/sumo2morai_tutorial-msg-paths.cmake")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include" TYPE DIRECTORY FILES "/home/jhs/Desktop/SUMO-to-MORAI/sumo2morai/devel/include/sumo2morai_tutorial")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/roseus/ros" TYPE DIRECTORY FILES "/home/jhs/Desktop/SUMO-to-MORAI/sumo2morai/devel/share/roseus/ros/sumo2morai_tutorial")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/common-lisp/ros" TYPE DIRECTORY FILES "/home/jhs/Desktop/SUMO-to-MORAI/sumo2morai/devel/share/common-lisp/ros/sumo2morai_tutorial")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/gennodejs/ros" TYPE DIRECTORY FILES "/home/jhs/Desktop/SUMO-to-MORAI/sumo2morai/devel/share/gennodejs/ros/sumo2morai_tutorial")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  execute_process(COMMAND "/usr/bin/python2" -m compileall "/home/jhs/Desktop/SUMO-to-MORAI/sumo2morai/devel/lib/python2.7/dist-packages/sumo2morai_tutorial")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/python2.7/dist-packages" TYPE DIRECTORY FILES "/home/jhs/Desktop/SUMO-to-MORAI/sumo2morai/devel/lib/python2.7/dist-packages/sumo2morai_tutorial")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/pkgconfig" TYPE FILE FILES "/home/jhs/Desktop/SUMO-to-MORAI/sumo2morai/build/sumo2morai_tutorial/catkin_generated/installspace/sumo2morai_tutorial.pc")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/sumo2morai_tutorial/cmake" TYPE FILE FILES "/home/jhs/Desktop/SUMO-to-MORAI/sumo2morai/build/sumo2morai_tutorial/catkin_generated/installspace/sumo2morai_tutorial-msg-extras.cmake")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/sumo2morai_tutorial/cmake" TYPE FILE FILES
    "/home/jhs/Desktop/SUMO-to-MORAI/sumo2morai/build/sumo2morai_tutorial/catkin_generated/installspace/sumo2morai_tutorialConfig.cmake"
    "/home/jhs/Desktop/SUMO-to-MORAI/sumo2morai/build/sumo2morai_tutorial/catkin_generated/installspace/sumo2morai_tutorialConfig-version.cmake"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/sumo2morai_tutorial" TYPE FILE FILES "/home/jhs/Desktop/SUMO-to-MORAI/sumo2morai/src/sumo2morai_tutorial/package.xml")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/sumo2morai_tutorial" TYPE PROGRAM FILES "/home/jhs/Desktop/SUMO-to-MORAI/sumo2morai/build/sumo2morai_tutorial/catkin_generated/installspace/talker.py")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/sumo2morai_tutorial" TYPE PROGRAM FILES "/home/jhs/Desktop/SUMO-to-MORAI/sumo2morai/build/sumo2morai_tutorial/catkin_generated/installspace/test.py")
endif()

