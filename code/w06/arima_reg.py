import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA

dl = pd.read_csv('gdp.csv')
dk_loc = dl["Country Code"]=="VNM"
data = dl[dk_loc]

# Đọc dữ liệu từ file CSV
#data = pd.read_csv('gdp_us.csv')

# Chuyển đổi cột Year thành kiểu datetime và đặt làm index
data['Year'] = pd.to_datetime(data['Year'], format='%Y')
data.set_index('Year', inplace=True)

# Chuẩn bị dữ liệu chuỗi thời gian
time_series = data['Value']

# Xây dựng mô hình ARIMA
# Tham số (p, d, q) có thể được điều chỉnh dựa trên ACF và PACF
# Ví dụ: p=2, d=1, q=2 (có thể thử các giá trị khác)
model = ARIMA(time_series, order=(2, 1, 2))
model_fit = model.fit()

# Dự đoán GDP cho 5 năm tới
forecast_steps = 5
forecast = model_fit.forecast(steps=forecast_steps)

print(forecast)

# Hiển thị kết quả dự đoán
forecast_years = pd.date_range(start='2024', periods=forecast_steps, freq='Y')
for year, gdp in zip(forecast_years, forecast):
    print(f"Dự đoán GDP năm {year.year}: {gdp:.2f}")


# Vẽ biểu đồ dữ liệu thực tế và dự đoán
plt.figure(figsize=(12, 6))
plt.plot(time_series, label='Dữ liệu thực tế')
plt.plot(forecast_years, forecast, label='Dự đoán', color='red', marker='o')
plt.xlabel('Năm')
plt.ylabel('GDP (USD)')
plt.title('Dự đoán GDP của Viet Nam sử dụng')
plt.legend()
plt.show()
