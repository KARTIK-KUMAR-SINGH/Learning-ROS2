#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from example_interfaces.msg import String
class RobotNewsStation(Node):
    def __init__(self) :
        super().__init__("robot_news_station_node_publisher")
        self.publisher = self.create_publisher(String , "robot_news" , 10)
        self.timer = self.create_timer(1.0 , self.publish_news)
        self.get_logger().info("Robot news station is now initialised")

    def publish_news(self):
        msg = String()
        msg.data = "Hello this is a robot messaging "
        self.publisher.publish(msg)
def main(args = None) :
    rclpy.init(args = args)
    node = RobotNewsStation()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__" :
    main()