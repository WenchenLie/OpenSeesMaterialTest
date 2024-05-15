from pathlib import Path
import os

# pyuic5file = r"E:\PythonEnvs\Python3113\Scripts"  # 笔记本
pyuic5file = r"D:\Python311\Scripts"  # 大电脑

path = Path(__file__).parent.parent / 'ui'
ui_files: list[Path] = []
for file in path.iterdir():
    if file.suffix == '.ui':
        ui_files.append(file)
for file in ui_files:
    ui_file = file.absolute()
    py_file = ui_file.parent / (ui_file.stem + '.py')
    cmd = pyuic5file + f'\\pyuic5 -x {ui_file} -o {py_file}'
    os.system(cmd)
print('完成！')