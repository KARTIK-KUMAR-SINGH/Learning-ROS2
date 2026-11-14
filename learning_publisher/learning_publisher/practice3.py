#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32
import random

class temprature_data(Node) :
    def __init__(self) :
        super().__init__("temprature_sensor")
        self.temp_publish = self.create_publisher(
            Float32 ,
            "temprature_sensor_data_topic",
            10
        )
        
        self.timer = self.create_timer(2 , self.temprature_data)
    def temprature_data(self) :
        msg = Float32()
        self.random_number = round(random.uniform(20 , 40) , 1)
        msg.data = self.random_number
        self.temp_publish.publish(msg)
        self.get_logger().info('publishing :- "%s"' % msg.data)
def main (args = None) :
    rclpy.init(args = args)
    node = temprature_data()
    try :
        rclpy.spin(node)
    except KeyboardInterrupt :
        pass
    finally :
        rclpy.shutdown()
if __name__ == "__main__" :
    main()
