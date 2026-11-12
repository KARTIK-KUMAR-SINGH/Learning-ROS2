#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

class back_counter_node(Node) :
    def __init__(self) :
        super().__init__("new_node")
        self.count = 20 
        self.timer = self.create_timer(1  , self.back_count)
    def back_count(self) :
        self.get_logger().info(f"The count currently is :- {self.count}")
        self.count = self.count - 1
        if(self.count < 0):
            self.get_logger().info("Count down completed")
            self.timer.cancel()
            if rclpy.ok() :
                rclpy.shutdown()
def main (args = None) :
    rclpy.init(args = args)
    node = back_counter_node()
    try :
        rclpy.spin(node)
    except KeyboardInterrupt :
        pass
    finally :
        node.destroy_node()
        if rclpy.ok() :
            rclpy.shutdown()
if __name__ == '__main__' :
    main()