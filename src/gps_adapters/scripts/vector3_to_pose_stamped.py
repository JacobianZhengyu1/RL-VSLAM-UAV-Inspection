#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import rospy
from geometry_msgs.msg import Vector3, PoseStamped, Quaternion
from std_msgs.msg import Header

def main():
    rospy.init_node('vector3_to_pose_stamped')

    # 参数可由 launch 覆盖
    in_topic  = rospy.get_param('~in_topic',  '/gps/position')
    out_topic = rospy.get_param('~out_topic', '/gps')
    frame_id  = rospy.get_param('~frame_id',  'map')

    pub = rospy.Publisher(out_topic, PoseStamped, queue_size=10)

    def cb(msg):
        ps = PoseStamped()
        ps.header = Header(stamp=rospy.Time.now(), frame_id=frame_id)
        ps.pose.position.x = msg.x
        ps.pose.position.y = msg.y
        ps.pose.position.z = msg.z
        ps.pose.orientation = Quaternion(0.0, 0.0, 0.0, 1.0)  # 单位四元数
        pub.publish(ps)

    rospy.Subscriber(in_topic, Vector3, cb, queue_size=50)
    rospy.loginfo("Vector3→PoseStamped: %s -> %s [frame_id=%s]", in_topic, out_topic, frame_id)
    rospy.spin()

if __name__ == '__main__':
    main()

