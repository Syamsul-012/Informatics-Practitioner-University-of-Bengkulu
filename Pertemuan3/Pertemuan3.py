import geopandas as gpd
from shapely.geometry import Point, Polygon

print("=== SESI 3: GIS SPATIAL AUTOMATION ===")

# 1. Membuat data spasial titik aset (Misal: Sensor / Fasilitas Publik)
data_points = {
    'AssetID': ['A1', 'A2', 'A3'],
    'geometry': [Point(102.2655, -3.7928), Point(102.2700, -3.7950), Point(102.2800, -3.8000)]
}

gdf_assets = gpd.GeoDataFrame(data_points, crs="EPSG:4326")

# 2. Re-proyeksi ke sistem koordinat terproyeksi (UTM) untuk analisis jarak meter
gdf_assets_projected = gdf_assets.to_crs(epsg=32748) # UTM Zone 48S (Area Indonesia/Bengkulu)

# 3. Analisis Buffering (Zone buffer 500 meter di sekitar aset)
gdf_assets_projected['buffer_500m'] = gdf_assets_projected.geometry.buffer(500)

print(gdf_assets_projected[['AssetID', 'geometry', 'buffer_500m']])