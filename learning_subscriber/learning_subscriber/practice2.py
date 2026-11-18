#!usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import Int16

class counting_subscriber(Node) :
    def __init__(self) :
        super().__init__("counting_subscriber_node")
        self.count_subscriber = self.create_subscription(
            Int16 ,
            "counting_topic" ,
            self.callback ,
            10
        )
    def callback(self , msg : Int16) :
        self.get_logger().info(str(msg.data))
def main(args = None) :
    rclpy.init(args = args)
    node = counting_subscriber()
    try :
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally :
        rclpy.shutdown()

if __name__ == "__main__" :
    main()
