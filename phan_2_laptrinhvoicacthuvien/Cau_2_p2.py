#Câu 2:
from sympy import symbols, Eq, solve, pi
from sympy import *

#2.1 Viết hàm giải hệ phương trình
def giai_hept_3an():
    x, y, z = symbols('x y z')
    pt1 = Eq(2 * x - 5 * y + z + 5, 0)
    pt2 = Eq(4 * x + 2 * y - 2 * z - 2, 0)
    pt3 = Eq(x + y - z, 0)
    ketqua = solve((pt1, pt2, pt3), (x, y, z))
    print('nghiệm của hệ:', ketqua)

#2.2 Viết hàm tính giới hạn
def gioihan():
    x = symbols('x')
    a = (x ** 3 - 3 * x ** 2) ** (1 / 3) + (x ** 2 - 2 * x) ** (1 / 2)
    gioihan = limit(a, x, oo)
    print('giới hạn của hàm số:', gioihan)

#2.3 Viết hàm tính đạo hàm
def daoham():
    x = symbols('x')
    b = (2 * x - 1) / (x + 2)
    daoham = diff(b, x)
    print('đạo hàm của hàm số:', daoham)

#2.4 Viết hàm tính nguyên hàm
def nguyenham():
    x = symbols('x')
    c = x / (x ** 2 + 1)
    nguyenham = integrate(c, x)
    print('nguyên hàm của hàm số:', nguyenham)

#2.5 Viết hàm tính tích phân
def tichphan():
    x = symbols('x')
    d = (1 - x * tan(x)) / (x * x * cos(x) + x)
    tichphan = integrate(d, (x, (2/3) * pi, pi))
    print('tích phân của hàm số:', tichphan)

#2.6 Viết chương trình chính gọi thực hiện các hàm trên
def main():
    giai_hept_3an()
    gioihan()
    daoham()
    nguyenham()
    tichphan()

if __name__=='__main__':
    main()