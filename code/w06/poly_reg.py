import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

# 1. Đọc và lọc dữ liệu cho Mỹ
df = pd.read_csv('gdp.csv')
usa_data = df[df['Country Code'] == 'VNM']
usa_data = usa_data.sort_values(by='Year')

# Xây dựng biến độc lập X (Year) và biến phụ thuộc y (GDP)
X = usa_data[['Year']]
y = usa_data['Value']

# 2. Tạo đặc trưng đa thức với degree=2
poly = PolynomialFeatures(degree=2)
X_poly = poly.fit_transform(X)

# 3. Huấn luyện mô hình hồi quy đa thức
poly_model = LinearRegression()
poly_model.fit(X_poly, y)

# Dự báo cho dữ liệu lịch sử (để vẽ đường cong)
y_poly_pred = poly_model.predict(X_poly)

# 4. Dự báo cho các năm 2024, 2025, 2026, 2027
future_years = pd.DataFrame({'Year': [2024, 2025, 2026, 2027]})
future_years_poly = poly.transform(future_years)
predictions_poly = poly_model.predict(future_years_poly)

# Hiển thị kết quả dự báo
forecast_poly = future_years.copy()
forecast_poly['Predicted GDP'] = predictions_poly
print("Dự báo GDP của Mỹ (Hồi quy đa thức, degree=2):")
print(forecast_poly)

# 5. Vẽ đồ thị: dữ liệu lịch sử, đường hồi quy đa thức và dự báo tương lai
plt.figure(figsize=(8, 5))
#plt.scatter(X, y, color='blue', label='Dữ liệu lịch sử')
plt.plot(X, y, color='blue', label='Dữ liệu lịch sử')
plt.plot(X, y_poly_pred, color='red', label='Đường hồi quy đa thức')

#plt.scatter(future_years, predictions_poly, color='green', label='Dự báo tương lai')
plt.scatter(future_years, predictions_poly, color='green', label='Dự báo tương lai')
plt.xlabel('Năm')
plt.ylabel('GDP')
plt.title('Dự báo GDP của Mỹ với Hồi quy đa thức (degree=2)')
plt.legend()
plt.show()
