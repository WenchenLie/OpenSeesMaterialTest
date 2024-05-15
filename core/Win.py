import numpy as np
from ui.MainWin import Ui_MainWindow
from ui.WinOSPara import Ui_WinOSPara
from ui.WinAMP import Ui_WinAMP
from ui.WinCalc import Ui_WinCalc
from ui.WinData import Ui_WinGetData
from ui.WinAbout import Ui_WinAbout
from ui.WinHelp import Ui_WinHelp
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PyQt5.QtGui import QKeySequence, QDesktopServices
from PyQt5.QtCore import QThread, pyqtSignal, Qt, QPoint, QEvent, QCoreApplication, QUrl, QTranslator
from PyQt5.QtWidgets import QApplication, QMessageBox, QFileDialog, QDialog, QTableWidgetItem, QMainWindow, QMenu, QSizePolicy
from core.generate_AMP import generate_AMP
from core.ThreadRunOS import ThreadRunOS


VERSION = 'V2.3'
DATE = '2024.05.15'

# class Win(QWidget):
class Win(QMainWindow):
    LANGUAGE = 'zh'
    u_pre, u_exp, F_pre, F_exp, u = None, None, None, None, None
    u_from = 'test'  # 使用的位移是来自试验还是生成（test / amp）

    def __init__(self):
        super().__init__()
        self.init_ui()  # 初始化界面
        self.init_var()  # 初始化变量

    def init_ui(self):
        self.ui = Ui_MainWindow()  # 主窗口
        self.ui.setupUi(self)
        self.setWindowTitle(f"OpenSees材料测试软件 {VERSION}")
        self.ui.btn_getTestCurve.clicked.connect(self.click_btn_getTestCurve)  # 导入试验滞回曲线
        self.ui.btn_inputMatPara.clicked.connect(self.click_btn_inputMatPara)  # 输入材料参数
        self.ui.btn_defineAMP.clicked.connect(self.click_btn_defineAMP)  # 定义位移幅值
        self.ui.btn_GenerateProtocol.clicked.connect(self.click_btn_GenerateProtocol)  # 生成加载制度
        self.ui.btn_PlotCurve.clicked.connect(self.click_btn_PlotCurve)  # 绘制滞回曲线
        self.ui.btn_getData.clicked.connect(self.clicked_btn_getData)  # 查看滞回曲线数据
        self.ui.action_2.triggered.connect(self.triggered_1)  # 帮助-关于
        self.ui.action_1.triggered.connect(self.triggered_2)  # 帮助-帮助文档
        self.ui.action_6.triggered.connect(self.OpenOSPyUrl)  # 打开OpenSeesPy官网
        self.ui.action_7.triggered.connect(self.OpenOSUrl)  # 打开OpenSees官网
        # self.ui.action_Chinese.triggered.connect(self.translate_to_Chinese)  # 中文模式
        # self.ui.action_English.triggered.connect(self.translate_to_English)  # 中文模式
        self.trans = QTranslator()
        self.ui.rbtn_FromTest.pressed.connect(self.press_rbtn_FromTest)
        self.ui.rbtn_FromAMP.pressed.connect(self.press_rbtn_FromAMP)
        self.ui.statusBar.showMessage(f'OpenSees材料测试 {VERSION}')
        self.fig, self.ax = plt.subplots()
        self.ui.verticalLayout.removeWidget(self.ui.graph_protocol)
        self.ui.graph_protocol.deleteLater()  # 将原ui中的graph_protocol对象删除
        self.ui.graph_protocol = FigureCanvas(self.fig)
        self.fig.tight_layout()
        self.ui.verticalLayout.insertWidget(3, self.ui.graph_protocol)
        for i in range(4):
            self.ui.verticalLayout.setStretch(i, [0, 0, 0, 1][i])
        self.fig1, self.ax1 = plt.subplots()
        self.ui.verticalLayout_3.removeWidget(self.ui.graph_Curve)
        self.ui.graph_Curve.deleteLater()  # 将原ui中的graph_Curve对象删除
        self.ui.graph_Curve = FigureCanvas(self.fig1)  # 向原ui添加FigureCanvas对象，用来嵌入matplotlib
        self.fig1.tight_layout()
        self.ui.verticalLayout_3.insertWidget(0, self.ui.graph_Curve)
        for i in range(3):
            self.ui.verticalLayout_3.setStretch(i, [1, 0, 0][i])
        for i in range(3):
            self.ui.horizontalLayout_2.setStretch(i, [2, 0, 3][i])

    def init_var(self):
        # 初始化变量
        self.para = [300, 150, 0.02]  # opensees材料参数
        self.ui.ledit_OSModel.text()
        self.u0 = [0, 5, 0, -5, 0, 20, 0, -20, 0]  # 默认位移幅值点
        self.du0 = 0.5  # 默认最小位移增量
        self.plot_finished = False  # 是否完成滞回曲线绘制

    def triggered_1(self):
        # 显示关于窗口
        self.win_help = Win_about()
        self.win_help.exec_()

    def triggered_2(self):
        # 打开帮助文档
        self.win_about = Win_help()
        self.win_about.exec_()

    def click_btn_getTestCurve(self):
        curve_path, _ = QFileDialog.getOpenFileName(self, "选择文件（两列，一列位移，一列力）", "", "文本文档 (*.txt)")
        if curve_path == "":
            # QMessageBox.information(self, "提示", "没有选择文件")
            pass
        else:
            try:
                self.TestData = np.loadtxt(curve_path)
                Win.u_exp = self.TestData[:, 0]
                Win.F_exp = self.TestData[:, 1]
                self.ui.label.setText(f"已导入（{curve_path.split('/')[-1]}）")
            except:
                QMessageBox.warning(self, "警告", '无法读取文件！\n（.txt文件应仅包括两列数据，第一列位移，第二列为力，建议直接从excel复制.txt文件！）')
        # print(self.win_AMP.AMP)

    def click_btn_inputMatPara(self):
        # 打开输入opensees材料参数窗口
        self.win_OSpara = Win_OSpara()
        self.win_OSpara.exec_()
        self.para = []
        for i in self.win_OSpara.para:
            try:
                self.para.append(float(i))
            except:
                self.para.append(i)

    def press_rbtn_FromTest(self):
        self.ui.btn_defineAMP.setEnabled(False)

    def press_rbtn_FromAMP(self):
        self.ui.btn_defineAMP.setEnabled(True)

    def click_btn_defineAMP(self):
        self.win_AMP = Win_AMP()
        self.win_AMP.exec()
        self.u0 = self.win_AMP.AMP
        self.du0 = self.win_AMP.du

    def click_btn_GenerateProtocol(self):
        if self.ui.rbtn_FromTest.isChecked():
            # 加载制度来自试验数据
            if Win.u_exp is None:
                QMessageBox.warning(self, "警告", "未导入试验数据！")
                return 0
            else:
                Win.u = Win.u_exp
                Win.u_from = 'test'
        else:
            # 加载制度通过生成获得
            try:
                self.u0 = [float(i) for i in self.u0]
            except:
                QMessageBox.warning(self, '警告', '位移幅值输入有误！')
                return 0
            if self.u0 == []:
                QMessageBox.warning(self, '警告', '位移幅值输入有误！')
                return 0
            Win.u_pre = generate_AMP(self.u0, self.du0)
            Win.u = Win.u_pre
            Win.u_from = 'amp'
        self.ax.clear()
        self.ax.plot(np.arange(0, len(Win.u), 1), Win.u)
        self.ui.graph_protocol.draw()

    def click_btn_PlotCurve(self):
        if Win.u is None:
            QMessageBox.warning(self, '警告', '请首先生成加载制度！')
            return 0
        self.Mat_name = self.ui.ledit_OSModel.text()  # 获取材料名
        self.thread_ctrl = Thread_ctrl(Win.u, self.para, self.Mat_name)
        self.win_calc = Win_calc()
        self.win_calc.signal_kill.connect(self.thread_ctrl.thread.stop)
        self.thread_ctrl.thread.signal_finish.connect(self.get_OS_result)
        self.thread_ctrl.thread.signal_OS_error.connect(self.win_calc.OS_error)
        self.thread_ctrl.thread_start()
        self.win_calc.exec()

    def get_OS_result(self, result):
        # signal_finish的槽函数
        self.win_calc.accept()
        Win.F_pre = result
        self.ax1.clear()
        if Win.u_from == 'test':
            self.ax1.plot(Win.u_exp, Win.F_exp, label='Experimental')
        if not Win.F_pre == []:
            self.ax1.plot(Win.u, Win.F_pre, label='Predictional')
            self.ax1.legend()
            self.ui.graph_Curve.draw()
            self.plot_finished = True  # 已完成绘制
            self.result_statistics()  # 输出结果

    def result_statistics(self):
        max_u, min_u = round(max(Win.u), 4), round(min(Win.u), 4)
        max_F_pre, min_F_pre = round(max(Win.F_pre), 4), round(min(Win.F_pre), 4)
        self.ui.lineEdit.setText(str(min_u))
        self.ui.lineEdit_2.setText(str(max_u))
        self.ui.lineEdit_3.setText(str(min_F_pre))
        self.ui.lineEdit_4.setText(str(max_F_pre))
        if Win.u_from == 'test':
            # 如果有试验数据
            max_F_exp, min_F_exp = round(max(Win.F_exp), 4), round(min(Win.F_exp), 4)
            self.ui.lineEdit_5.setText(str(min_F_exp))
            self.ui.lineEdit_6.setText(str(max_F_exp))
            std = round(np.std(Win.F_exp), 4)  # 试验标准差
            RMSE = round(np.sqrt(np.sum(Win.F_exp - Win.F_pre) ** 2) / len(Win.F_exp), 4)  # 均方根误差
            NRMSE = round(RMSE / std, 4)  # 归一化均方根误差
            self.ui.lineEdit_8.setText(str(RMSE))
            self.ui.lineEdit_7.setText(str(NRMSE))
        else:
            self.ui.lineEdit_5.clear()
            self.ui.lineEdit_6.clear()
            self.ui.lineEdit_8.clear()
            self.ui.lineEdit_7.clear()

    def clicked_btn_getData(self):
        # 查看滞回曲线数据
        self.win_getData = Win_getData(self.plot_finished, Win.u, Win.F_pre)
        self.win_getData.exec()
    
    def OpenOSPyUrl(self):
        QDesktopServices.openUrl(QUrl("https://openseespydoc.readthedocs.io/en/latest/src/uniaxialMaterial.html"))

    def OpenOSUrl(self):
        QDesktopServices.openUrl(QUrl("https://opensees.berkeley.edu/wiki/index.php/UniaxialMaterial_Command"))

class Win_OSpara(QDialog):
    # 输入材料参数表格
    last_para = [300, 150, 0.02]

    def __init__(self):
        super().__init__()
        self.ui_OSpara = Ui_WinOSPara()  # 输入OpenSees材料参数的窗口
        self.ui_OSpara.setupUi(self)
        self.ui_OSpara.pushButton_2.clicked.connect(self.submit)
        self.init_table_with_last_data()
        self.init_setLanguage()
        if Win.LANGUAGE == 'zh':
            self.ui_OSpara.table.horizontalHeaderItem(0).setText(QCoreApplication.translate("win_OSpara", "输入材料参数\n（不包括材料名和编号）"))
        elif Win.LANGUAGE == 'eng':
            self.ui_OSpara.table.horizontalHeaderItem(0).setText(QCoreApplication.translate("win_OSpara", "Input material parameters\n(Excluding type and tag)"))

    def init_table_with_last_data(self):
        # 打开表格时自动填入数据
        for row, val in enumerate(self.last_para):
            item = QTableWidgetItem(str(val))
            self.ui_OSpara.table.setItem(row, 0, item)
        self.para = []  # 初始化opensees材料参数

    def init_setLanguage(self):
        self.trans = QTranslator()
        if Win.LANGUAGE == 'zh':
            self.trans.load('zh_CN')
            _app = QApplication.instance()
            _app.installTranslator(self.trans)
            self.ui_OSpara.retranslateUi(self)
        elif Win.LANGUAGE == 'eng':
            self.trans.load('trans/win_OSpara.qm')
            _app = QApplication.instance()
            _app.installTranslator(self.trans)
            self.ui_OSpara.retranslateUi(self)

    def submit(self):
        para = []
        for i in range(self.ui_OSpara.table.rowCount()):
            para.append(self.ui_OSpara.table.item(i, 0).text() if self.ui_OSpara.table.item(i, 0) else '')
        for val in para:
            if not val == '':
                self.para.append(val)
        Win_OSpara.last_para = self.para  # 使表格每次打开自动显示上次的数据
        self.accept()
        
class Win_AMP(QDialog):
    # 输入位移幅值表格
    last_AMP = [0, 5, 0, -5, 0, 20, 0, -20, 0]
    last_du = 0.5

    def __init__(self):
        super().__init__()
        self.ui_AMP = Ui_WinAMP()  # 输入OpenSees材料参数的窗口
        self.ui_AMP.setupUi(self)
        self.ui_AMP.table.setContextMenuPolicy(Qt.CustomContextMenu)
        self.ui_AMP.table.customContextMenuRequested.connect(self.showContextMenu)
        self.ui_AMP.table.itemClicked.connect(self.ensure_table_item)
        self.ui_AMP.table.installEventFilter(self)
        self.ui_AMP.pushButton_2.clicked.connect(self.submit)
        self.init_table_with_last_data()
        self.init_last_du()
        self.init_setLanguage()

    def init_table_with_last_data(self):
        # 打开窗口时自动填入数据
        for row, val in enumerate(self.last_AMP):
            item = QTableWidgetItem(str(val))
            self.ui_AMP.table.setItem(row, 0, item)
        self.ui_AMP.lineEdit.setText(str(self.last_du))
        self.AMP = []  # 初始化opensees材料参数

    def init_setLanguage(self):
        self.trans = QTranslator()
        if Win.LANGUAGE == 'zh':
            self.trans.load('zh_CN')
            _app = QApplication.instance()
            _app.installTranslator(self.trans)
            self.ui_AMP.retranslateUi(self)
        elif Win.LANGUAGE == 'eng':
            self.trans.load('trans/win_AMP.qm')
            _app = QApplication.instance()
            _app.installTranslator(self.trans)
            self.ui_AMP.retranslateUi(self)

    def init_last_du(self):
        # 打开窗口时自动填入du
        self.du = 0.5

    def submit(self):
        AMP = []
        for i in range(self.ui_AMP.table.rowCount()):
            AMP.append(self.ui_AMP.table.item(i, 0).text() if self.ui_AMP.table.item(i, 0) else '')
        for val in AMP:
            if not val == '':
                self.AMP.append(val)
        self.du = self.ui_AMP.lineEdit.text()
        Win_AMP.last_AMP = self.AMP  # 使表格每次打开自动显示上次的数据(更新类变量)
        Win_AMP.last_du = self.du  # 更新类变量
        if len(Win_AMP.last_AMP) == 0:
            pass
        elif not Win_AMP.last_AMP[0] == '0':
            QMessageBox.warning(self, "警告", "强烈建议将第一个位移幅值设为0！")
        self.accept()

    def ensure_table_item(self, item):
        row = item.row()
        column = item.column()
        if self.ui_AMP.table.item(row, column) is None:
            self.ui_AMP.table.setItem(row, column, QTableWidgetItem(""))

    def pasteData(self):
        clipboard = QApplication.clipboard().text()
        rows = clipboard.split("\n")
        # 获取当前选中的行
        start_row = self.ui_AMP.table.currentRow()
        if start_row == -1:  # 如果没有选中行，从第0行开始
            start_row = 0
        for i, row in enumerate(rows):
            if row:
                row_index = start_row + i
                item = QTableWidgetItem(row)
                self.ui_AMP.table.setItem(row_index, 0, item)

    def showContextMenu(self, pos):
        context_menu = QMenu(self)
        paste_action = context_menu.addAction("粘贴")
        action = context_menu.exec_(self.ui_AMP.table.mapToGlobal(pos))
        if action == paste_action:
            self.pasteData()

    def eventFilter(self, source, event):
        if event.type() == QEvent.KeyPress and event.matches(QKeySequence.Paste):
            self.pasteData()
            return True
        return super(Win_AMP, self).eventFilter(source, event)
    

class Win_calc(QDialog):
    signal_kill = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.ui_calc = Ui_WinCalc()  # 开始计算时弹出窗口
        self.ui_calc.setupUi(self)
        self.ui_calc.pushButton.clicked.connect(self.kill)  # 终止按钮
        self.init_setLanguage()

    def init_setLanguage(self):
        self.trans = QTranslator()
        if Win.LANGUAGE == 'zh':
            self.trans.load('zh_CN')
            _app = QApplication.instance()
            _app.installTranslator(self.trans)
            self.ui_calc.retranslateUi(self)
        elif Win.LANGUAGE == 'eng':
            self.trans.load('trans/win_calc.qm')
            _app = QApplication.instance()
            _app.installTranslator(self.trans)
            self.ui_calc.retranslateUi(self)

    def kill(self):
        ret = QMessageBox.warning(self, "警告", "是否终止计算？", QMessageBox.Yes | QMessageBox.No)
        if ret == QMessageBox.Yes:
            self.signal_kill.emit()

    def close_win(self):
        self.accept()

    def OS_error(self, error_type):
        if error_type == 1:
            QMessageBox.warning(self, '警告', '无法定义OpenSees材料，请检查材料参数或材料名是否正确！')
        elif error_type == 2:
            QMessageBox.warning(self, '警告', 'OpenSees分析不收敛！')

class Thread_ctrl(QThread):
    def __init__(self, u, para, Mat_name):
        super().__init__()
        self.u, self.para, self.Mat_name = u, para, Mat_name
        self.thread = ThreadRunOS(self.u, self.para, self.Mat_name)
        self.thread.is_running = True

    def thread_start(self):
        self.thread.start()


class Win_getData(QDialog):
    def __init__(self, plot_finished, u, F_pre):
        super().__init__()
        self.plot_finished, self.u, self.F_pre = plot_finished, u, F_pre
        self.ui_getData = Ui_WinGetData()
        self.ui_getData.setupUi(self)
        self.ui_getData.tableWidget.setEditTriggers(self.ui_getData.tableWidget.NoEditTriggers)  # 禁止编辑
        self.ui_getData.pushButton.clicked.connect(self.data_export)
        self.ui_getData.pushButton_2.clicked.connect(self.data_copy)
        self.ui_getData.tableWidget.setContextMenuPolicy(Qt.CustomContextMenu)
        self.ui_getData.tableWidget.customContextMenuRequested.connect(self.showContextMenu)
        self.init_write_data()
        self.init_setLanguage()

    def init_write_data(self):
        if self.plot_finished:
            self.ui_getData.tableWidget.setRowCount(len(self.u))
            for i in range(len(self.u)):
                item_x = QTableWidgetItem(str(round(self.u[i], 3)))
                item_y = QTableWidgetItem(str(round(self.F_pre[i], 3)))
                self.ui_getData.tableWidget.setItem(i, 0, item_x)
                self.ui_getData.tableWidget.setItem(i, 1, item_y)
            self.data = np.zeros((len(self.u), 2))
            self.data[:, 0], self.data[:, 1] = self.u, self.F_pre

    def init_setLanguage(self):
        self.trans = QTranslator()
        if Win.LANGUAGE == 'zh':
            self.trans.load('zh_CN')
            _app = QApplication.instance()
            _app.installTranslator(self.trans)
            self.ui_getData.retranslateUi(self)
        elif Win.LANGUAGE == 'eng':
            self.trans.load('trans/win_data.qm')
            _app = QApplication.instance()
            _app.installTranslator(self.trans)
            self.ui_getData.retranslateUi(self)

    def data_export(self):
        if not self.plot_finished:
            QMessageBox.warning(self, '警告', '无滞回曲线数据！')
            return 0
        else:
            fileName, _ = QFileDialog.getSaveFileName(self, "保存", "Data", "文本文档 (*.txt)")
            if fileName:
                np.savetxt(fileName, self.data)
                QMessageBox.information(self, '提示', f'数据已保存至{fileName}')

    def data_copy(self):
        if self.plot_finished:
            QApplication.clipboard().setText("\n".join(["\t".join(map(str, row)) for row in self.data]))
            QMessageBox.information(self, '提示', '已复制。')
        else:
            QMessageBox.warning(self, '警告', '无滞回曲线数据！')

    def copy_to_clipboard(self):
        selected = self.ui_getData.tableWidget.selectedItems()
        if selected:
            row_start = selected[0].row()
            row_end = selected[-1].row()
            col_start = selected[0].column()
            col_end = selected[-1].column()

            clipboard_text = ""
            for r in range(row_start, row_end + 1):
                row_data = []
                for c in range(col_start, col_end + 1):
                    item = self.ui_getData.tableWidget.item(r, c)
                    if item and item.text():
                        row_data.append(item.text())
                clipboard_text += "\t".join(row_data) + "\n"

            QApplication.clipboard().setText(clipboard_text)
            # QMessageBox.information(self, '提示', '已复制。')

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_C and event.modifiers() == Qt.ControlModifier:
            self.copy_to_clipboard()
        else:
            super().keyPressEvent(event)

    def showContextMenu(self, pos):
        # 定义上下文菜单
        context_menu = QMenu(self)
        copy_action = context_menu.addAction("复制")
        menu_size = context_menu.sizeHint()  # 获取菜单的大小
        global_pos = self.ui_getData.tableWidget.mapToGlobal(pos)  # 获取全局坐标
        adjusted_pos = global_pos + QPoint(menu_size.width() // 2, menu_size.height() // 2)  # 调整位置以使其出现在鼠标指针的右下方
        action = context_menu.exec_(adjusted_pos)
        if action == copy_action:
            self.copy_to_clipboard()

class Win_about(QDialog):
    def __init__(self):
        super().__init__()
        self.ui_win_about = Ui_WinAbout()
        self.ui_win_about.setupUi(self)
        self.init_ui()
        # self.init_setLanguage()

    def init_ui(self):
        text = self.ui_win_about.label_3.text()
        text = text.replace('data', DATE)
        text = text.replace('Version', VERSION)
        self.ui_win_about.label_3.setText(text)

class Win_help(QDialog):
    def __init__(self):
        super().__init__()
        self.ui_win_help = Ui_WinHelp()
        self.ui_win_help.setupUi(self)
        self.init_setLanguage()

    def init_setLanguage(self):
        self.trans = QTranslator()
        if Win.LANGUAGE == 'zh':
            self.trans.load('zh_CN')
            _app = QApplication.instance()
            _app.installTranslator(self.trans)
            self.ui_win_help.retranslateUi(self)
        elif Win.LANGUAGE == 'eng':
            self.trans.load('trans/win_help.qm')
            _app = QApplication.instance()
            _app.installTranslator(self.trans)
            self.ui_win_help.retranslateUi(self)


class MyCanvas(FigureCanvas):
    """重写FigureCanvas类的resizeEvent方法，实现自动设置tight_layout"""
    def __init__(self, fig, parent=None):
        super(MyCanvas, self).__init__(fig)
        self.fig = fig
        if parent:
            self.setParent(parent)
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

    def resizeEvent(self, event):
        super(MyCanvas, self).resizeEvent(event)
        self.fig.tight_layout()

