#!/usr/bin/env python 3
import rclpy
import random
from rclpy.node import Node
class MyNode(Node) :
    def __init__(self) :
        super().__init__('humidity_sensor')
        self.counter = 0
        self.get_logger().info('Humidity Sensor is now activated')
        self.create_timer(1.0, self.timers_callback)
    def timers_callback(self) :
        self.reading = random.randint(0 , 255)
        self.get_logger().info("Humidity Sensor reading: " + str(self.reading) + "and the counter count is :- " + str(self.counter))
        self.counter += 1 

def main(args=None) :
    rclpy.init(args = args)
    node = MyNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__' :
    main()