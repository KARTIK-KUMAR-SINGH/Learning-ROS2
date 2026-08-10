#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

class MyNode(Node):
    def __init__(self):
        super().__init__("py_test")
        self.counter = 0
        self.get_logger().info("Hello world")
        self.create_timer(1.0 , self.timer_call_back)

    def timer_call_back(self) :
        self.get_logger().info("Hello from timer!" + str(self.counter))
        self.counter = self.counter + 1

def main(args = None):
    rclpy.init(args=args)
    node = MyNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()