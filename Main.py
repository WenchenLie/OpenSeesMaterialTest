from sys import argv as sysargv, exit as sysexit
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QCoreApplication
from core.Win import Win


if __name__ == '__main__':

    QCoreApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    app = QApplication(sysargv)
    myshow = Win()
    myshow.show()
    sysexit(app.exec_())



"""
第三方库：
pyqt5
numpy
matplotlib
openseespy
pyinstaller

版本更新日志：
V1.0（2023-08-29）：初代版本，开发环境为Python3.10.11 + PyQt5 + openseespy3.5.1.3。
V2.0（2023-08-31）：增加了菜单栏、用户文档、件信息、跳转至OS和OSPy网站的选项，优化了ui在不同分辨率显示器上的显示问题。
V2.1（2023-09-01）：增加了语言选择（X）
V2.2（2023-09-07）：优化了画图框的显式效果
V2.3（2024-05-15）：优化代码，增加了一些类型注解
"""