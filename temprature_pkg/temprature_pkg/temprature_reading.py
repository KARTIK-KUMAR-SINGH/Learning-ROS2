#!usr/bin/env python 3
import random
import rclpy
from rclpy.node import Node

class TempratureReading(Node):
    def __init__(self):
        super().__init__("temprature_reading")
        self.counter = 0
        
        self.get_logger().info("Temprature Sensor is now initialised")
        self.create_timer(1.0 , self.timer_call_back)
    def timer_call_back(self) :
        self.reading = random.randint(0 , 255)
        self.get_logger().info("Temprature sensor current reading is : " + str(self.reading) + "and the current counter count is :- " + str(self.counter))
        self.counter = self.counter + 1
def main(args = None):
    rclpy.init(args = args)
    node = TempratureReading()
    rclpy.spin(node)
    rclpy.shutdown()
if __name__ == "__main__":
    main()