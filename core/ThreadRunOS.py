import numpy as np
import openseespy.opensees as ops
from PyQt5.QtCore import QThread, pyqtSignal


class ThreadRunOS(QThread):
    signal_finish = pyqtSignal(list)
    signal_OS_error = pyqtSignal(int)  # 1: 材料参数错误，2: 不收敛

    def __init__(self, u: np.ndarray, para: list, Mat_name: str):
        """运行OpenSees运行子线程

        Args:
            u (np.ndarray): 位移序列
            para (list): 材料参数
            Mat_name (str): 材料名
        """
        super().__init__()
        self.is_running = True
        self.u, self.para, self.Mat_name = np.insert(u, len(u), 0), para, Mat_name
        
    def run(self):
        N = len(self.u)  # 迭代次数
        ops.wipe()
        ops.model('basic', '-ndm', 3, '-ndf', 3)
        ops.node(1, 0, 0, 0)
        ops.node(2, 1, 0, 0)
        try:
            ops.uniaxialMaterial(*([self.Mat_name, 1] + self.para))
        except:
            print('材料错误：')
            print([self.Mat_name, 1] + self.para)
            self.signal_OS_error.emit(1)
            self.is_running = False
        if self.is_running:
            ops.element('Truss', 1, 1, 2, 1, 1)
            ops.fix(1, 1, 1, 1)
            ops.fix(2, 0, 1, 1)
            ops.timeSeries('Path', 1, '-dt', 1, '-values', *self.u)
            ops.pattern('Plain', 1, 1)  # patternTag, tsTag, fact
            ops.sp(2, 1, 1)  # nodeTag, dof, dofValue
            ops.constraints('Lagrange')
            ops.numberer('RCM')
            ops.system('BandGeneral')
            ops.test('EnergyIncr', 0.0001, 80)
            ops.algorithm('Newton')
            ops.integrator('LoadControl', 1)
            ops.analysis('Static')

        F_pre = np.zeros((N - 1))
        for i in range(N - 1):
            if self.is_running:
                F_pre[i] = -ops.eleForce(1, 1)
                ok = ops.analyze(1)
                if ok != 0:
                    self.signal_OS_error.emit(2)
                    self.is_running = False
            else:
                self.signal_finish.emit([])
                break
        else:
            self.signal_finish.emit(F_pre.tolist())

    def stop(self):
        """停止运算"""
        self.is_running = False

