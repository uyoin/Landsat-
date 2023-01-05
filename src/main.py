import arcpy
import extractPath
import initialize
import extractMTLparameter
import getTemp
import eliminateOutliers

if __name__ == '__main__':
    root_dir = r"L:\大三课程\【周五早上】遥感探测学综合应用\期末\!Data"
    temp_gdb_path = r"L:\大三课程\【周五早上】遥感探测学综合应用\期末\!Data\temp.gdb"
    result_gdb_path = r"L:\大三课程\【周五早上】遥感探测学综合应用\期末\!Data\result.gdb"
    reacher_area = r"C:\Users\LENOVO\Documents\Tencent Files\183873588\FileRecv\厦门岛\厦门岛.shp"

    frequency_L1, frequency_L2 = initialize.judge_level_frequency(root_dir)

    initialize.level_info(root_dir)
    getTemp.loop(reacher_area, root_dir, temp_gdb_path, result_gdb_path, frequency_L1, frequency_L2)
    # 清理中间产生的临时数据
    arcpy.Delete_management(temp_gdb_path)
