#Câu 1:
import numpy as np
import random

#1.1 Cho x ∈ Rn và A ∈ Rm×n, hãy viết hàm tính tích x. A

#vector ngẫu nhiên với ? phần tử số nguyên
def sinh_vector(kichco):
  x = np.random.randint(low=-10, high=10, size= kichco)
  return x

#matrix ngẫu nhiên với ? hàng ? cột, số nguyên
def sinh_matrix(kichco1,kichco2):
  y = np.random.randint(low=-10, high=10, size= (kichco1, kichco2))
  return y

#nhân matrix(vector) với vector(matrix)
def nhan_matrix_vector(vectrix1, vectrix2):
  a = vectrix1.dot(vectrix2)
  return a

#1.2 Cho A, B ∈ Rm×n, hãy viết hàm tính A°B và AT. B

#Phép nhân Hadamard 2 matrix
def nhan_hadamard(matrix1,matrix2):
  a = np.multiply(matrix1, matrix2)
  return a

#Phép chuyển vị matrix
def chuyenvi_matrix(matrix):
  print('ma trận trước khi chuyển vị', matrix)
  matrixt = matrix.T
  print('ma trận sau khi chuyển vị: ', matrixt)
  return matrixt

#1.3 Viết chương trình chính gọi các hàm trên
#Chương trình chính
def main():
  vt_x = sinh_vector(3)
  mt_a = sinh_matrix(3, 3)
  mt_b = sinh_matrix(3, 3)
  print('vector x', vt_x)
  print('ma trận a', mt_a)
  print('ma trận b' ,mt_b)
  print('tích vector x và ma trận a')
  kq_1 = nhan_matrix_vector(mt_a, vt_x)
  print(kq_1)
  print('tích hadamard 2 ma trận a, b')
  kq_2 = nhan_hadamard(mt_a, mt_b)
  print(kq_2)
  print('nhân ma trận b với ma trận chuyển vị của ma trận a')
  mt_a_tfm = chuyenvi_matrix(mt_a)
  print('tích ma trận b với ma trận a(T)')
  kq_3 = nhan_matrix_vector(mt_b, mt_a_tfm)
  print(kq_3)

if __name__=='__main__':
  main()