; Auto-generated. Do not edit!


(cl:in-package morai_msgs-srv)


;//! \htmlinclude MoraiSimpProcSrv-request.msg.html

(cl:defclass <MoraiSimpProcSrv-request> (roslisp-msg-protocol:ros-message)
  ((request
    :reader request
    :initarg :request
    :type morai_msgs-msg:MoraiSimProcHandle
    :initform (cl:make-instance 'morai_msgs-msg:MoraiSimProcHandle)))
)

(cl:defclass MoraiSimpProcSrv-request (<MoraiSimpProcSrv-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <MoraiSimpProcSrv-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'MoraiSimpProcSrv-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name morai_msgs-srv:<MoraiSimpProcSrv-request> is deprecated: use morai_msgs-srv:MoraiSimpProcSrv-request instead.")))

(cl:ensure-generic-function 'request-val :lambda-list '(m))
(cl:defmethod request-val ((m <MoraiSimpProcSrv-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader morai_msgs-srv:request-val is deprecated.  Use morai_msgs-srv:request instead.")
  (request m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <MoraiSimpProcSrv-request>) ostream)
  "Serializes a message object of type '<MoraiSimpProcSrv-request>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'request) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <MoraiSimpProcSrv-request>) istream)
  "Deserializes a message object of type '<MoraiSimpProcSrv-request>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'request) istream)
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<MoraiSimpProcSrv-request>)))
  "Returns string type for a service object of type '<MoraiSimpProcSrv-request>"
  "morai_msgs/MoraiSimpProcSrvRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'MoraiSimpProcSrv-request)))
  "Returns string type for a service object of type 'MoraiSimpProcSrv-request"
  "morai_msgs/MoraiSimpProcSrvRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<MoraiSimpProcSrv-request>)))
  "Returns md5sum for a message object of type '<MoraiSimpProcSrv-request>"
  "6d340598acf4b7d6e6f913c45512bf48")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'MoraiSimpProcSrv-request)))
  "Returns md5sum for a message object of type 'MoraiSimpProcSrv-request"
  "6d340598acf4b7d6e6f913c45512bf48")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<MoraiSimpProcSrv-request>)))
  "Returns full string definition for message of type '<MoraiSimpProcSrv-request>"
  (cl:format cl:nil "MoraiSimProcHandle request~%~%================================================================================~%MSG: morai_msgs/MoraiSimProcHandle~%uint8 sim_process_status~%~%int16 replay_option~%string rosbag_file_name~%int16 replay_target_option~%~%int32 replay_speed~%int32 start_time~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'MoraiSimpProcSrv-request)))
  "Returns full string definition for message of type 'MoraiSimpProcSrv-request"
  (cl:format cl:nil "MoraiSimProcHandle request~%~%================================================================================~%MSG: morai_msgs/MoraiSimProcHandle~%uint8 sim_process_status~%~%int16 replay_option~%string rosbag_file_name~%int16 replay_target_option~%~%int32 replay_speed~%int32 start_time~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <MoraiSimpProcSrv-request>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'request))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <MoraiSimpProcSrv-request>))
  "Converts a ROS message object to a list"
  (cl:list 'MoraiSimpProcSrv-request
    (cl:cons ':request (request msg))
))
;//! \htmlinclude MoraiSimpProcSrv-response.msg.html

(cl:defclass <MoraiSimpProcSrv-response> (roslisp-msg-protocol:ros-message)
  ((response
    :reader response
    :initarg :response
    :type morai_msgs-msg:MoraiSrvResponse
    :initform (cl:make-instance 'morai_msgs-msg:MoraiSrvResponse)))
)

(cl:defclass MoraiSimpProcSrv-response (<MoraiSimpProcSrv-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <MoraiSimpProcSrv-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'MoraiSimpProcSrv-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name morai_msgs-srv:<MoraiSimpProcSrv-response> is deprecated: use morai_msgs-srv:MoraiSimpProcSrv-response instead.")))

(cl:ensure-generic-function 'response-val :lambda-list '(m))
(cl:defmethod response-val ((m <MoraiSimpProcSrv-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader morai_msgs-srv:response-val is deprecated.  Use morai_msgs-srv:response instead.")
  (response m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <MoraiSimpProcSrv-response>) ostream)
  "Serializes a message object of type '<MoraiSimpProcSrv-response>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'response) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <MoraiSimpProcSrv-response>) istream)
  "Deserializes a message object of type '<MoraiSimpProcSrv-response>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'response) istream)
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<MoraiSimpProcSrv-response>)))
  "Returns string type for a service object of type '<MoraiSimpProcSrv-response>"
  "morai_msgs/MoraiSimpProcSrvResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'MoraiSimpProcSrv-response)))
  "Returns string type for a service object of type 'MoraiSimpProcSrv-response"
  "morai_msgs/MoraiSimpProcSrvResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<MoraiSimpProcSrv-response>)))
  "Returns md5sum for a message object of type '<MoraiSimpProcSrv-response>"
  "6d340598acf4b7d6e6f913c45512bf48")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'MoraiSimpProcSrv-response)))
  "Returns md5sum for a message object of type 'MoraiSimpProcSrv-response"
  "6d340598acf4b7d6e6f913c45512bf48")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<MoraiSimpProcSrv-response>)))
  "Returns full string definition for message of type '<MoraiSimpProcSrv-response>"
  (cl:format cl:nil "MoraiSrvResponse response~%~%~%================================================================================~%MSG: morai_msgs/MoraiSrvResponse~%bool result~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'MoraiSimpProcSrv-response)))
  "Returns full string definition for message of type 'MoraiSimpProcSrv-response"
  (cl:format cl:nil "MoraiSrvResponse response~%~%~%================================================================================~%MSG: morai_msgs/MoraiSrvResponse~%bool result~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <MoraiSimpProcSrv-response>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'response))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <MoraiSimpProcSrv-response>))
  "Converts a ROS message object to a list"
  (cl:list 'MoraiSimpProcSrv-response
    (cl:cons ':response (response msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'MoraiSimpProcSrv)))
  'MoraiSimpProcSrv-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'MoraiSimpProcSrv)))
  'MoraiSimpProcSrv-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'MoraiSimpProcSrv)))
  "Returns string type for a service object of type '<MoraiSimpProcSrv>"
  "morai_msgs/MoraiSimpProcSrv")