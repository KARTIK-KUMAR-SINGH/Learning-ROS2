#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

class odd_even(Node) :
    def __init__(self) :
        super().__init__("new_node")
        self.count = 1
        self.timer = self.create_timer(1 , self.counter)
    def counter(self) :
        if(self.count % 2 == 0):
            self.get_logger().info(f"Number {self.count} : Even")
        else :
            self.get_logger().info(f"Number {self.count} : Odd")

        self.count = self.count + 1
        if(self.count > 30) :
            self.get_logger().info("All numbers completed")
            self.timer.cancel()
            if rclpy.ok ():
                rclpy.shutdown()
def main(args = None) :
    rclpy.init(args = args)
    node = odd_even()
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