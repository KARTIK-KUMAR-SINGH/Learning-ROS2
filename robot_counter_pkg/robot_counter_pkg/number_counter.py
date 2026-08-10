#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from example_interfaces.msg import Int32
class number_counting(Node): #Modify Name
    def __init__(self) :
        super().__init__("number_counter") #Node Name
        self.subscriber = self.create_subscription(Int32 , "number" , self.call_back_number , 10)
        self.get_logger().info("Number counter has sucessfully subscriber to a topic")
        self.data_coming = 0
        self.publisher = self.create_publisher(Int32 , "number_count" , 10) #Topic name
    def call_back_number(self , msg):
        self.data_coming = self.data_coming + msg.data 
        self.get_logger().info("Recived number from publisher and added 2 from the subscriber: " + str(self.data_coming+ 2))
        output_msg = Int32()
        output_msg.data = self.data_coming 
        self.publisher.publish(output_msg)


def main(args = None) :
    rclpy.init(args = args)
    node = number_counting() #Modify Name
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__" :
    main()