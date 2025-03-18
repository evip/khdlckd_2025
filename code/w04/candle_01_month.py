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

df_monthly = df.resample('M').agg({
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

# 5) Vẽ biểu đồ nến theo khung tháng
mpf.plot(
    df_monthly,
    type='candle',
    style=custom_style,
    title='Biểu đồ nến - Khung Tháng',
    volume=True,             # Hiển thị cột Volume
    mav=(3,6),               # Đường trung bình 3,6 (theo tháng)
    ylabel='Giá (Monthly)',
    ylabel_lower='Khối lượng'
)
