import numpy as np
import matplotlib.pyplot as plt


def generate_AMP(amp: list, du: float) -> np.ndarray:
    """生成加载制度

    Args:
        amp (list): 加载制度的峰值位移值
        du (float): 位移增量

    Returns:
        np.ndarray: 加载制度位移序列
    """
    du = float(du)
    u = np.array([])
    for i in range(len(amp) - 1):
        N = int(abs((amp[i + 1] - amp[i]) / du))
        u = np.append(u, np.linspace(amp[i], amp[i + 1], N)[: -1])
    u = np.append(u, amp[-1])
    return u

if __name__ == "__main__":
    amp = [0, 5, 0, -5, 0]
    u = generate_AMP(amp, du=0.1)
    plt.plot(u, '-o')
    plt.show()