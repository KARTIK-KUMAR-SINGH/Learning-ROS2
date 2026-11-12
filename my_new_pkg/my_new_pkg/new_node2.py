#!usr/bin/env/python3
import rclpy
from rclpy.node import Node
def main (args = None) :
    rclpy.init(args = args)
    node = Node("new_node")
    while(1) :
        node.get_logger().info("Everyone Hello Everyone nice to see you all here!!")
    rclpy.spin(node)
    rclpy.shutdown()
if __name__ ==  "__main__" :
    main()