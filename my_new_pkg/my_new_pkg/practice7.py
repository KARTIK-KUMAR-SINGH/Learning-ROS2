#!/usr/bin/env python3
import rclpy
import random
import sys
from rclpy.node import Node

class SensorSimulator(Node) :
    def __init__(self) :
        super().__init__("new_node")
        self.count = 1
        self.readings = []
        self.timer = self.create_timer(1 , self.counter)
    def counter(self) :
        self.num = random.randint(5 , 150)
        self.get_logger().info(f"current ultrasonic sensor reading is :- {self.num}")
        self.readings.append(self.num)
        self.count += 1
        if(self.count > 10) :
            length = len(self.readings)
            self.sum = 0 
            self.min = sys.maxsize
            self.max = -sys.maxsize - 1
            for i in range(length) :
                self.sum += self.readings[i]
                if(self.readings[i] > self.max) :
                    self.max = self.readings[i]
                if(self.readings[i] < self.min) :
                    self.min = self.readings[i]
            self.get_logger().info(f"The readings are :- {self.readings}")
            self.get_logger().info(f"The total sum of the distances captured is :- {self.sum}")
            self.get_logger().info(f"The average distance capture by ultrasomnic sensor is :- {self.sum/len(self.readings)}")
            self.get_logger().info(f"The maximum distance captured by the ultrasonic sensor is :- {self.max}")
            self.get_logger().info(f"The minimum distance captured by the ultrasonic sensor is :- {self.min}")
            self.timer.cancel()
            if rclpy.ok() :
                rclpy.shutdown()
def main(args = None) :
    rclpy.init(args = args)
    node = SensorSimulator()
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