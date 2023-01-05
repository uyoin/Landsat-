# -*- coding: utf-8 -*-
import arcpy
import os
import extractPath


def create_gdb(gdb_path):
    # 检查数据库是否已经存在
    if arcpy.Exists(gdb_path):
        print("数据库已存在")
    else:
        # 创建数据库
        arcpy.CreateFileGDB_management(out_folder_path=os.path.dirname(gdb_path), out_name=os.path.basename(gdb_path))
        print("数据库创建成功")


def judge_sensor(img_path):
    sensor = []
    if type(img_path) == str:
        imgName = extractPath.find_imgName(img_path)
        if imgName[0:2] == "LC":
            sensor = "OLI"
        elif imgName[0:2] == "LE":
            sensor = "ETM+"
        elif imgName[0:2] == "LT":
            sensor = "TM"
    else:
        for i in range(len(img_path)):
            imgName[i] = extractPath.find_imgName(img_path[i][0])
            if imgName[i][0:2] == "LC":
                sensor[i] = "OLI"
            elif imgName[i][0:2] == "LE":
                sensor[i] = "ETM+"
            elif imgName[i][0:2] == "LT":
                sensor[i] = "TM"
    return sensor


def judge_level_frequency(img_path):
    frequency_L1 = len(extractPath.find_filesPaths(img_path, 'L1GT'))
    frequency_L1 = len(extractPath.find_filesPaths(img_path, 'LGN00_MTL.txt'))
    frequency_L2 = len(extractPath.find_filesPaths(img_path, 'MTL.json'))
    return frequency_L1, frequency_L2


def judge_level_path(img_path):
    path_L1 = extractPath.find_filesPaths(img_path, 'L1GT')
    path_L1 = extractPath.find_filesPaths(img_path, 'LGN00_MTL.txt')
    path_L2 = extractPath.find_filesPaths(img_path, 'MTL.json')
    return path_L1, path_L2


def level_info(img_path):
    frequency_L1, frequency_L2 = judge_level_frequency(img_path)
    print("该文件目录下共有 " + str(frequency_L1 + frequency_L2) + " 个Landsat影像")
    print("其中有 " + str(frequency_L1) + " 个 L1 影像" + ", " + str(frequency_L2) + " 个 L2 影像")
    print("L1影像使用单窗法反演，L2影像使用直接法反演")
