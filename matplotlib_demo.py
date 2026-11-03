import matplotlib.pyplot as plt
import pandas as pd

# Lay du lieu tu file diem_sinh_vien.csv
df = pd.read_csv("diem_sinh_vien.csv")
diem_trung_binh_mon = df.groupby("mon_hoc")["diem"].mean()

# Bai tap 3.1: Bieu do cot diem trung binh theo mon hoc
plt.figure(figsize=(6, 4))
plt.bar(diem_trung_binh_mon.index, diem_trung_binh_mon.values, color="skyblue")
plt.title("Diem trung binh theo mon hoc")
plt.xlabel("Mon hoc")
plt.ylabel("Diem trung binh")
plt.ylim(0, 10)

# Them gia tri len dau moi cot
for idx, val in enumerate(diem_trung_binh_mon.values):
    plt.text(idx, val + 0.1, f"{val:.2f}", ha="center")

plt.tight_layout()
plt.savefig("bieu_do_cot.png")
plt.show()

# Bai tap 3.2: Bieu do duong xu huong diem qua cac lan kiem tra
lan_kiem_tra = [1, 2, 3]
diem_qua_cac_lan = [6.5, 7.5, 8.5]

plt.figure(figsize=(6, 4))
plt.plot(lan_kiem_tra, diem_qua_cac_lan, marker="o", color="green", label="Diem thuc te")
plt.title("Xu huong diem qua cac lan kiem tra")
plt.xlabel("Lan kiem tra")
plt.ylabel("Diem")
plt.ylim(0, 10)
plt.xticks(lan_kiem_tra, ["Lan 1", "Lan 2", "Lan 3"])

for x, y in zip(lan_kiem_tra, diem_qua_cac_lan):
    plt.text(x, y + 0.2, f"{y}", ha="center")

plt.legend()
plt.tight_layout()
plt.savefig("bieu_do_duong.png")
plt.show()