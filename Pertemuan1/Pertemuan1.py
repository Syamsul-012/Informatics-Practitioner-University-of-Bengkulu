import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix

# 1. Data Collection & Simulation
np.random.seed(42)
n_samples = 500

data = {
    'InvoiceID': [f'INV-{i:04d}' for i in range(1, n_samples + 1)],
    'Amount': np.random.uniform(100, 5000, n_samples),
    'DaysToDueDate': np.random.randint(7, 60, n_samples),
    'ClientTenureMonths': np.random.randint(1, 120, n_samples),
    'LatePaymentRisk': np.random.choice([0, 1], size=n_samples, p=[0.7, 0.3])
}

df = pd.DataFrame(data)

# 2. Data Cleaning & Preparation (Handling Garbage In, Garbage Out)
# Injeksi missing values secara acak untuk simulasi data berantakan
df.loc[10:20, 'Amount'] = np.nan
df['Amount'] = df['Amount'].fillna(df['Amount'].median())

# 3. Model Training (Predictive Analytics)
X = df[['Amount', 'DaysToDueDate', 'ClientTenureMonths']]
y = df['LatePaymentRisk']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X_train, y_train)

# 4. Evaluation & Diagnostic Report
y_pred = clf.predict(X_test)
print("=== SESI 1: CLASSIFICATION REPORT INVOICE RISK ===")
print(classification_report(y_test, y_pred))