#!/use/bin/env python3
import rclpy
from rclpy.node import Node

class testing_node(Node):
    def __init__(self) :
        super().__init__("testing_node")
        self.get_logger().info("The testing node is working")
        self.count = 0
        self.timer = self.create_timer(1 , self.callback)
    def callback(self) :
        self.get_logger().info(f"testing :- {self.count}")
        self.count += 1
def main(args = None) :
    rclpy.init(args = args)
    node = testing_node()
    try : 
        rclpy.spin(node)
    except KeyboardInterrupt :
        pass
    finally :
        node.destroy_node(node)
        if rclpy.ok():
            rclpy.shutdown()
if __name__ == "__main__" :
    main()