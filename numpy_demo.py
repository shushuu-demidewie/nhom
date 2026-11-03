import numpy as np

diem_list = [8.5, 7.0, 9.2, 6.5, 5.5]
diem_array = np.array(diem_list)
print("Kieu du lieu:", type(diem_list), type(diem_array))

# Phep toan vector hoa: cong truc tiep 0.5 vao toan bo mang
diem_cong_them = diem_array + 0.5
print("Mang cong them 0.5 (NumPy):", diem_cong_them)

# Cach lam bang list comprehension tren list thuan
diem_cong_them_list = [diem + 0.5 for diem in diem_list]
print("List cong them 0.5 (List comprehension):", diem_cong_them_list)

# Thong ke co ban
print("Trung binh:", np.mean(diem_array))
print("Lon nhat:", np.max(diem_array))
print("Nho nhat:", np.min(diem_array))
print("Do lech chuan:", round(np.std(diem_array), 2))

# Mang 2 chieu (ma tran)
ma_tran = np.array([[1, 2, 3], [4, 5, 6]])
print("Ma tran:\n", ma_tran)
print("Kich thuoc (shape):", ma_tran.shape)
print("Ma tran nhan 2:\n", ma_tran * 2)