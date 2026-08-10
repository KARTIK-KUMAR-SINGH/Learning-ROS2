#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from example_interfaces.msg import Int32
class number_publisher(Node): #Modify Name
    def __init__(self) :
        super().__init__("number_publisher") #Node Name
        self.publisher = self.create_publisher(Int32 , "number" , 10) #Topic name
        self.timer = self.create_timer(1.0 , self.publish_news)
        self.get_logger().info("A constant number is ready to get published.....waiting for any subscriber to subscribe the topic")

    def publish_news(self):
        msg = Int32()
        msg.data = 2
        self.publisher.publish(msg)

def main(args = None) :
    rclpy.init(args = args)
    node = number_publisher() #Modify Name
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__" :
    main()