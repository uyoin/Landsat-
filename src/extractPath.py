import os


def find_filesPaths(root_dir, search_string):
    # 初始化空文件路径list
    file_paths = []

    # 遍历所有根目录与子目录
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            # 检查文件名是否包括search_string传入的参数（模糊文件名）
            if search_string in file:
                # 如果有，将完整的文件路径和文件名append到list中，组合成元胞
                file_paths.append((os.path.join(root, file), file))
            # 否则直接进入下一个循环

    return file_paths


def find_imgName(img_path):
    path_list = []
    imgName = []
    if type(img_path) == str:
        path_split = img_path.split('\\')
        imgName = path_split[-2]
    else:
        for i in range(len(img_path)):
            path_list.append(img_path[i][0])
            path_split = path_list[i].split('\\')
            imgName.append(path_split[-2])

    return imgName
# root_dir = 'L:\大三课程\【周五早上】遥感探测学综合应用\期末\!Data'
# search_string = 'B3'
# file_paths = find_filesPaths(root_dir, search_string)
# imgname = find_imgName(file_paths)
# print(file_paths[0][1])
# print(imgname)
