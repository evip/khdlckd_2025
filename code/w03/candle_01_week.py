import pandas as pd
import mplfinance as mpf

# 1) Đọc dữ liệu từ file CSV
df = pd.read_csv('Gia_uniswap.csv', parse_dates=['Date'], index_col='Date')

# Kiểm tra xem dữ liệu daily
print(df.head())

# 2) Tạo hàm resample (OHLCV) theo khung tuần, khung tháng
#    Mỗi group (tuần hoặc tháng) ta lấy:
#    - Open = giá Open của ngày đầu group
#    - High = giá High cao nhất group
#    - Low = giá Low thấp nhất group
#    - Close = giá Close của ngày cuối group
#    - Volume = tổng khối lượng group
df_weekly = df.resample('W').agg({
    'Open':  'first',
    'High':  'max',
    'Low':   'min',
    'Close': 'last',
    'Volume':'sum'
}).dropna()

# 3) Tạo "marketcolors" và style tuỳ chỉnh (nến xanh-đỏ, viền đen, bóng đen)
custom_market_colors = mpf.make_marketcolors(
    up='blue',   # Nến tăng
    down='red',  # Nến giảm
    edge='black',
    wick='black',
    volume='in'
)

custom_style = mpf.make_mpf_style(
    base_mpf_style='classic',
    marketcolors=custom_market_colors,
    facecolor='white',
    gridcolor='gray',
    gridstyle='--'
)

# 4) Vẽ biểu đồ nến theo khung tuần
mpf.plot(
    df_weekly,
    type='candle',
    style=custom_style,
    title='Biểu đồ nến - Khung Tuần',
    volume=True,             # Hiển thị cột Volume
    mav=(5,10),              # Đường trung bình 5,10 (theo tuần)
    ylabel='Giá (Weekly)',
    ylabel_lower='Khối lượng'
)
