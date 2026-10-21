import pandas as pd
import plotly.express as px

print("=== SESI 5: INTERACTIVE DATA VISUALIZATION ===")

# Data Tren Transaksi/Interaksi Pengguna
data = {
    'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
    'User_Type_A': [120, 150, 170, 210, 250, 300],
    'User_Type_B': [80, 90, 100, 130, 140, 160]
}

df = pd.DataFrame(data)

# Pembuatan visualisasi interaktif dengan kontras warna yang jelas
fig = px.line(
    df, 
    x='Month', 
    y=['User_Type_A', 'User_Type_B'],
    title='Statistik Interaksi Pengguna Berdasarkan Tipe',
    labels={'value': 'Jumlah Interaksi', 'variable': 'Kategori User'},
    markers=True
)

# Menyesuaikan tema antarmuka agar ramah secara visual (Preattentive Visual Attributes)
fig.update_layout(template="plotly_white")

# Untuk menyimpan keluaran visualisasi sebagai berkas HTML interaktif
fig.write_html("interactive_dashboard.html")
print("Visualisasi berhasil diekspor ke 'interactive_dashboard.html'")