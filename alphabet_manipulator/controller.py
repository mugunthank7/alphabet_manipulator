#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from trajectory_msgs.msg import JointTrajectory
from trajectory_msgs.msg import JointTrajectoryPoint
from builtin_interfaces.msg import Duration

from alphabet_manipulator.model import get_alphabet
import time, sys

class Controller(Node):
    def __init__(self):
        super().__init__("arm_move")
        
        self.publisher_ = self.create_publisher(JointTrajectory, '/arm_controller/joint_trajectory', 10)
        self.move()

    def move(self):
        arm_cmd = JointTrajectory()

        arm_point = JointTrajectoryPoint()

        arm_cmd.joint_names = ["hip", "shoulder", "elbow", "wrist"]

        initial = [0.0, 0.0, 0.0, 0.0]

        a1 = [1.0, 0.0, 0.0, 0.0]
        a2 = [1.5, -1.0, 0.0, 0.0]
        a3 = [2.0, 0.0, 0.0, 0.0]
        a4 = [1.25, -0.5, 0.0, 0.0]
        a5 = [1.75, -0.5, 0.0, 0.0]

        t1 = [0.5, 0.0, 0.0, 0.0]
        t2 = [0.75, -0.5, 0.0, 0.0]
        t3 = [0.25, -0.5, 0.0, 0.0]

        h1 = [0.25, 0.0, 0.0, 0.0]
        h2 = [0.25, -0.5, 0.0, 0.0]
        h3 = [0.75, 0.0, 0.0, 0.0]
        h4 = [0.75, -0.5, 0.0, 0.0]
        h5 = [0.75, -0.25, 0.0, 0.0]
        h6 = [0.25, -0.25, 0.0, 0.0]

        l1 = [0.25, -0.25, 0.0, 0.0]
        l2 = [0.25, 0.0, 0.0, 0.0]
        l3 = [0.5, 0.0, 0.0, 0.0]

        e1 = [1.50, 0.0, 0.0, 0.0]
        e2 = [0.50, 0.0, 0.0, 0.0]
        e3 = [0.50, -1.0, 0.0, 0.0]
        e4 = [1.50, -1.0, 0.0, 0.0]
        e5 = [1.50, -0.50, 0.0, 0.0]
        e6 = [0.50, -0.50, 0.0, 0.0]

        f1 = [0.50, 0.0, 0.0, 0.0]
        f2 = [0.50, -1.0, 0.0, 0.0]
        f3 = [1.50, -1.0, 0.0, 0.0]
        f4 = [1.50, -0.50, 0.0, 0.0]
        f5 = [0.50, -0.50, 0.0, 0.0]
        
        # print("Enter an alphabet in A T H L E F :")
        alphabet = get_alphabet(sys.argv[1])  # input()

        arm_point.time_from_start = Duration(sec=2)


        if (alphabet == 'A'):
            arm_point.positions = a1
            arm_cmd.points = [arm_point]
            self.publisher_.publish(arm_cmd)
            time.sleep(3)

            arm_point.positions = a2
            arm_cmd.points = [arm_point]
            self.publisher_.publish(arm_cmd)
            time.sleep(3)

            arm_point.positions = a3
            arm_cmd.points = [arm_point]
            self.publisher_.publish(arm_cmd)
            time.sleep(3)

            arm_point.positions = a4
            arm_cmd.points = [arm_point]
            self.publisher_.publish(arm_cmd)
            time.sleep(3)

            arm_point.positions = a5
            arm_cmd.points = [arm_point]
            self.publisher_.publish(arm_cmd)
            time.sleep(3)

            print("A is published")

            arm_point.positions = initial
            arm_cmd.points = [arm_point]
            self.publisher_.publish(arm_cmd)
            time.sleep(3)

        if (alphabet == 'T'):
            arm_point.positions = t1
            arm_cmd.points = [arm_point]
            self.publisher_.publish(arm_cmd)
            time.sleep(3)

            arm_point.positions = t2
            arm_cmd.points = [arm_point]
            self.publisher_.publish(arm_cmd)
            time.sleep(3)

            arm_point.positions = t3
            arm_cmd.points = [arm_point]
            self.publisher_.publish(arm_cmd)
            time.sleep(3)

            print("T is published")

            arm_point.positions = initial
            arm_cmd.points = [arm_point]
            self.publisher_.publish(arm_cmd)
            time.sleep(3)

        if (alphabet == 'L'):
            arm_point.positions = l1
            arm_cmd.points = [arm_point]
            self.publisher_.publish(arm_cmd)
            time.sleep(3)

            arm_point.positions = l2
            arm_cmd.points = [arm_point]
            self.publisher_.publish(arm_cmd)
            time.sleep(3)

            arm_point.positions = l3
            arm_cmd.points = [arm_point]
            self.publisher_.publish(arm_cmd)
            time.sleep(3)

            print("L is published")

            arm_point.positions = initial
            arm_cmd.points = [arm_point]
            self.publisher_.publish(arm_cmd)
            time.sleep(3)

        if (alphabet == 'H'):
            arm_point.positions = h1
            arm_cmd.points = [arm_point]
            self.publisher_.publish(arm_cmd)
            time.sleep(3)

            arm_point.positions = h2
            arm_cmd.points = [arm_point]
            self.publisher_.publish(arm_cmd)
            time.sleep(3)

            arm_point.positions = h3
            arm_cmd.points = [arm_point]
            self.publisher_.publish(arm_cmd)
            time.sleep(3)

            arm_point.positions = h4
            arm_cmd.points = [arm_point]
            self.publisher_.publish(arm_cmd)
            time.sleep(3)

            arm_point.positions = h5
            arm_cmd.points = [arm_point]
            self.publisher_.publish(arm_cmd)
            time.sleep(3)

            arm_point.positions = h6
            arm_cmd.points = [arm_point]
            self.publisher_.publish(arm_cmd)
            time.sleep(3)

            print("H is published")

            arm_point.positions = initial
            arm_cmd.points = [arm_point]
            self.publisher_.publish(arm_cmd)
            time.sleep(3)

        if (alphabet == 'E'):
            arm_point.positions = e1
            arm_cmd.points = [arm_point]
            self.publisher_.publish(arm_cmd)
            time.sleep(3)

            arm_point.positions = e2
            arm_cmd.points = [arm_point]
            self.publisher_.publish(arm_cmd)
            time.sleep(3)

            arm_point.positions = e3
            arm_cmd.points = [arm_point]
            self.publisher_.publish(arm_cmd)
            time.sleep(3)

            arm_point.positions = e4
            arm_cmd.points = [arm_point]
            self.publisher_.publish(arm_cmd)
            time.sleep(3)

            arm_point.positions = e5
            arm_cmd.points = [arm_point]
            self.publisher_.publish(arm_cmd)
            time.sleep(3)

            arm_point.positions = e6
            arm_cmd.points = [arm_point]
            self.publisher_.publish(arm_cmd)
            time.sleep(3)

            print("E is published")

            arm_point.positions = initial
            arm_cmd.points = [arm_point]
            self.publisher_.publish(arm_cmd)
            time.sleep(3)

        if (alphabet == 'F'):
            arm_point.positions = f1
            arm_cmd.points = [arm_point]
            self.publisher_.publish(arm_cmd)
            time.sleep(3)

            arm_point.positions = f2
            arm_cmd.points = [arm_point]
            self.publisher_.publish(arm_cmd)
            time.sleep(3)

            arm_point.positions = f3
            arm_cmd.points = [arm_point]
            self.publisher_.publish(arm_cmd)
            time.sleep(3)

            arm_point.positions = f4
            arm_cmd.points = [arm_point]
            self.publisher_.publish(arm_cmd)
            time.sleep(3)

            arm_point.positions = f5
            arm_cmd.points = [arm_point]
            self.publisher_.publish(arm_cmd)
            time.sleep(3)

            print("F is published")

            arm_point.positions = initial
            arm_cmd.points = [arm_point]
            self.publisher_.publish(arm_cmd)
            time.sleep(3)
            
            
def main(args=None):
    rclpy.init(args=args)
    controller = Controller()
    
    rclpy.spin(controller)
    rclpy.shutdown()

if __name__ == '__main__':
	main()