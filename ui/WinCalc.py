# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'f:\MyProgram\Software\OpenSeesMaterialTest\ui\WinCalc.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_WinCalc(object):
    def setupUi(self, WinCalc):
        WinCalc.setObjectName("WinCalc")
        WinCalc.resize(700, 500)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        WinCalc.setFont(font)
        WinCalc.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("f:\\MyProgram\\Software\\OpenSeesMaterialTest\\ui\\../logo.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        WinCalc.setWindowIcon(icon)
        WinCalc.setModal(True)
        self.label = QtWidgets.QLabel(WinCalc)
        self.label.setGeometry(QtCore.QRect(240, 220, 241, 51))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(28)
        self.label.setFont(font)
        self.label.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(WinCalc)
        self.pushButton.setGeometry(QtCore.QRect(10, 460, 100, 30))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(WinCalc)
        QtCore.QMetaObject.connectSlotsByName(WinCalc)

    def retranslateUi(self, WinCalc):
        _translate = QtCore.QCoreApplication.translate
        WinCalc.setWindowTitle(_translate("WinCalc", "正在调用openseespy进行计算"))
        self.label.setText(_translate("WinCalc", "正在计算。。。"))
        self.pushButton.setText(_translate("WinCalc", "中断"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    WinCalc = QtWidgets.QDialog()
    ui = Ui_WinCalc()
    ui.setupUi(WinCalc)
    WinCalc.show()
    sys.exit(app.exec_())
