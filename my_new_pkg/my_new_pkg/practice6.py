#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

class sum_calc(Node) :
    def __init__(self) :
        super().__init__("new_node")
        self.start = 1
        self.sum = 0 

        self.timer = self.create_timer(1 , self.counter)
    def counter(self) :
        self.sum = self.sum + self.start
        self.get_logger().info(f"Number :- {self.start} , current sum :- {self.sum}")
        self.start += 1

        if(self.start > 20) :
            self.get_logger().info(f"The total Sum is :- {self.sum}")
            self.timer.cancel()
            if rclpy.ok() :
                rclpy.shutdown()
def main(args = None) :
    rclpy.init(args = args)
    node = sum_calc()
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
            