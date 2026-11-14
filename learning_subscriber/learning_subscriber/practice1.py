#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class robot_news_recieve(Node) :
    def __init__(self) :
        super().__init__("robot_news_reciveing_node")
        self.robot_news_subscriber = self.create_subscription(
            String ,
            "robot_news_topic",
            self.callback_robot_news ,
            10
        )
    def callback_robot_news(self , msg : String) :
        self.get_logger().info(msg.data)
def main(args = None) :
    rclpy.init(args = args)
    node = robot_news_recieve()
    try :
        rclpy.spin(node)
    except KeyboardInterrupt :
        pass
    finally :
        rclpy.shutdown()
if __name__ == "__main__" :
    main()