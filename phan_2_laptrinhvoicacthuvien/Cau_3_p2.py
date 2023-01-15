#Câu 3: Xét hàm số y = x4 − 2x2 − 3, hãy viết chương trình vẽ đồ thị hàm số y, y′, y′′ và y′′′
# xét x ∈ [−10, 10]

import numpy as np
import matplotlib.pyplot as plt

def vedothi():
  x = np.linspace(start=-10, stop=10, num=30)
  y = x ** 4 - 2 * x ** 2 - 3
  y_phay = 4 * x ** 3 - 4 * x
  y_2phay = 12 * x ** 2 - 4
  y_3phay = 24 * x
  fig, ax = plt.subplots()
  ax.plot(x, y)
  ax.plot(x, y_phay)
  ax.plot(x, y_2phay)
  ax.plot(x, y_3phay)
  ax.set_xlabel("Trục hoành - x")
  ax.set_ylabel("Trục tung - y")
  ax.plot(x, y, marker='*', ms=10, label=r'$y=x^{4} -2x^{2} -3$')
  ax.plot(x, y_phay, marker='v', ms=5, label=r'$y=4x^{3} - 4x$')
  ax.plot(x, y_2phay, marker='o', ms=5, label=r'$y=12x^{2} -4$')
  ax.plot(x, y_3phay, marker='s', ms=5, label=r'$y=24x$')
  ax.set_title("Đồ thị phương trình f(x), f'(x), f''(x), f'''(x)")
  ax.legend()
  plt.show()
vedothi()