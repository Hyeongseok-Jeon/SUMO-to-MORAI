;; Auto-generated. Do not edit!


(when (boundp 'morai_msgs::GhostMessage)
  (if (not (find-package "MORAI_MSGS"))
    (make-package "MORAI_MSGS"))
  (shadow 'GhostMessage (find-package "MORAI_MSGS")))
(unless (find-package "MORAI_MSGS::GHOSTMESSAGE")
  (make-package "MORAI_MSGS::GHOSTMESSAGE"))

(in-package "ROS")
;;//! \htmlinclude GhostMessage.msg.html
(if (not (find-package "GEOMETRY_MSGS"))
  (ros::roseus-add-msgs "geometry_msgs"))


(defclass morai_msgs::GhostMessage
  :super ros::object
  :slots (_position _heading ))

(defmethod morai_msgs::GhostMessage
  (:init
   (&key
    ((:position __position) (instance geometry_msgs::Vector3 :init))
    ((:heading __heading) 0.0)
    )
   (send-super :init)
   (setq _position __position)
   (setq _heading (float __heading))
   self)
  (:position
   (&rest __position)
   (if (keywordp (car __position))
       (send* _position __position)
     (progn
       (if __position (setq _position (car __position)))
       _position)))
  (:heading
   (&optional __heading)
   (if __heading (setq _heading __heading)) _heading)
  (:serialization-length
   ()
   (+
    ;; geometry_msgs/Vector3 _position
    (send _position :serialization-length)
    ;; float64 _heading
    8
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; geometry_msgs/Vector3 _position
       (send _position :serialize s)
     ;; float64 _heading
       (sys::poke _heading (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; geometry_msgs/Vector3 _position
     (send _position :deserialize buf ptr-) (incf ptr- (send _position :serialization-length))
   ;; float64 _heading
     (setq _heading (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;;
   self)
  )

(setf (get morai_msgs::GhostMessage :md5sum-) "b7529b96025c54855f296c4413ac7578")
(setf (get morai_msgs::GhostMessage :datatype-) "morai_msgs/GhostMessage")
(setf (get morai_msgs::GhostMessage :definition-)
      "geometry_msgs/Vector3 position

float64 heading
================================================================================
MSG: geometry_msgs/Vector3
# This represents a vector in free space. 
# It is only meant to represent a direction. Therefore, it does not
# make sense to apply a translation to it (e.g., when applying a 
# generic rigid transformation to a Vector3, tf2 will only apply the
# rotation). If you want your data to be translatable too, use the
# geometry_msgs/Point message instead.

float64 x
float64 y
float64 z
")



(provide :morai_msgs/GhostMessage "b7529b96025c54855f296c4413ac7578")


