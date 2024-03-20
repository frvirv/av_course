#!/usr/bin/env python3

import rclpy
from rclpy.node import Node

from geometry_msgs.msg import Twist


class DrawCircleNode(Node):
    
    def __init__(self):
        super().__init__("draw_circle")
        self.vel_pub_cmd = self.create_publisher(Twist,'/turtle1/cmd_vel',10)
        self._time = self.create_timer(0.5,self.send_velocity_command)
        self.get_logger().info("The node is already started")
        
    def send_velocity_command(self):
        msg = Twist()
        msg.linear.x = 2.0
        msg.angular.z = 1.0
        self.vel_pub_cmd.publish(msg)
        
        



def main(args=None):
    rclpy.init(args=args)
    node = DrawCircleNode()
    rclpy.spin(node)
    ###
    
    rclpy.shutdown()