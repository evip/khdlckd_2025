import pandas as pd
import mplfinance as mpf

# 1) Đọc dữ liệu từ file CSV
#    parse_dates=['Date'] để chuyển cột Date sang kiểu datetime
#    index_col='Date' để dùng Date làm chỉ số index
df = pd.read_csv('Gia_uniswap.csv', parse_dates=['Date'], index_col='Date')

# Kiểm tra xem dữ liệu đã đọc vào thế nào:
print(df.head())  # In 5 dòng đầu

# 2) Tạo "marketcolors" tuỳ chỉnh
custom_market_colors = mpf.make_marketcolors(
    up='blue',      # Màu nến tăng
    down='red',     # Màu nến giảm
    edge='black',   # Viền nến màu đen
    wick='black',   # Bóng nến màu đen
    volume='in'     # Màu cột volume sẽ tự động xanh/đỏ theo nến
)

# 3) Tạo style tuỳ chỉnh
custom_style = mpf.make_mpf_style(
    base_mpf_style='classic',  # Có thể đổi sang 'charles', 'yahoo', ...
    marketcolors=custom_market_colors,
    facecolor='white',         # Nền trắng
    gridcolor='gray',          # Màu lưới
    gridstyle='--',            # Kiểu gạch ngang
    y_on_right=False           # Trục giá nằm bên trái
)

# 4) Vẽ biểu đồ nến
mpf.plot(
    df,
    type='candle',         # Kiểu nến
    style=custom_style,    # Áp dụng style tuỳ chỉnh
    volume=True,           # Vẽ khối lượng (nếu có cột 'Volume')
    mav=(5, 10),           # Vẽ thêm 2 đường trung bình động (5 và 10 phiên)
    title='Biểu đồ nến Uniswap', 
    ylabel='Giá', 
    ylabel_lower='Khối lượng'
)
