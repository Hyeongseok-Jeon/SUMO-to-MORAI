
"use strict";

let VehicleCollision = require('./VehicleCollision.js');
let NpcGhostInfo = require('./NpcGhostInfo.js');
let MapSpec = require('./MapSpec.js');
let MapSpecIndex = require('./MapSpecIndex.js');
let SyncModeCtrlCmd = require('./SyncModeCtrlCmd.js');
let SyncModeCmdResponse = require('./SyncModeCmdResponse.js');
let EgoVehicleStatus = require('./EgoVehicleStatus.js');
let ObjectStatusList = require('./ObjectStatusList.js');
let VehicleSpecIndex = require('./VehicleSpecIndex.js');
let ObjectStatus = require('./ObjectStatus.js');
let GhostMessage = require('./GhostMessage.js');
let MultiEgoSetting = require('./MultiEgoSetting.js');
let ERP42Info = require('./ERP42Info.js');
let SyncModeSetGear = require('./SyncModeSetGear.js');
let MoraiSimProcHandle = require('./MoraiSimProcHandle.js');
let WaitForTickResponse = require('./WaitForTickResponse.js');
let GPSMessage = require('./GPSMessage.js');
let CollisionData = require('./CollisionData.js');
let CtrlCmd = require('./CtrlCmd.js');
let TrafficLight = require('./TrafficLight.js');
let SyncModeCmd = require('./SyncModeCmd.js');
let IntscnTL = require('./IntscnTL.js');
let VehicleCollisionData = require('./VehicleCollisionData.js');
let SensorPosControl = require('./SensorPosControl.js');
let VehicleSpec = require('./VehicleSpec.js');
let EventInfo = require('./EventInfo.js');
let NpcGhostCmd = require('./NpcGhostCmd.js');
let ScenarioLoad = require('./ScenarioLoad.js');
let SyncModeAddObj = require('./SyncModeAddObj.js');
let WaitForTick = require('./WaitForTick.js');
let ReplayInfo = require('./ReplayInfo.js');
let IntersectionControl = require('./IntersectionControl.js');
let SaveSensorData = require('./SaveSensorData.js');
let MoraiTLInfo = require('./MoraiTLInfo.js');
let RadarTracks = require('./RadarTracks.js');
let Lamps = require('./Lamps.js');
let MoraiSrvResponse = require('./MoraiSrvResponse.js');
let MoraiSimProcStatus = require('./MoraiSimProcStatus.js');
let IntersectionStatus = require('./IntersectionStatus.js');
let RadarTrack = require('./RadarTrack.js');
let GetTrafficLightStatus = require('./GetTrafficLightStatus.js');
let SetTrafficLight = require('./SetTrafficLight.js');
let SyncModeRemoveObj = require('./SyncModeRemoveObj.js');
let SyncModeInfo = require('./SyncModeInfo.js');
let MoraiTLIndex = require('./MoraiTLIndex.js');
let SyncModeScenarioLoad = require('./SyncModeScenarioLoad.js');
let SyncModeResultResponse = require('./SyncModeResultResponse.js');

module.exports = {
  VehicleCollision: VehicleCollision,
  NpcGhostInfo: NpcGhostInfo,
  MapSpec: MapSpec,
  MapSpecIndex: MapSpecIndex,
  SyncModeCtrlCmd: SyncModeCtrlCmd,
  SyncModeCmdResponse: SyncModeCmdResponse,
  EgoVehicleStatus: EgoVehicleStatus,
  ObjectStatusList: ObjectStatusList,
  VehicleSpecIndex: VehicleSpecIndex,
  ObjectStatus: ObjectStatus,
  GhostMessage: GhostMessage,
  MultiEgoSetting: MultiEgoSetting,
  ERP42Info: ERP42Info,
  SyncModeSetGear: SyncModeSetGear,
  MoraiSimProcHandle: MoraiSimProcHandle,
  WaitForTickResponse: WaitForTickResponse,
  GPSMessage: GPSMessage,
  CollisionData: CollisionData,
  CtrlCmd: CtrlCmd,
  TrafficLight: TrafficLight,
  SyncModeCmd: SyncModeCmd,
  IntscnTL: IntscnTL,
  VehicleCollisionData: VehicleCollisionData,
  SensorPosControl: SensorPosControl,
  VehicleSpec: VehicleSpec,
  EventInfo: EventInfo,
  NpcGhostCmd: NpcGhostCmd,
  ScenarioLoad: ScenarioLoad,
  SyncModeAddObj: SyncModeAddObj,
  WaitForTick: WaitForTick,
  ReplayInfo: ReplayInfo,
  IntersectionControl: IntersectionControl,
  SaveSensorData: SaveSensorData,
  MoraiTLInfo: MoraiTLInfo,
  RadarTracks: RadarTracks,
  Lamps: Lamps,
  MoraiSrvResponse: MoraiSrvResponse,
  MoraiSimProcStatus: MoraiSimProcStatus,
  IntersectionStatus: IntersectionStatus,
  RadarTrack: RadarTrack,
  GetTrafficLightStatus: GetTrafficLightStatus,
  SetTrafficLight: SetTrafficLight,
  SyncModeRemoveObj: SyncModeRemoveObj,
  SyncModeInfo: SyncModeInfo,
  MoraiTLIndex: MoraiTLIndex,
  SyncModeScenarioLoad: SyncModeScenarioLoad,
  SyncModeResultResponse: SyncModeResultResponse,
};
