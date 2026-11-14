#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from std_msgs.msg import Int16

class Counting(Node) :
    def __init__(self) :
        super().__init__("counter_node")
        self.count_publisher = self.create_publisher(
            Int16,
            'counting_topic' ,
            10
        )
        self.count = 1
        self.timer = self.create_timer(1 , self.counting_numbers)
        self.get_logger().info("The counter node has started and has stsrted publishing counting values on the TOPIC named :- counting")
    def counting_numbers(self) :
        msg = Int16()
        msg.data = self.count
        self.count += 1
        if(self.count > 20):
            self.count = 1
        self.count_publisher.publish(msg)
        self.get_logger().info('publishing :- "%s"' % msg.data)
def main(args = None) :
    rclpy.init(args = args)
    node = Counting()
    try :
        rclpy.spin(node)
    except KeyboardInterrupt :
        pass
    finally :
        if rclpy.ok() :
            rclpy.shutdown()
if __name__ == "__main__" :
    main()