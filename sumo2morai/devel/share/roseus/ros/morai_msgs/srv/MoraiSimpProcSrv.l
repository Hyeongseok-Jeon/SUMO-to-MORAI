;; Auto-generated. Do not edit!


(when (boundp 'morai_msgs::MoraiSimpProcSrv)
  (if (not (find-package "MORAI_MSGS"))
    (make-package "MORAI_MSGS"))
  (shadow 'MoraiSimpProcSrv (find-package "MORAI_MSGS")))
(unless (find-package "MORAI_MSGS::MORAISIMPPROCSRV")
  (make-package "MORAI_MSGS::MORAISIMPPROCSRV"))
(unless (find-package "MORAI_MSGS::MORAISIMPPROCSRVREQUEST")
  (make-package "MORAI_MSGS::MORAISIMPPROCSRVREQUEST"))
(unless (find-package "MORAI_MSGS::MORAISIMPPROCSRVRESPONSE")
  (make-package "MORAI_MSGS::MORAISIMPPROCSRVRESPONSE"))

(in-package "ROS")





(defclass morai_msgs::MoraiSimpProcSrvRequest
  :super ros::object
  :slots (_request ))

(defmethod morai_msgs::MoraiSimpProcSrvRequest
  (:init
   (&key
    ((:request __request) (instance morai_msgs::MoraiSimProcHandle :init))
    )
   (send-super :init)
   (setq _request __request)
   self)
  (:request
   (&rest __request)
   (if (keywordp (car __request))
       (send* _request __request)
     (progn
       (if __request (setq _request (car __request)))
       _request)))
  (:serialization-length
   ()
   (+
    ;; morai_msgs/MoraiSimProcHandle _request
    (send _request :serialization-length)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; morai_msgs/MoraiSimProcHandle _request
       (send _request :serialize s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; morai_msgs/MoraiSimProcHandle _request
     (send _request :deserialize buf ptr-) (incf ptr- (send _request :serialization-length))
   ;;
   self)
  )

(defclass morai_msgs::MoraiSimpProcSrvResponse
  :super ros::object
  :slots (_response ))

(defmethod morai_msgs::MoraiSimpProcSrvResponse
  (:init
   (&key
    ((:response __response) (instance morai_msgs::MoraiSrvResponse :init))
    )
   (send-super :init)
   (setq _response __response)
   self)
  (:response
   (&rest __response)
   (if (keywordp (car __response))
       (send* _response __response)
     (progn
       (if __response (setq _response (car __response)))
       _response)))
  (:serialization-length
   ()
   (+
    ;; morai_msgs/MoraiSrvResponse _response
    (send _response :serialization-length)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; morai_msgs/MoraiSrvResponse _response
       (send _response :serialize s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; morai_msgs/MoraiSrvResponse _response
     (send _response :deserialize buf ptr-) (incf ptr- (send _response :serialization-length))
   ;;
   self)
  )

(defclass morai_msgs::MoraiSimpProcSrv
  :super ros::object
  :slots ())

(setf (get morai_msgs::MoraiSimpProcSrv :md5sum-) "6d340598acf4b7d6e6f913c45512bf48")
(setf (get morai_msgs::MoraiSimpProcSrv :datatype-) "morai_msgs/MoraiSimpProcSrv")
(setf (get morai_msgs::MoraiSimpProcSrv :request) morai_msgs::MoraiSimpProcSrvRequest)
(setf (get morai_msgs::MoraiSimpProcSrv :response) morai_msgs::MoraiSimpProcSrvResponse)

(defmethod morai_msgs::MoraiSimpProcSrvRequest
  (:response () (instance morai_msgs::MoraiSimpProcSrvResponse :init)))

(setf (get morai_msgs::MoraiSimpProcSrvRequest :md5sum-) "6d340598acf4b7d6e6f913c45512bf48")
(setf (get morai_msgs::MoraiSimpProcSrvRequest :datatype-) "morai_msgs/MoraiSimpProcSrvRequest")
(setf (get morai_msgs::MoraiSimpProcSrvRequest :definition-)
      "MoraiSimProcHandle request

================================================================================
MSG: morai_msgs/MoraiSimProcHandle
uint8 sim_process_status

int16 replay_option
string rosbag_file_name
int16 replay_target_option

int32 replay_speed
int32 start_time
---
MoraiSrvResponse response


================================================================================
MSG: morai_msgs/MoraiSrvResponse
bool result
")

(setf (get morai_msgs::MoraiSimpProcSrvResponse :md5sum-) "6d340598acf4b7d6e6f913c45512bf48")
(setf (get morai_msgs::MoraiSimpProcSrvResponse :datatype-) "morai_msgs/MoraiSimpProcSrvResponse")
(setf (get morai_msgs::MoraiSimpProcSrvResponse :definition-)
      "MoraiSimProcHandle request

================================================================================
MSG: morai_msgs/MoraiSimProcHandle
uint8 sim_process_status

int16 replay_option
string rosbag_file_name
int16 replay_target_option

int32 replay_speed
int32 start_time
---
MoraiSrvResponse response


================================================================================
MSG: morai_msgs/MoraiSrvResponse
bool result
")



(provide :morai_msgs/MoraiSimpProcSrv "6d340598acf4b7d6e6f913c45512bf48")


