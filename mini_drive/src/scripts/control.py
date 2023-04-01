#! /usr/bin/env python
import rospy
from geometry_msgs.msg import Twist, Vector3
from sensor_msgs.msg import Joy

def drive_callback(data):
    global velocity_pub
    
    twist = Twist()
    print(list(data.axes))

    if data.axes[1]>0:
        twist.linear.x = 0.3
        velocity_pub.publish(twist)
        print("Forward")
    elif data.axes[1]<0:
        twist.linear.x = -0.3
        velocity_pub.publish(twist)
        print("Backward")
    elif data.axes[0]>0: #left
        twist = Twist()
        twist.angular.z = 0.5
        velocity_pub.publish(twist)
        print("Left")
    elif data.axes[0]<0: #right
        twist.angular.z = -0.5
        velocity_pub.publish(twist)
        print("Right")
    
    velocity_pub.publish(twist)


# def forward():
#         twist = Twist()
#         twist.linear.x = 0.1
#         velocity_pub.publish(twist)
#         print("Forward")

# def backward():
#         # fw.write("inside--backward\n")
#         twist = Twist()
#         twist.linear.x = -0.1
#         velocity_pub.publish(twist)
#         print("Backward")

# def turnLeft():
#         # fw.write("inside--rotationPositive\n")
#         twist = Twist()
#         twist.angular.z = 0.1
#         velocity_pub.publish(twist)
#         print("Left")

# def turnRight():
#         # fw.write("inside--RotationNegative\n")
#         twist = Twist()
#         twist.angular.z = -0.1
#         velocity_pub.publish(twist)
#         print("Right")

def start():
    velocity_pub = rospy.Publisher("cmd_vel", Twist, queue_size=10)
    # subscribed to joystick inputs on topic "joy"
    rospy.Subscriber('joy', Joy, drive_callback)
    # starts the node
    rospy.init_node('bot_control_node', anonymous=True)
    rospy.spin()

if __name__ == '__main__':
    velocity_pub = rospy.Publisher("cmd_vel", Twist, queue_size=10)
    start()