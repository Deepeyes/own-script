#把当前目录下的文件全部改成txt后缀
import os
import shutil

# 定义源目录和目标后缀
src_dir = r"E:\Downloads\t00lsweb"
dst_ext = ".txt"

# 遍历源目录下的所有文件，并修改文件后缀名
for root, dirs, files in os.walk(src_dir):
    for file in files:
        # 拼接源文件路径和目标文件路径
        src_file = os.path.join(root, file)
        dst_file = os.path.splitext(src_file)[0] + dst_ext
        
        # 修改文件后缀名
        shutil.move(src_file, dst_file)
        print(f"已将 {src_file} 重命名为 {dst_file}")
