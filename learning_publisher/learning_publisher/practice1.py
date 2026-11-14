#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class RobotPublisher(Node) :
    def __init__ (self) :
        super().__init__("robot_news_station")
        self.publisher_ = self.create_publisher(
            String , 
            'robot_news_topic' ,
            10
        )
        self.timer = self.create_timer(1 , self.publish_news)
        self.get_logger().info("Robot news has started")
    def publish_news(self) :
        msg = String()
        msg.data = 'Hello from Robot news station'
        self.publisher_.publish(msg)
        self.get_logger().info('publishing : "%s"' % msg.data)
def main(args = None) :
    rclpy.init(args = args)
    node = RobotPublisher()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__" :
    main()