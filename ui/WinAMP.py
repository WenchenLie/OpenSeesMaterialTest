# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'f:\MyProgram\Software\OpenSeesMaterialTest\ui\WinAMP.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_WinAMP(object):
    def setupUi(self, WinAMP):
        WinAMP.setObjectName("WinAMP")
        WinAMP.resize(318, 500)
        WinAMP.setMinimumSize(QtCore.QSize(0, 500))
        WinAMP.setMaximumSize(QtCore.QSize(318, 500))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        WinAMP.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("f:\\MyProgram\\Software\\OpenSeesMaterialTest\\ui\\../logo.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        WinAMP.setWindowIcon(icon)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(WinAMP)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.groupBox = QtWidgets.QGroupBox(WinAMP)
        self.groupBox.setMinimumSize(QtCore.QSize(0, 100))
        self.groupBox.setMaximumSize(QtCore.QSize(16777215, 100))
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setMinimumSize(QtCore.QSize(0, 30))
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setMinimumSize(QtCore.QSize(0, 30))
        self.label.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit.setMinimumSize(QtCore.QSize(0, 30))
        self.lineEdit.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 1)
        self.verticalLayout_2.addWidget(self.groupBox)
        self.table = QtWidgets.QTableWidget(WinAMP)
        self.table.setMinimumSize(QtCore.QSize(200, 0))
        self.table.setFrameShape(QtWidgets.QFrame.Box)
        self.table.setLineWidth(1)
        self.table.setAutoScrollMargin(16)
        self.table.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.table.setShowGrid(True)
        self.table.setGridStyle(QtCore.Qt.SolidLine)
        self.table.setWordWrap(True)
        self.table.setCornerButtonEnabled(True)
        self.table.setRowCount(300)
        self.table.setColumnCount(1)
        self.table.setObjectName("table")
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        item.setFont(font)
        self.table.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setItem(2, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setItem(3, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setItem(4, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setItem(5, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setItem(6, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setItem(7, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setItem(8, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setItem(9, 0, item)
        self.table.horizontalHeader().setVisible(True)
        self.table.horizontalHeader().setCascadingSectionResizes(False)
        self.table.horizontalHeader().setDefaultSectionSize(250)
        self.table.horizontalHeader().setMinimumSectionSize(25)
        self.table.horizontalHeader().setSortIndicatorShown(False)
        self.table.horizontalHeader().setStretchLastSection(True)
        self.table.verticalHeader().setVisible(True)
        self.table.verticalHeader().setCascadingSectionResizes(False)
        self.table.verticalHeader().setDefaultSectionSize(30)
        self.table.verticalHeader().setHighlightSections(True)
        self.table.verticalHeader().setMinimumSectionSize(15)
        self.table.verticalHeader().setSortIndicatorShown(False)
        self.table.verticalHeader().setStretchLastSection(False)
        self.verticalLayout_2.addWidget(self.table)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_2 = QtWidgets.QPushButton(WinAMP)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_2.addWidget(self.pushButton_2)
        self.pushButton = QtWidgets.QPushButton(WinAMP)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_2.addWidget(self.pushButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.retranslateUi(WinAMP)
        self.pushButton.clicked.connect(self.table.clearContents) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(WinAMP)

    def retranslateUi(self, WinAMP):
        _translate = QtCore.QCoreApplication.translate
        WinAMP.setWindowTitle(_translate("WinAMP", "定义位移幅值"))
        self.groupBox.setTitle(_translate("WinAMP", "提示"))
        self.label_2.setText(_translate("WinAMP", "在表格中输入加载制度曲线的反向点对应的位移（如：0,5,0,-5,0)。"))
        self.label.setText(_translate("WinAMP", "最小位移增量："))
        self.lineEdit.setText(_translate("WinAMP", "0.1"))
        self.table.setSortingEnabled(False)
        item = self.table.horizontalHeaderItem(0)
        item.setText(_translate("WinAMP", "位移幅值"))
        __sortingEnabled = self.table.isSortingEnabled()
        self.table.setSortingEnabled(False)
        self.table.setSortingEnabled(__sortingEnabled)
        self.pushButton_2.setText(_translate("WinAMP", "确认"))
        self.pushButton.setText(_translate("WinAMP", "清空"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    WinAMP = QtWidgets.QDialog()
    ui = Ui_WinAMP()
    ui.setupUi(WinAMP)
    WinAMP.show()
    sys.exit(app.exec_())
