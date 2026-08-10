#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from example_interfaces.srv import AddTwoInts
class add_two_ints_serverNode(Node): #Modify Name
    def __init__(self) :
        super().__init__("add_two_ints_server") #Node Name
        self.server_ = self.create_service(AddTwoInts , 'add_two_ints' , self.call_back_add_two_ints)
        self.get_logger().info("Add two ints server has sucessfully created a service")

    def call_back_add_two_ints(self , request: AddTwoInts.Request , response: AddTwoInts.Response):
        response.sum = request.a + request.b
        self.get_logger().info(str(request.a) + " + " +  str(request.b) + " = " + str(response.sum))
        return response


def main(args = None) :
    rclpy.init(args = args)
    node = add_two_ints_serverNode() #Modify Name
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__" :
    main()