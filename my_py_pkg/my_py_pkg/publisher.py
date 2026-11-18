#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32

class publisher_testing(Node) :
    def __init__ (self) :
        super().__init__("publisher_testing_node")
        self.number_publisher = self.create_publisher(
            Int32 ,
            "publishing_topic" ,
            10
        )
        self.count = 0
        self.timer = self.create_timer(1 , self.callback)
        self.get_logger().info("The publishing node has sucessfully started and publishing on topic PUBLISHING TOPIC has started")
    def callback(self) :
        msg = Int32()
        msg.data = self.count
        self.number_publisher.publish(msg)
        self.get_logger().info('publishing :- "%s"' % msg.data)
        self.count += 1
def main(args = None) :
    rclpy.init(args = args)
    node = publisher_testing()
    try :
        rclpy.spin(node)
    except KeyboardInterrupt :
        pass
    finally :
        node.destroy_node()
        if rclpy.ok() :
            rclpy.shutdown()
if __name__ == "__main__" :
    main()  