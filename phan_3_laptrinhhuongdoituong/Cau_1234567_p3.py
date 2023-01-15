import os
import pickle
#1 Xây dựng lớp NhanVien có các thuộc tính là hoten, tuoi, luong
class NhanVien:
  def __init__(self, name, age, salary):
      self.hoten = name
      self.tuoi = age
      self.luong = salary
  def __str__(self):
      info = 'tên: ' + self.hoten + ', ' + 'tuổi: ' + str(self.tuoi) + ', ' + 'lương: ' + str(self.luong)
      return info
  def __gt__(self, obj):
      return (self.tuoi > obj.tuoi)
  def __ge__(self, obj):
      return (self.tuoi >= obj.tuoi)
  def __lt__(self, obj):
      return (self.tuoi < obj.tuoi)
  def __le__(self, obj):
      return (self.tuoi <= obj.tuoi)
  def __eq__(self, obj):
      return (self.tuoi == obj.tuoi)
#2 Viết hàm nhập dữ liệu cho 1 list các đối tượng thuộc lớp NhanVien
def nhap_nhanvien():
    name = str(input('nhập tên: '))
    age = int(input('nhập tuổi: '))
    salary = int(input('nhập lương: '))
    nhanvien = NhanVien(name, age, salary)
    return nhanvien
#3 Viết hàm hiển thị list các đối tượng thuộc lớp NhanVien ra màn hình
def hienthi_nhanvien(NhanVien):
    for item in NhanVien:
        print(item)
#4 Viết hàm hiển thị list các đối tượng thuộc lớp NhanVien theo chiều giảm dần của độ tuổi
def sapxep_nhanvien_theotuoi(list):
    print('Sắp xếp giảm dần tuổi của nhân viên')
    sapxep = sorted(list, reverse=True)
    for item in sapxep:
        print(item)
#5 Viết hàm lưu list các đối tượng thuộc lớp NhanVien vào tập tin nhị phân
def luu_nhanvien(thumuc: str, ten_taptin: str, objs: list[NhanVien]):
    try:
        with open(os.path.join(thumuc, ten_taptin), 'wb') as f:
            pickle.dump(objs, f)
        print('Hoàn thành quá trình lưu dữ liệu vào tập tin')
    except Exception as e:
        print(e)
        print('Xảy ra lỗi trong quá trình lưu file')
#6 Viết hàm đọc list các đối tượng thuộc lớp NhanVien vào tập tin nhị phân
def doc_nhanvien(thumuc: str, ten_taptin: str) -> list[NhanVien]:
    try:
        with open(os.path.join(thumuc, ten_taptin), 'rb') as f:
            nv = pickle.load(f)
        return nv
    except Exception as e:
        return None
#7 Viết chương trình chính gọi thực hiện các hàm trên
def main():
    path = '/Users/trung/data'
    filename = 'nhanvien'
    nv1 = nhap_nhanvien()
    nv2 = nhap_nhanvien()
    nv3 = nhap_nhanvien()
    nv = [nv1, nv2, nv3]
    luu_nhanvien(path, filename, nv)
    noidung = doc_nhanvien(path, filename)
    hienthi_nhanvien(noidung)
    sapxep_nhanvien_theotuoi(nv)
    print('Kết thúc chương trình')
if __name__ == '__main__':
    main()