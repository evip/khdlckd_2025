import pandas as pd
from sklearn.datasets import load_diabetes

# Load diabetes dataset
bunch = load_diabetes(as_frame=True)
df = pd.concat([bunch.data, bunch.target.rename("target")], axis=1)

# Export to CSV
csv_path = "du_lieu_diabetes.csv"
df.to_csv(csv_path, index=False)

print(f"Dataset đã được lưu vào {csv_path}")