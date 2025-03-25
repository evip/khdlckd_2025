import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Đọc dữ liệu
dl = pd.read_csv('gdp.csv')

# Lọc dữ liệu cho Việt Nam (Country Code = "VNM")
dk_loc = dl["Country Code"] == "VNM"
dl_vn = dl[dk_loc]

# Lấy biến độc lập X (Year) và biến phụ thuộc Y (Value)
X = dl_vn["Year"]
Y = dl_vn["Value"]

# Áp dụng mô hình hồi quy đa thức với bậc 2
# Y = a * X^2 + b * X + c
degree = 2
coeffs = np.polyfit(X, Y, degree)
print("Hệ số mô hình hồi quy đa thức:")
print(coeffs)

a = coeffs[0]
b = coeffs[1]
c = coeffs[2]


# Hàm dự đoán: Y = coeffs[0] * X^2 + coeffs[1] * X + coeffs[2]
x_test = np.array([2024, 2025, 2026, 2027])

y_predict = a * x_test * x_test + b * x_test + c
#y_predict = np.polyval(coeffs, x_test)
print("Kết quả dự đoán:")
print(y_predict)




# Vẽ đồ thị dữ liệu lịch sử và dự đoán
plt.plot(X, Y, label='Dữ liệu lịch sử')
plt.plot(x_test, y_predict, color="red", marker='o', label='Dự đoán')
plt.xlabel("Năm")
plt.ylabel("GDP")
plt.title("Dự đoán GDP của Việt Nam bằng Hồi quy đa thức (Bậc 2)")
plt.legend()
plt.show()
