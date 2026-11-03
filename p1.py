import numpy as np

diem = np.array([8.0, 7.5, 9.0, 6.5, 8.5])

print("Danh sach diem:", diem)
print("Diem trung binh:", np.mean(diem))
print("Diem cao nhat:", np.max(diem))
print("Diem thap nhat:", np.min(diem))
print("Do lech chuan:", np.std(diem))