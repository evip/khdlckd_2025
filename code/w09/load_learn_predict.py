import pandas as pd
from sklearn.datasets import load_diabetes
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

import pandas as pd

# Load CSV file
csv_path = "du_lieu_diabetes.csv"
df_loaded = pd.read_csv(csv_path)

# Gán X và y
X = df_loaded.drop(columns=["target"])
y = df_loaded["target"]

# Tạo lại df từ X và y
df = pd.concat([X, y.rename("target")], axis=1)

# Hiển thị vài dòng đầu để kiểm tra
df.head()


# Hiển thị vài dòng dữ liệu
print("Dữ liệu Diabetes (vài dòng đầu)")
print(df.head())

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=0
)

# Huấn luyện mô hình MLR
model = LinearRegression()
model.fit(X_train, y_train)

# In hệ số và R² trên tập kiểm thử
print("Intercept (β0):", round(model.intercept_, 3))
print("Coefficients:")
for feat, coef in zip(X.columns, model.coef_):
    print(f"  {feat}: {coef:.3f}")
print("R² score on test set:", round(model.score(X_test, y_test), 3))

# Đồ thị Predicted vs Actual
y_pred = model.predict(X_test)
plt.scatter(y_pred, y_test)
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()])
plt.xlabel("Giá trị dự đoán")
plt.ylabel("Giá trị thực tế")
plt.title("Predicted vs Actual (Test Set)")
plt.show()
