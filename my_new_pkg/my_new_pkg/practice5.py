#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

class MultiplicationTable(Node) :
    def __init__(self) :
        super().__init__("new_node")
        self.num = 7
        self.multi = 1

        self.timer = self.create_timer(1 , self.counter)
    def counter(self) :
        self.multiply = self.num * self.multi
        self.get_logger().info(f"{self.num} x {self.multi} = {self.multiply}")
        self.multi = self.multi + 1
        if(self.multi > 10) :
            self.get_logger().info("The multiplication is connected")
            self.timer.cancel()
            if rclpy.ok() :
                rclpy.shutdown()
def main(args = None) :
    rclpy.init(args = args)
    node = MultiplicationTable()
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