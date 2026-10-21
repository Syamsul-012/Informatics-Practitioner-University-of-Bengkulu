import time
import multiprocessing as mp
import numpy as np

# Fungsi simulasi kalkulasi matematis berat (misal: simulasi kualitas udara PM2.5)
def process_sensor_chunk(chunk_id, data_chunk):
    # Simulasi perhitungan kompleks pada array numerik
    result = np.sin(data_chunk) ** 2 + np.cos(data_chunk) ** 2
    avg_value = np.mean(result)
    return f"Chunk {chunk_id}: Avg = {avg_value:.4f}"

if __name__ == "__main__":
    print("=== SESI 2: HPC MULTIPROCESSING SIMULATION ===")
    
    # Generasi data sintetis berukuran besar
    large_dataset = np.random.rand(10_000_000)
    num_chunks = 4
    chunks = np.array_split(large_dataset, num_chunks)
    
    start_time = time.time()
    
    # Menjalankan pemrosesan paralel memanfaatkan multiple CPU cores
    with mp.Pool(processes=num_chunks) as pool:
        args = [(i, chunks[i]) for i in range(num_chunks)]
        results = pool.starmap(process_sensor_chunk, args)
        
    for res in results:
        print(res)
        
    print(f"Selesai dalam waktu: {time.time() - start_time:.4f} detik")