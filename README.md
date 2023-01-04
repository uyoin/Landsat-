# Landsat-TemperatuReretrieval-main
本项目通过Arcpy库实现Landsat影像温度的自动反演，而参数的自动选取则是通过自己编写的主模块外的其他模块实现，所有的一切只需要提供影像所在的目录就好。
# 所需库
``` python
import arcpy
import os
``` 
# 使用
## 打开“main.py”代码，输入以下四个参数即可：
### ①root_dir：影像所在根目录
### ②temp_gdb_path：存放临时处理数据的gdb路径,例如："D:\temp.gdb"（若不存在会自动创建）（结束会自动清理）
### ③result_gdb_path：存放结果的gdb路径,例如："D:\result.gdb"（若不存在会自动创建）
### ④reacher_area：研究区shp的路径，例如："D:\厦门.shp"
# 代码主要功能与实现大致流程原理
本项目由五部分组成：“mian.py”、“initialize.py”、“extractPath.py”，“extractMTLparameter.py”、“getTemp.py”。  
其中“mian.py”是主函数，在此设置程序的主入口，调用“extractPath.py”，“extractMTLparameter.py”、“getTemp.py”所编写的函数进行基于Arcpy库批量自动化温度反演流程。
## initialize.py
“initialize.py”由五个函数组成：create_gdb（gdb_path）、judge_sensor（img_path）、judge_level_frequency（img_path）、judge_level_path（img_path）、level_info（img_path）。  
  ①其中create_gdb（gdb_path）函数主要功能是在gdb_path路径创建文件地理数据库。首先使用arcpy.Exists（）函数检查给定路径的数据库是否已经存在。如果数据库已经存在，则提示“数据库已存在”。如果数据库不存在，则使用arcpy.CreateFileGDB_management（）函数创建新的文件地理数据库。  
  ②judge_sensor（img_path）函数主要功能是判断图像路径下传感器的类型。首先判断输入的图像路径的类型是字符串还是list，如果是字符串则使用extractPath.find_imgName（）函数提取图像名称，根据图像名称的前两个字符判断传感器类型。如果是list则执行步骤对输入的list中的每一个图像路径，使用extractPath.find_imgName（）函数提取图像名称，根据图像名称的前两个字符判断感测器类型。最后，返回感测器类型。  
  ③judge_level_frequency（img_path）函数主要功能是统计该路径下究竟有多少L1与L2级别的图像。首先调用extractPath.find_filesPaths（）函数，查找img_path目录下，所有文件名为“01_T1_MTL.txt”的档案的路径，并将结果存入存入并计算list长度赋值给frequency_L1作为L1图像个数。之后调用extractPath.find_filesPaths（）函数，查找img_path目录下，所有文件名为“MTL.json”的档案的路径，并将结果存入并计算list长度赋值给frequency_L2作为L2图像个数。最后，返回frequency_L1和frequency_L2的值。至于为什么将“01_T1_MTL.txt”作为图像L1级别的识别，将“MTL.json”作为图像L2级别的识别，是因为通过观察地理空间数据云下载的图像发现，这是L1、L2它们独有的文件，可以通过这两个头文件相关文件识别，这样还不用打开MTL文件读取减少内存占用。  
  ④judge_level_path（img_path）函数主要功能是通过查找img_path路径下的档案，找出L1、L2档案的路径，并分别返回到两个list存储。首先调用extractPath.find_filesPaths（）函数，在文件夹img_path中查找满足文件名'01_T1_MTL.txt'的档案，并将查找到的档案路径存储在path_L1中。再次调用extractPath.find_filesPaths（）函数，在文件夹img_path中查找满足文件名'MTL.json'的档案，并将查找到的档案路径存储在清单path_L2中。最后，返回path_L1和path_L2两个不同级别图像的路径list。  
  ⑤level_info（img_path）函数主要功能是整合以上函数，输出提示用户路径下L1与L2图像分别的数量。  
## extractPath.py
“extractPath.py”由两个函数组成：find_filesPaths（root_dir，search_string）、find_imgName（img_path），是重要代码，于多个模块中均会调用此模块中的函数。  
  ①其中find_filesPaths（root_dir，search_string）函数主要功能是根据提供的文件名和路径，提取路径下以及子目录下的文件名与输入文件名匹配的文件名与路径。首先初始化空list，用于保存找到的档案的完整路径和文件名。之后使用os.walk函数遍历指定文件夹及其子文件夹的所有档案，root表示当前遍历到的档案所在目录的路径，dirs表示目前的目录下的所有子文件夹名称，files表示目前的目录下的所有文件名。遍历目前的目录下的所有档案，如果文件名包含指定的搜索字符，则将档案的完整路径和文件名保存到list中，否则直接进入下一个循环。在所有档案都遍历完后，返回保存找到的档案信息的list。  
  ②find_imgName（img_path）函数主要功能是获取img_path路径下图像的名称。首先初始化两个空list，path_list和imgName。之后，判断传入的参数img_path是否为字符串，如果是，则折分字符串，将倒数第二个字符串（图像名）赋值给imgName。如果不是，则进行循环。在循环中，将清单img_path的第i个元素的第一个元素加入到path_list中。将path_list的第i个元素折开为字符串list，并将倒数第二个字符串加入到imgName中。最后，返回列表imgName。  
## extractMTLparameter.py
“extractMTLparameter.py”由两个函数组成：extract_L1values（txt_file_path）、extract_L2values（txt_file_path），是实现根据不同级别图像提取不同方法的核心代码。  
  ①extract_L1values（txt_file_path）函数主要功能是使用已经写好的模块去判断txt_file_path下图像的传感器类型，从而实现不同传感器取参的方式不同，提高泛用性。主要是通过遍历MTL头文件中的每一行，从中分割出每一个单词，并通过判断第一个单词是否等于预定义的字符串来选取出其中的参数值。如果是则提取出后面的参数值，并将其赋值给相应的参数存放，最终进行多个参数的返回。  
  ②extract_L2values（txt_file_path）函数与L1同理。
## getTemp.py
“getTemp.py”由三个函数组成：L1（reacher_area，root_dir，temp_gdb_path，result_gdb_path，i）、L2（reacher_area，root_dir，temp_gdb_path，result_gdb_path，i）、loop（reacher_area，root_dir，temp_gdb_path，result_gdb_path，frequency_L1，frequency_L2）是实现自动批量反演功能的最主要代码，参数传入后的传感器与级别的判断均为以上写好的模块与参数实现，目的就是为了让该代码能够实现自动化的跑动。L1与L2函数的属性与逻辑较为简单都是比较直接没有那麽拐弯抹角因此就不赘述。但值得一提的是Loop函数，它是整个项目代码的集大成者，将所有的自动化批量处理与可视化通过两个for循环实现。
# 致谢
本项目为了实现徐逸祥老师所上的“遥感探测学综合应用”课程的期末汇报而做，感谢老师提供的机会与指导。感谢搭建温度反演模型的刘昕怡同学让我节省了不少时间，有更多的时间可以去做参数方面的自动识别处理。
