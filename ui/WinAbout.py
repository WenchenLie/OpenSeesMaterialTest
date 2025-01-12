# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'f:\MyProgram\Software\OpenSeesMaterialTest\ui\WinAbout.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_WinAbout(object):
    def setupUi(self, WinAbout):
        WinAbout.setObjectName("WinAbout")
        WinAbout.setWindowModality(QtCore.Qt.NonModal)
        WinAbout.resize(600, 300)
        WinAbout.setMinimumSize(QtCore.QSize(600, 300))
        WinAbout.setMaximumSize(QtCore.QSize(600, 300))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        WinAbout.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("f:\\MyProgram\\Software\\OpenSeesMaterialTest\\ui\\../logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        WinAbout.setWindowIcon(icon)
        WinAbout.setModal(False)
        self.verticalLayout = QtWidgets.QVBoxLayout(WinAbout)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(WinAbout)
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame.setLineWidth(1)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(40, 40, 171, 161))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(80, 80))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("f:\\MyProgram\\Software\\OpenSeesMaterialTest\\ui\\../figures/logo.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(240, 20, 311, 191))
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.frame)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButton = QtWidgets.QPushButton(WinAbout)
        self.pushButton.setMinimumSize(QtCore.QSize(100, 30))
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout.setStretch(0, 6)
        self.verticalLayout.setStretch(1, 1)

        self.retranslateUi(WinAbout)
        self.pushButton.clicked.connect(WinAbout.close) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(WinAbout)

    def retranslateUi(self, WinAbout):
        _translate = QtCore.QCoreApplication.translate
        WinAbout.setWindowTitle(_translate("WinAbout", "关于"))
        self.label_3.setText(_translate("WinAbout", "<html><head/><body><p><span style=\" font-size:14pt;\">OpenSees Material Test<br/><span style=\" font-size:14pt;\">OpenSees材料测试</span></p><p><span style=\" font-size:14pt; color:#000000;\">Copyright (c) data<br/>开发者：列文琛<br/>版本：Version<br/>联系邮箱：438171766@qq.com<br/>QQ：438171766</span></p></body></html>"))
        self.pushButton.setText(_translate("WinAbout", "确认"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    WinAbout = QtWidgets.QDialog()
    ui = Ui_WinAbout()
    ui.setupUi(WinAbout)
    WinAbout.show()
    sys.exit(app.exec_())
