#!/usr/bin/env python 3
import rclpy
from rclpy.node import Node
class counter_node (Node) :
    def __init__(self) :
        super().__init__("new_node")
        self.count = 0
        self.timer = self.create_timer(1 , self.counter)
    def counter(self) :
        self.get_logger().info(f"hello everyone :- {self.count}")
        self.count += 1
def main (args = None) :
    rclpy.init(args = args)
    node = counter_node()
    try :
        rclpy.spin(node)
    except KeyboardInterrupt :
        pass
    finally :
        node.destroy_node()
        node.shutdown()
if __name__ == "__main__" :
    main()