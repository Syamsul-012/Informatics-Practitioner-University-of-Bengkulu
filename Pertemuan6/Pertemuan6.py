import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

print("=== SESI 6: SATELLITE IMAGERY DEFORESTATION DRIVER CLASSIFICATION ===")

# 1. Simulasi Data Ekstraksi Citra Satelit (Nilai Spektral NDVI, NBR, Tekstur)
np.random.seed(42)
n_pixels = 300

# Fitur Spektral Satelit
NDVI_diff = np.random.uniform(-0.8, 0.2, n_pixels) # Perubahan Indeks Vegetasi
NBR_diff = np.random.uniform(-0.9, 0.1, n_pixels)  # Perubahan Indeks Kebakaran
Texture_var = np.random.uniform(0.1, 0.9, n_pixels) # Variasi Tekstur Spasial

# Label Penyebab (0: Perkebunan Sawit, 1: Kebakaran Hutan, 2: Pertambangan)
drivers = np.random.choice([0, 1, 2], size=n_pixels)

df_sat = pd.DataFrame({
    'NDVI_diff': NDVI_diff,
    'NBR_diff': NBR_diff,
    'Texture_var': Texture_var,
    'Driver_Class': drivers
})

# 2. Model Training
X = df_sat[['NDVI_diff', 'NBR_diff', 'Texture_var']]
y = df_sat['Driver_Class']

model = RandomForestClassifier(n_estimators=50, random_state=42)
model.fit(X, y)

# 3. Evaluasi
predictions = model.predict(X)
print(f"Model Training Accuracy: {accuracy_score(y, predictions) * 100:.2f}%")