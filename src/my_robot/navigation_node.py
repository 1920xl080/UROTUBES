import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from time import sleep

class SimpleTeleop(Node):
    def __init__(self):
        super().__init__('simple_teleop')
        self.publisher = self.create_publisher(Twist, '/cmd_vel', 10)
        self.timer = self.create_timer(0.1, self.timer_callback)

    def timer_callback(self):
        twist = Twist()
        twist.linear.x = 0.2  # Move forward
        twist.angular.z = 0.0  # No rotation
        self.publisher.publish(twist)

def main(args=None):
    rclpy.init(args=args)
    node = SimpleTeleop()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
