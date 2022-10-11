# HackMining2022


## Description
This is a solution to the Hackathon challenge presented by [Becker Mining Europe](https://www.becker-mining.com/). The problem statement involves developing a verification tool for the existing PDS4.0 system. This tool should be able to sense real time information from anchor points, develop a simple and lucid coordinate system, and accurately determine location of object and humans in the mine field.


## Installation
Requires a RasberryPi PICO with Micro-ROS installed. Also requires THONNY to be installed in order to accesss the device usinf a serial bus connection.

##Solution
The algorithm presented here is a trilateration based system, which uses a minimum of three anchors to develop a coordinate system and localize object/device. Please refer to /files/presentation_group_print_hello_world_.pptx for a more thorough walkthrough of the solution. 

## Usage
All codes and data files are available inside the /files directory.
/files/TARGET_CFG.txt - Contains MAC address of all anchors from which target position is determied
/files/start.py - determines position of target device/object with respect to anchor points only once
/files/start_loop.py - determines position of target device/object with respect to anchor points continuously
/files/positioning_gui_dynamic.py - gives dynamic graphical output of live location of target

## Project status
This project was only intended for the purpose of the Hackmining2022 hackathon itself, and should not be considered as a working prototype. However, the project was considered a success and future implementation of the solution might be taking place at [Becker Mining Europe](https://www.becker-mining.com/).
