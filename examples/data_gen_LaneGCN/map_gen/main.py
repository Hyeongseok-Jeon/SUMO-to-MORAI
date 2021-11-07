import numpy as np
import json
from xml.etree.ElementTree import Element, SubElement, ElementTree, dump
# -*-coding:UTF-8 -*-
from scipy.optimize import curve_fit
from matplotlib import pyplot as plt


def indent(elem, level=0):
    i = "\n" + level * "  "
    if len(elem):
        if not elem.text or not elem.text.strip():
            elem.text = i + "  "
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
        for elem in elem:
            indent(elem, level + 1)
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
    else:
        if level and (not elem.tail or not elem.tail.strip()):
            elem.tail = i


def polyfit_with_fixed_points(n, x, y, xf, yf):
    mat = np.empty((n + 1 + len(xf),) * 2)
    vec = np.empty((n + 1 + len(xf),))
    x_n = x ** np.arange(2 * n + 1)[:, None]
    yx_n = np.sum(x_n[:n + 1] * y, axis=1)
    x_n = np.sum(x_n, axis=1)
    idx = np.arange(n + 1) + np.arange(n + 1)[:, None]
    mat[:n + 1, :n + 1] = np.take(x_n, idx)
    xf_n = xf ** np.arange(n + 1)[:, None]
    mat[:n + 1, n + 1:] = xf_n / 2
    mat[n + 1:, :n + 1] = xf_n.T
    mat[n + 1:, n + 1:] = 0
    vec[:n + 1] = yx_n
    vec[n + 1:] = yf
    params = np.linalg.solve(mat, vec)
    return params[:n + 1]


def point_regen(path_length, points_np):
    x_new = []
    y_new = []
    seg_length = path_length / 9
    t = np.linspace(0, 1, len(points_np))
    x = points_np[:, 0]
    y = points_np[:, 1]

    n, d, f = len(t), 7, 2
    params_x = polyfit_with_fixed_points(d, t[1:-1], x[1:-1], np.asarray([t[0], t[-1]]), np.asarray([x[0], x[-1]]))
    poly_x = np.polynomial.Polynomial(params_x)

    params_y = polyfit_with_fixed_points(d, t[1:-1], y[1:-1], np.asarray([t[0], t[-1]]), np.asarray([y[0], y[-1]]))
    poly_y = np.polynomial.Polynomial(params_y)

    t_cand = np.linspace(0, 1, 1001)
    x_cands = poly_x(t_cand)
    y_cands = poly_y(t_cand)
    x_cands[0] = points_np[0, 0]
    x_cands[-1] = points_np[-1, 0]
    y_cands[0] = points_np[0, 1]
    y_cands[-1] = points_np[-1, 1]
    for i in range(len(t_cand)):
        if len(x_new) < 9:
            if i == 0:
                x_new.append(x_cands[i])
                y_new.append(y_cands[i])
            else:
                dist_cnt = np.sqrt(np.sum((x_cands[i] - x_new[-1]) ** 2 + (y_cands[i] - y_new[-1]) ** 2))
                if dist_cnt >= seg_length:
                    x_new.append(x_cands[i])
                    y_new.append(y_cands[i])
        elif len(x_new) == 9:
            x_new.append(x_cands[-1])
            y_new.append(y_cands[-1])
            break
    return np.transpose(np.concatenate((np.array([x_new]), np.array([y_new])), axis=0))


def link_mod(link_tmp, is_turn):
    points_in_link = link_tmp['points']
    points_np = np.array(points_in_link)[:, :2]
    dists = np.linalg.norm(points_np[1:] - points_np[:-1], axis=1)
    path_length = np.sum(np.linalg.norm(points_np[:-1] - points_np[1:], axis=1))
    if is_turn:
        new_points = point_regen(path_length, points_np)
        points_mod = []
        for i in range(len(new_points)):
            wp = [int(10 ** 12 * new_points[i, 0]) / (10 ** 12), int(10 ** 12 * new_points[i, 1]) / (10 ** 12), 0.0]
            points_mod.append(wp)
        link_tmp['points'] = points_mod
        return [link_tmp]
    else:
        seg_num = int(round(path_length / (1.5 * 9)))
        if seg_num == 0:
            seg_num = 1
        seg_length = path_length / seg_num
        child_links = []
        wpts_add = []
        sig = False
        for i in range(len(dists)):
            if len(wpts_add) < seg_num:
                if i == 0:
                    wpts_add.append(i)
                else:
                    dist = np.sum(dists[wpts_add[-1]:i])
                    if dist > seg_length:
                        if sig == True:
                            wpts_add.append(i)
                            sig = False
                        else:
                            wpts_add.append(i)
                            sig = True
            else:
                wpts_add.append(len(dists))
                break

        for i in range(seg_num):
            child_link = dict()
            child_link['idx'] = link_tmp['idx'] + '_' + str(i)
            if i == 0:
                child_link['from_node_idx'] = link_tmp['from_node_idx']
                child_link['to_node_idx'] = link_tmp['to_node_idx'] + '_0'
            elif i == seg_num - 1:
                child_link['from_node_idx'] = child_links[-1]['to_node_idx']
                child_link['to_node_idx'] = link_tmp['to_node_idx']
            else:
                child_link['from_node_idx'] = child_links[-1]['to_node_idx']
                child_link['to_node_idx'] = link_tmp['to_node_idx'] + '_' + str(i)
            if i == seg_num - 1:
                points = points_np[wpts_add[i]: wpts_add[i + 1]]
            else:
                points = points_np[wpts_add[i]: wpts_add[i + 1] + 1]
            path_length = np.sum(np.linalg.norm(points[:-1] - points[1:], axis=1))

            new_points = point_regen(path_length, points)
            mod_points = []
            for k in range(len(new_points)):
                wp = [int(10 ** 12 * new_points[k, 0]) / (10 ** 12), int(10 ** 12 * new_points[k, 1]) / (10 ** 12), 0.0]
                mod_points.append(wp)
            child_link['points'] = mod_points
            child_link['max_speed'] = link_tmp['max_speed']
            child_link['lazy_init'] = link_tmp['lazy_init']
            child_link['can_move_left_lane'] = link_tmp['can_move_left_lane']
            child_link['can_move_right_lane'] = link_tmp['can_move_right_lane']
            child_link['left_lane_change_dst_link_idx'] = link_tmp['left_lane_change_dst_link_idx']
            child_link['right_lane_change_dst_link_idx'] = link_tmp['right_lane_change_dst_link_idx']
            child_link['lane_ch_link_path'] = link_tmp['lane_ch_link_path']
            child_link['link_type'] = link_tmp['link_type']
            child_link['link_type_def'] = link_tmp['link_type_def']
            child_link['road_type'] = link_tmp['road_type']
            child_link['road_id'] = link_tmp['road_id']
            child_link['ego_lane'] = link_tmp['ego_lane']
            child_link['lane_change_dir'] = link_tmp['lane_change_dir']
            child_link['hov'] = link_tmp['hov']
            child_link['geometry'] = link_tmp['geometry']
            child_link['related_signal'] = link_tmp['related_signal']
            child_link['its_link_id'] = link_tmp['its_link_id']
            child_link['force_width_start'] = link_tmp['force_width_start']
            child_link['width_start'] = link_tmp['width_start']
            child_link['force_width_end'] = link_tmp['force_width_end']
            child_link['width_end'] = link_tmp['width_end']
            child_link['enable_side_border'] = link_tmp['enable_side_border']
            child_link['lane_mark_left'] = link_tmp['lane_mark_left']
            child_link['lane_mark_right'] = link_tmp['lane_mark_right']
            child_link['oppTraffic'] = link_tmp['oppTraffic']
            if i == 0:
                child_link['is_entrance'] = link_tmp['is_entrance']
                child_link['is_exit'] = False
            elif i == seg_num - 1:
                child_link['is_entrance'] = False
                child_link['is_exit'] = link_tmp['is_exit']
            else:
                child_link['is_entrance'] = False
                child_link['is_exit'] = False
            child_link['speed_unit'] = link_tmp['idx']
            child_link['speed_start'] = link_tmp['idx']
            child_link['speed_end'] = link_tmp['idx']
            child_link['speed_list'] = link_tmp['idx']
            child_link['recommended_speed'] = link_tmp['idx']
            child_links.append(child_link)
        return child_links


map = 'Suburb_02'
map_abbr = 'SUB'
map_id = '10315'

with open('mgeos/' + map + '/link_set.json') as json_file:
    links = json.load(json_file)
num_orig_link = len(links)
for i in range(num_orig_link):
    link_tmp = links[i]
    idx = i
    if link_tmp['related_signal'] == 'left':
        is_turn = True
    elif link_tmp['related_signal'] == 'straight':
        is_turn = False
    elif link_tmp['related_signal'] == 'right_unprotected':
        is_turn = True
    elif link_tmp['related_signal'] == None:
        is_turn = False
    mod_link = link_mod(link_tmp, is_turn)
    links[i] = mod_link

init = 1
links_new = []
for i in range(len(links)):
    for j in range(len(links[i])):
        if init == 1:
            links_new = links_new + [links[i][j]]
            pt_list = np.array(links[i][j]['points'])[:, :2]
            init = 0
        else:
            links_new = links_new + [links[i][j]]
            pt_list = np.concatenate((pt_list, np.array(links[i][j]['points'])[:, :2]), axis=0)

[_, indexes] = np.unique(pt_list, axis=0, return_index=True)
wps = pt_list[sorted(indexes)]

root = Element('ArgoverseVectorMap')
lane_id_map = dict()

for i in range(len(wps)):
    id = i
    x = wps[i, 0]
    y = wps[i, 1]
    SubElement(root, 'node').attrib = {"id": str(id), "x": str(x), "y": str(y)}

halluc_bbox = np.empty(shape=(len(links_new), 4))
for i in range(len(links_new)):
    link_tmp = links_new[i]
    lane_id = 7000000 + i
    lane_id_map[str(i)] = lane_id
    way = SubElement(root, 'way', lane_id=str(lane_id))
    if link_tmp["related_signal"] == None:
        SubElement(way, 'tag').attrib = {"k": "has_traffic_control", "v": "False"}
    else:
        SubElement(way, 'tag').attrib = {"k": "has_traffic_control", "v": "True"}
    from_node = link_tmp["from_node_idx"]
    to_node = link_tmp["to_node_idx"]
    predecessor = []
    pred_idx = []
    for j in range(len(links_new)):
        predecessor_cand = links_new[j]
        if predecessor_cand["to_node_idx"] == from_node:
            predecessor.append(predecessor_cand)
            pred_idx.append(j)

    successor = []
    suc_idx = []
    for j in range(len(links_new)):
        successor_cand = links_new[j]
        if successor_cand["from_node_idx"] == to_node:
            successor.append(successor_cand)
            suc_idx.append(j)

    if len(predecessor) > 1:
        is_inter = False
        SubElement(way, 'tag').attrib = {"k": "turn_direction", "v": "NONE"}
        SubElement(way, 'tag').attrib = {"k": "is_intersection", "v": "False"}
    elif len(predecessor) == 0:
        is_inter = False
        SubElement(way, 'tag').attrib = {"k": "turn_direction", "v": "NONE"}
        SubElement(way, 'tag').attrib = {"k": "is_intersection", "v": "False"}
    else:
        if predecessor[0]["related_signal"] == 'left':
            is_inter = True
            SubElement(way, 'tag').attrib = {"k": "turn_direction", "v": "LEFT"}
            SubElement(way, 'tag').attrib = {"k": "is_intersection", "v": "True"}
        if predecessor[0]["related_signal"] == 'right_unprotected':
            is_inter = True
            SubElement(way, 'tag').attrib = {"k": "turn_direction", "v": "RIGHT"}
            SubElement(way, 'tag').attrib = {"k": "is_intersection", "v": "True"}
        if predecessor[0]["related_signal"] == 'straight':
            is_inter = True
            SubElement(way, 'tag').attrib = {"k": "turn_direction", "v": "NONE"}
            SubElement(way, 'tag').attrib = {"k": "is_intersection", "v": "True"}
        if predecessor[0]["related_signal"] == None:
            is_inter = False
            SubElement(way, 'tag').attrib = {"k": "turn_direction", "v": "NONE"}
            SubElement(way, 'tag').attrib = {"k": "is_intersection", "v": "False"}

    SubElement(way, 'tag').attrib = {"k": "l_neighbor_id", "v": "None"}
    SubElement(way, 'tag').attrib = {"k": "r_neighbor_id", "v": "None"}
    points_in_link = link_tmp["points"]
    for j in range(len(points_in_link)):
        wps_pt = np.array([points_in_link[j][0], points_in_link[j][1]])
        for z in range(len(wps)):
            wps_cand = wps[z]
            if wps_cand[0] == wps_pt[0] and wps_cand[1] == wps_pt[1]:
                SubElement(way, 'nd').attrib = {"ref": str(z)}
    halluc_bbox[i,0] = np.min(np.asarray(link_tmp["points"])[:,0])
    halluc_bbox[i,1] = np.min(np.asarray(link_tmp["points"])[:,1])
    halluc_bbox[i,2] = np.max(np.asarray(link_tmp["points"])[:,0])
    halluc_bbox[i,3] = np.max(np.asarray(link_tmp["points"])[:,1])

    for j in range(len(predecessor)):
        pred_id = 7000000 + pred_idx[j]
        SubElement(way, 'tag').attrib = {"k": "predecessor", "v": str(pred_id)}

    for j in range(len(successor)):
        suc_id = 7000000 + suc_idx[j]
        SubElement(way, 'tag').attrib = {"k": "successor", "v": str(suc_id)}

indent(root)
dump(root)
tree = ElementTree(root)

xmin = np.min(wps[:, 0])
xmax = np.max(wps[:, 0])
ymin = np.min(wps[:, 1])
ymax = np.max(wps[:, 1])
grid = np.zeros(shape=(int(np.ceil(xmax - xmin)), int(np.ceil(ymax - ymin))))
grid_x = np.zeros(shape=(int(np.ceil(xmax - xmin)), int(np.ceil(ymax - ymin))))
grid_y = np.zeros(shape=(int(np.ceil(xmax - xmin)), int(np.ceil(ymax - ymin))))
drivable_region = np.zeros(shape=(int(np.ceil(xmax - xmin)), int(np.ceil(ymax - ymin))), dtype=np.uint8)
ground_height = np.empty(shape=(int(np.ceil(xmax - xmin)), int(np.ceil(ymax - ymin))), dtype=np.float32)
ground_height[:] = np.nan
city_se2 = np.array([[1, 0, -xmin], [0, 1, -ymin], [0, 0, 1]])

for i in range(grid.shape[0]):
    for j in range(grid.shape[1]):
        x = (i + 1) - 0.5
        y = (j - 58) - 0.5
        grid_x[i, j] = x
        grid_y[i, j] = y
        min_dist_to_wps = np.min(np.linalg.norm(wps - np.array([x, y]), axis=1))
        if min_dist_to_wps < 3.5/2 + 1:
            drivable_region[i,j] = int(1)

tree.write('argoverse_map/pruned_argoverse_' + map_abbr + '_' + map_id + '_vector_map.xml', encoding='utf-8', xml_declaration=True)
with open('argoverse_map/' + map_abbr + '_' + map_id + "_tableidx_to_laneid_map.json", "w") as json_file:
    json.dump(lane_id_map, json_file)
np.save('argoverse_map/' + map_abbr + '_' + map_id + "_npyimage_to_city_se2_2019_05_28.npy", city_se2)
np.save('argoverse_map/' + map_abbr + '_' + map_id + "_driveable_area_mat_2019_05_28.npy", drivable_region)
np.save('argoverse_map/' + map_abbr + '_' + map_id + "_ground_height_mat_2019_05_28.npy", ground_height)
np.save('argoverse_map/' + map_abbr + '_' + map_id + "_halluc_bbox_table.npy", halluc_bbox)
