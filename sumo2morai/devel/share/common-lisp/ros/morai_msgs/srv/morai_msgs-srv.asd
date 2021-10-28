
(cl:in-package :asdf)

(defsystem "morai_msgs-srv"
  :depends-on (:roslisp-msg-protocol :roslisp-utils :morai_msgs-msg
)
  :components ((:file "_package")
    (:file "MoraiEventCmdSrv" :depends-on ("_package_MoraiEventCmdSrv"))
    (:file "_package_MoraiEventCmdSrv" :depends-on ("_package"))
    (:file "MoraiMapSpecSrv" :depends-on ("_package_MoraiMapSpecSrv"))
    (:file "_package_MoraiMapSpecSrv" :depends-on ("_package"))
    (:file "MoraiScenarioLoadSrv" :depends-on ("_package_MoraiScenarioLoadSrv"))
    (:file "_package_MoraiScenarioLoadSrv" :depends-on ("_package"))
    (:file "MoraiSimpProcSrv" :depends-on ("_package_MoraiSimpProcSrv"))
    (:file "_package_MoraiSimpProcSrv" :depends-on ("_package"))
    (:file "MoraiSyncModeCmdSrv" :depends-on ("_package_MoraiSyncModeCmdSrv"))
    (:file "_package_MoraiSyncModeCmdSrv" :depends-on ("_package"))
    (:file "MoraiSyncModeCtrlCmdSrv" :depends-on ("_package_MoraiSyncModeCtrlCmdSrv"))
    (:file "_package_MoraiSyncModeCtrlCmdSrv" :depends-on ("_package"))
    (:file "MoraiSyncModeSLSrv" :depends-on ("_package_MoraiSyncModeSLSrv"))
    (:file "_package_MoraiSyncModeSLSrv" :depends-on ("_package"))
    (:file "MoraiSyncModeSetGearSrv" :depends-on ("_package_MoraiSyncModeSetGearSrv"))
    (:file "_package_MoraiSyncModeSetGearSrv" :depends-on ("_package"))
    (:file "MoraiTLInfoSrv" :depends-on ("_package_MoraiTLInfoSrv"))
    (:file "_package_MoraiTLInfoSrv" :depends-on ("_package"))
    (:file "MoraiVehicleSpecSrv" :depends-on ("_package_MoraiVehicleSpecSrv"))
    (:file "_package_MoraiVehicleSpecSrv" :depends-on ("_package"))
    (:file "MoraiWaitForTickSrv" :depends-on ("_package_MoraiWaitForTickSrv"))
    (:file "_package_MoraiWaitForTickSrv" :depends-on ("_package"))
  ))