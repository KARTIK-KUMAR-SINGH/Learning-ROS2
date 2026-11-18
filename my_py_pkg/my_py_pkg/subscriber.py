#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32

class subscriber_node(Node) :
    def __init__(self) :
        super().__init__("subscribing_testing_node")
        self.get_logger().info("subscriber node has started and ready to subscribe to the publihung topic PUBLISHING TOPIC")
        self.subscribing = self.create_subscription(
            Int32 ,
            "publishing_topic" ,
            self.callback ,
            10
        )
    def callback(self , msg : Int32) :
        self.get_logger().info('subscribed data got from topic :- "%s"' % msg.data)
def main(args = None) :
    rclpy.init(args = args)
    node = subscriber_node()
    try :
        rclpy.spin(node)
    except KeyboardInterrupt :
        pass
    finally :
        node.destroy_node()
        if rclpy.ok() :
            rclpy.shutdown()
if __name__ == "__main__" :
    main()