
(cl:in-package :asdf)

(defsystem "sumo2morai_tutorial-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils :geometry_msgs-msg
               :std_msgs-msg
)
  :components ((:file "_package")
    (:file "NpcGhostCmd" :depends-on ("_package_NpcGhostCmd"))
    (:file "_package_NpcGhostCmd" :depends-on ("_package"))
    (:file "NpcGhostInfo" :depends-on ("_package_NpcGhostInfo"))
    (:file "_package_NpcGhostInfo" :depends-on ("_package"))
    (:file "Num" :depends-on ("_package_Num"))
    (:file "_package_Num" :depends-on ("_package"))
  ))