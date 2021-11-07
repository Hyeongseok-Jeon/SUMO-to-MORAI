#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import optparse
import rospy
import numpy as np
import time
import threading

from geometry_msgs.msg import PoseStamped
from math import pi
from morai_msgs.msg import ObjectStatusList
from multiprocessing import Process, Pipe
import csv

gen_sig = 0
data_pool = []

def get_pos(data, timestep, veh_id):
    for i in range(len(data[timestep]['data'].npc_list)):
        if veh_id == data[timestep]['data'].npc_list[i].unique_id:
            veh_pos = np.array([data[timestep]['data'].npc_list[i].position.x, data[timestep]['data'].npc_list[i].position.y])
            break
    return veh_pos

def select_AV_TV(data, full_vehs):
    AV = []
    TV = []
    for i in range(len(full_vehs)):
        AV_cands = full_vehs[i]
        idx_rand = np.arange(len(full_vehs))
        np.random.shuffle(idx_rand)
        for j in range(len(full_vehs)):
            TV_cands = full_vehs[idx_rand[j]]
            if AV_cands != TV_cands:
                AV_pos = get_pos(data, 19, AV_cands)
                TV_pos = get_pos(data, 19, TV_cands)
                if np.linalg.norm(AV_pos-TV_pos) < 20:
                    AV.append(AV_cands)
                    TV.append(TV_cands)
    return AV, TV

def get_full_veh(data):
    ego_cands = []
    for i in range(len(data[19]['data'].npc_list)):
        cand = data[19]['data'].npc_list[i].unique_id
        cand_sig = True
        for j in range(50):
            step_check = True
            for z in range(len(data[j]['data'].npc_list)):
                if cand == data[j]['data'].npc_list[z].unique_id:
                    break
                else:
                   if z == len(data[j]['data'].npc_list)-1:
                       step_check = False
            if step_check == False:
                cand_sig = False
        if cand_sig == True:
            ego_cands.append(cand)
    return ego_cands

class data_get(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        rospy.init_node('receivew', anonymous=True)
        rospy.Subscriber("/Object_topic", ObjectStatusList, self.objCB)
        rospy.spin()
        

    def objCB(self,data):
        global gen_sig
        global data_pool
        cur_time = time.time()
        print(cur_time)
        data_tmp = {'time':cur_time, 'data':data}
        if len(data_pool) < 50:
            gen_sig = 0
            data_pool.append(data_tmp)
        elif len(data_pool) == 50:
            save_idx = np.random.rand(1)
            if save_idx > 0.8:
                gen_sig = 1
            else:
                gen_sig = 0
            data_pool[:49] = data_pool[1:]
            data_pool[49] = data_tmp


class data_save(threading.Thread):
    def __init__(self):
        print('start')
        threading.Thread.__init__(self)

    def run(self):
        global gen_sig
        global data_pool
        data_idx = 0
        while True:
            if gen_sig == 1:
                data_now = data_pool.copy()
                data_idx = self.save(data_now,data_idx)

    def save(self, data, data_idx):
        full_vehs = get_full_veh(data)
        AV, TV = select_AV_TV(data, full_vehs)
    
        for ii in range(len(AV)):
            f = open('../gen_data/'+str(data_idx)+'.csv','w', newline='')
            wr = csv.writer(f)
            wr.writerow(['TIMESTAMP', 'TRACK_ID', 'OBJECT_TYPE', 'X', 'Y', 'CITY_NAME'])
            AV_id = AV[ii]
            TV_id = TV[ii]
            for i in range(50):
                cur_time = data[i]['time']
                cur_data = data[i]['data'].npc_list
                for k in range(len(cur_data)):
                    timestep = i
                    veh_id = data[i]['data'].npc_list[k].unique_id
                    veh_pos = get_pos(data, timestep, veh_id)
                    if veh_id == AV_id:
                        veh_id = '00000000-0000-0000-0000-000000000000'
                        obj_type = 'AV'
                        wr.writerow([cur_time, veh_id, obj_type, veh_pos[0], veh_pos[1], 'SUB'])
                    elif veh_id == TV_id:
                        veh_id = '00000000-0000-0000-0000-'+'0'*(12-len(str(veh_id))) + str(veh_id)
                        obj_type = 'AGENT'
                        wr.writerow([cur_time, veh_id, obj_type, veh_pos[0], veh_pos[1], 'SUB'])
                    else:
                        if np.linalg.norm(veh_pos - get_pos(data, timestep, AV_id)) < 50:
                            veh_id = '00000000-0000-0000-0000-'+'0'*(12-len(str(veh_id))) + str(veh_id)
                            obj_type = 'OTHERS'
                            wr.writerow([cur_time, veh_id, obj_type, veh_pos[0], veh_pos[1], 'SUB'])
                
            f.close()
            data_idx = data_idx + 1
        return data_idx


if __name__ == '__main__':
    data_parse_save = data_save()
    data_parse_save.start()
    data_receive = data_get()
    data_receive.start()

