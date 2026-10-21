import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

print("=== SESI 4: K-MEANS CLUSTERING FOR CUSTOMER SEGMENTATION ===")

# 1. Data Synthesizing
np.random.seed(42)
X_raw = np.random.rand(200, 2) * [100, 1000] # Fitur: [Umur, Skor Belanja]

# 2. Preprocessing & Scaling
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X_raw)

# 3. Model Training (Unsupervised Learning)
kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
clusters = kmeans.fit_predict(X_scaled)

# 4. Result Structuring
df_results = pd.DataFrame(X_raw, columns=['Age', 'SpendingScore'])
df_results['Cluster'] = clusters

print(df_results.head())
print("\nJumlah Anggota per Cluster:")
print(df_results['Cluster'].value_counts())