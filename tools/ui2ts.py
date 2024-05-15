from tkinter import filedialog
import os

# pyuic5file = r"E:\PythonEnvs\Python3113\Scripts"  # 笔记本
pylupdate5 = r"C:\Users\admin\.virtualenvs\V2.0-4jnJinpo\Scripts\pylupdate5.exe"  # 大电脑

path = '\\'.join(__file__.split('\\')[:-1]) + '\\ui_file'  # ui文件所在目录
all_files = os.listdir(path)
ui_files = []
for file in all_files:
    if file[-3:] == '.ui':
        ui_files.append(file)
for file in ui_files:
    ui_file = path + '\\' + file
    py_file = ui_file[:-2] + 'py'
    ts_file = ui_file[:-2] + 'ts'
    cmd = pylupdate5 + f' {py_file} -ts {ts_file}'
    # print(cmd)
    os.system(cmd)
print('完成！')