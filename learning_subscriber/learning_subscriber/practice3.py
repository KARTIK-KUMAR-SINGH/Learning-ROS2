#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32


class temprature_sensor(Node) :
    def __init__ (self) :
        super().__init__("temprature_sensore_subscriber_node")
        self.temprature_subscribe = self.create_subscription(
            Float32 ,
            "temprature_sensor_data_topic",
            self.callback,
            10
        )
    def callback(self , msg :Float32) :
        self.get_logger().info(str(round((msg.data) , 2)))
def main(args = None) :
    rclpy.init(args = args)
    node = temprature_sensor()
    try :
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally :
        rclpy.shutdown()
if __name__ == "__main__" :
    main()