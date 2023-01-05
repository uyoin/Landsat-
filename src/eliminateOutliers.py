# -*- coding: utf-8 -*-
import arcpy

def eli_normal(image_path):
    arcpy.env.overwriteOutput = True
    # # 打开影像数据
    image_raster = arcpy.Raster(image_path)
    # 计算影像中温度值的平均值
    mean_temp = float(arcpy.GetRasterProperties_management(image_raster, "MEAN").getOutput(0))
    # 计算影像中温度值的标准差
    stddev_temp = float(arcpy.GetRasterProperties_management(image_raster, "STD").getOutput(0))
    # 定义极端值的范围
    lower_bound = mean_temp - 2 * stddev_temp
    upper_bound = mean_temp + 2 * stddev_temp
    # 将异常值替换为 NoData 值
    image_raster = arcpy.sa.SetNull(arcpy.sa.IsNull(image_raster) | (image_raster < lower_bound) | (image_raster > upper_bound), image_raster)
    # 定义保存路径
    output_path = r'L:\大三课程\【周五早上】遥感探测学综合应用\期末\!Data\output_image.tif'
    # 保存处理后的影像
    image_raster.save(output_path)
    # 定义点数据的输出路径
    point_data_path = r'L:\大三课程\point_data.shp'
    # 将影像栅格转换为点数据
    arcpy.RasterToPoint_conversion(output_path, point_data_path, "VALUE")
    # 定义插值结果的输出路径
    interpolated_raster_path = r'L:\大三课程\czLC09_L2SP_119043_20220821_20220823_02_T1_temp.tif'
    # 使用 Empirical Bayesian Kriging - Advanced 方法进行插值
    arcpy.EmpiricalBayesianKriging_ga(point_data_path, "grid_code", interpolated_raster_path)


if __name__ == '__main__':

    eli_normal(r'L:\大三课程\【周五早上】遥感探测学综合应用\期末\!Data\result.gdb\LC81190432016209LGN01_temp')