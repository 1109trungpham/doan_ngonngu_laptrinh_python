#Câu 4:
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

#4.1 Viết hàm vẽ đồ thị mặt yên ngựa

def yen_ngua():
  x = np.linspace(start=-10, stop=10, num=5000)
  y = np.linspace(start=-10, stop=10, num=5000)
  x, y = np.meshgrid(x, y)
  z = (x/3) ** 2 - (y/2) ** 2
  fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
  yenngua = ax.plot_surface(x, y, z, cmap=cm.gist_heat_r, linewidth=0, antialiased=False)
  plt.show()

#4.2 Viết hàm vẽ đồ thị mặt hyperbolic 1 tầng

def hyperbols():
  m = np.linspace(start=-10, stop=10, num=2000)
  n = np.linspace(start=-10, stop=10, num=2000)
  m, n = np.meshgrid(m, n)
  p1 = 2 * ((m/3) ** 2 + (n/5) ** 2 - 1) ** (1/2)
  p2 = - 2 * ((m/3) ** 2 + (n/5) ** 2 - 1) ** (1/2)
  fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
  hyperbols1 = ax.plot_surface(m, n, p1, cmap=cm.gist_heat_r, linewidth=0, antialiased=False)
  hyperbols2 = ax.plot_surface(m, n, p2, cmap=cm.gist_heat_r, linewidth=0, antialiased=False)
  plt.show()

#4.3 Viết hàm vẽ đồ thị mặt cầu

def mat_cau():
    a = np.linspace(start=-5, stop=1, num=5000)
    b = np.linspace(start=-1, stop=5, num=5000)
    a, b = np.meshgrid(a, b)
    c1 = 4 + (4 - (a + 2) ** 2 - (b - 1) ** 2) ** (1/2)
    c2 = 4 - (4 - (a + 2) ** 2 - (b - 1) ** 2) ** (1 / 2)
    fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
    matcau1 = ax.plot_surface(a, b, c1, cmap=cm.gist_heat_r, linewidth=0, antialiased=False)
    matcau2 = ax.plot_surface(a, b, c2, cmap=cm.gist_heat_r, linewidth=0, antialiased=False)
    plt.show()

def main():
    yen_ngua()
    hyperbols()
    mat_cau()
if __name__=='__main__':
    main()