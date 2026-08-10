#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
class RobotNewsStation(Node): #Modify Name
    def __init__(self) :
        super().__init__("robot_news_station_node_publisher") #Node Name


def main(args = None) :
    rclpy.init(args = args)
    node = RobotNewsStation() #Modify Name
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__" :
    main()