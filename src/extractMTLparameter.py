import extractPath
import initialize


def extract_L1values(txt_file_path):
    if initialize.judge_sensor(txt_file_path) == "OLI":
        # open the txt file and read each line
        with open(txt_file_path, 'r') as txt_file:
            for line in txt_file:
                # split the line into words
                words = line.split()
                # check if the first word is "REFLECTANCE_MULT_BAND_3="
                if words[0] == 'REFLECTANCE_MULT_BAND_3' and words[1] == '=':
                    # if it is, extract the value after the equals sign
                    refl_mult_b3 = words[2]
                # check if the first word is "REFLECTANCE_ADD_BAND_3="
                elif words[0] == 'REFLECTANCE_ADD_BAND_3' and words[1] == '=':
                    # if it is, extract the value after the equals sign
                    refl_add_b3 = words[2]
                # check if the first word is "QUANTIZE_CAL_MAX_BAND_6="
                elif words[0] == 'QUANTIZE_CAL_MAX_BAND_6' and words[1] == '=':
                    # if it is, extract the value after the equals sign
                    QCA_max_b6 = words[2]
                # check if the first word is "QUANTIZE_CAL_MIN_BAND_6="
                elif words[0] == 'QUANTIZE_CAL_MIN_BAND_6' and words[1] == '=':
                    # if it is, extract the value after the equals sign
                    QCA_min_b6 = words[2]
                # check if the first word is "RADIANCE_MAXIMUM_BAND_6="
                elif words[0] == 'RADIANCE_MAXIMUM_BAND_6' and words[1] == '=':
                    # if it is, extract the value after the equals sign
                    radiance_max = words[2]
                # check if the first word is "RADIANCE_MINIMUM_BAND_6="
                elif words[0] == 'RADIANCE_MINIMUM_BAND_6' and words[1] == '=':
                    # if it is, extract the value after the equals sign
                    radiance_min = words[2]
                # check if the first word is "K1_CONSTANT_BAND_10 ="
                elif words[0] == 'K1_CONSTANT_BAND_10' and words[1] == '=':
                    # if it is, extract the value after the equals sign
                    k1_b6 = words[2]
                # check if the first word is "K2_CONSTANT_BAND_10 ="
                elif words[0] == 'K2_CONSTANT_BAND_10' and words[1] == '=':
                    # if it is, extract the value after the equals sign
                    k2_b6 = words[2]
    elif initialize.judge_sensor(txt_file_path) == "ETM+":
        # open the txt file and read each line
        with open(txt_file_path, 'r') as txt_file:
            for line in txt_file:
                # split the line into words
                words = line.split()
                # check if the first word is "REFLECTANCE_MULT_BAND_3="
                if words[0] == 'REFLECTANCE_MULT_BAND_3' and words[1] == '=':
                    # if it is, extract the value after the equals sign
                    refl_mult_b3 = words[2]
                # check if the first word is "REFLECTANCE_ADD_BAND_3="
                elif words[0] == 'REFLECTANCE_ADD_BAND_3' and words[1] == '=':
                    # if it is, extract the value after the equals sign
                    refl_add_b3 = words[2]
                # check if the first word is "QUANTIZE_CAL_MAX_BAND_6="
                elif words[0] == 'QUANTIZE_CAL_MAX_BAND_6_VCID_1' and words[1] == '=':
                    # if it is, extract the value after the equals sign
                    QCA_max_b6 = words[2]
                # check if the first word is "QUANTIZE_CAL_MIN_BAND_6="
                elif words[0] == 'QUANTIZE_CAL_MIN_BAND_6_VCID_1' and words[1] == '=':
                    # if it is, extract the value after the equals sign
                    QCA_min_b6 = words[2]
                # check if the first word is "RADIANCE_MAXIMUM_BAND_6="
                elif words[0] == 'RADIANCE_MAXIMUM_BAND_6_VCID_1' and words[1] == '=':
                    # if it is, extract the value after the equals sign
                    radiance_max = words[2]
                # check if the first word is "RADIANCE_MINIMUM_BAND_6="
                elif words[0] == 'RADIANCE_MINIMUM_BAND_6_VCID_1' and words[1] == '=':
                    # if it is, extract the value after the equals sign
                    radiance_min = words[2]
                # check if the first word is "K1_CONSTANT_BAND_6="
                elif words[0] == 'K1_CONSTANT_BAND_6_VCID_1' and words[1] == '=':
                    # if it is, extract the value after the equals sign
                    k1_b6 = words[2]
                # check if the first word is "K2_CONSTANT_BAND_6="
                elif words[0] == 'K2_CONSTANT_BAND_6_VCID_1' and words[1] == '=':
                    # if it is, extract the value after the equals sign
                    k2_b6 = words[2]
    elif initialize.judge_sensor(txt_file_path) == "TM":
        # open the txt file and read each line
        with open(txt_file_path, 'r') as txt_file:
            for line in txt_file:
                # split the line into words
                words = line.split()
                # check if the first word is "REFLECTANCE_MULT_BAND_3="
                if words[0] == 'REFLECTANCE_MULT_BAND_3' and words[1] == '=':
                    # if it is, extract the value after the equals sign
                    refl_mult_b3 = words[2]
                # check if the first word is "REFLECTANCE_ADD_BAND_3="
                elif words[0] == 'REFLECTANCE_ADD_BAND_3' and words[1] == '=':
                    # if it is, extract the value after the equals sign
                    refl_add_b3 = words[2]
                # check if the first word is "QUANTIZE_CAL_MAX_BAND_6="
                elif words[0] == 'QUANTIZE_CAL_MAX_BAND_6' and words[1] == '=':
                    # if it is, extract the value after the equals sign
                    QCA_max_b6 = words[2]
                # check if the first word is "QUANTIZE_CAL_MIN_BAND_6="
                elif words[0] == 'QUANTIZE_CAL_MIN_BAND_6' and words[1] == '=':
                    # if it is, extract the value after the equals sign
                    QCA_min_b6 = words[2]
                # check if the first word is "RADIANCE_MAXIMUM_BAND_6="
                elif words[0] == 'RADIANCE_MAXIMUM_BAND_6' and words[1] == '=':
                    # if it is, extract the value after the equals sign
                    radiance_max = words[2]
                # check if the first word is "RADIANCE_MINIMUM_BAND_6="
                elif words[0] == 'RADIANCE_MINIMUM_BAND_6' and words[1] == '=':
                    # if it is, extract the value after the equals sign
                    radiance_min = words[2]
                # check if the first word is "K1_CONSTANT_BAND_6="
                elif words[0] == 'K1_CONSTANT_BAND_6' and words[1] == '=':
                    # if it is, extract the value after the equals sign
                    k1_b6 = words[2]
                # check if the first word is "K2_CONSTANT_BAND_6="
                elif words[0] == 'K2_CONSTANT_BAND_6' and words[1] == '=':
                    # if it is, extract the value after the equals sign
                    k2_b6 = words[2]

    # return the values as a tuple
    return refl_mult_b3, refl_add_b3, QCA_max_b6, QCA_min_b6, radiance_max, radiance_min, k1_b6, k2_b6


def extract_L2values(txt_file_path):
    if initialize.judge_sensor(txt_file_path) == "OLI":
        # open the txt file and read each line
        with open(txt_file_path, 'r') as txt_file:
            for line in txt_file:
                # split the line into words
                words = line.split()
                # check if the first word is "TEMPERATURE_MAXIMUM_BAND_ST_B10_3="
                if words[0] == 'TEMPERATURE_MAXIMUM_BAND_ST_B10' and words[1] == '=':
                    # if it is, extract the value after the equals sign
                    temp_maximum = words[2]
                # check if the first word is "TEMPERATURE_MINIMUM_BAND_ST_B10="
                elif words[0] == 'TEMPERATURE_MINIMUM_BAND_ST_B10' and words[1] == '=':
                    # if it is, extract the value after the equals sign
                    temp_minimum = words[2]
                # check if the first word is "TEMPERATURE_MULT_BAND_ST_B10="
                elif words[0] == 'TEMPERATURE_MULT_BAND_ST_B10' and words[1] == '=':
                    # if it is, extract the value after the equals sign
                    temp_mult = words[2]

    elif initialize.judge_sensor(txt_file_path) == "TM" or "ETM+":
        # open the txt file and read each line
        with open(txt_file_path, 'r') as txt_file:
            for line in txt_file:
                # split the line into words
                words = line.split()
                # check if the first word is "TEMPERATURE_MAXIMUM_BAND_ST_B6="
                if words[0] == 'TEMPERATURE_MAXIMUM_BAND_ST_B6' and words[1] == '=':
                    # if it is, extract the value after the equals sign
                    temp_maximum = words[2]
                # check if the first word is "TEMPERATURE_MINIMUM_BAND_ST_B6="
                elif words[0] == 'TEMPERATURE_MINIMUM_BAND_ST_B6' and words[1] == '=':
                    # if it is, extract the value after the equals sign
                    temp_minimum = words[2]
                # check if the first word is "TEMPERATURE_MULT_BAND_ST_B6="
                elif words[0] == 'TEMPERATURE_MULT_BAND_ST_B6' and words[1] == '=':
                    # if it is, extract the value after the equals sign
                    temp_mult = words[2]
    return temp_maximum, temp_minimum, temp_mult
# root_dir = "L:\大三课程\【周五早上】遥感探测学综合应用\期末\新建文件夹"
# mtl_path = extractPath.find_filesPaths(root_dir, "MTL")
# refl_mult_b3, refl_add_b3,QCA_max_b6,QCA_min_b6,radiance_max,radiance_min,k1_b6,k2_b6 = extract_values(mtl_path[0][0])
