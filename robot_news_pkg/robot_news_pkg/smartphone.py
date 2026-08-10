#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from example_interfaces.msg import String
class Smartphone(Node): #Modify Name
    def __init__(self) :
        super().__init__("smartphone_node") #Modify Name
        self.subscriber = self.create_subscription(String , "robot_news" , self.callback_robot_news , 10)
        self.get_logger().info("Smartphone subscriber is now initialised")
    def callback_robot_news(self , msg) :
        self.get_logger().info("Recived news from robot news station : " + msg.data)

def main(args = None) :
    rclpy.init(args = args)
    node = Smartphone() #Modify Name
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__" :
    main()