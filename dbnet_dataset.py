import pandas as pd

# Data
data = {
    'point_cloud_feature': [0.123, 0.321],
    'video_feature1': [0.456, 0.654],
    'video_feature2': [0.789, 0.987],
    'vehicle_speed': [60.0, 45.0],
    'steering_angle': [0.5, -0.3]
}

# Membuat DataFrame dari data
df = pd.DataFrame(data)

# Menyimpan DataFrame ke dalam file CSV (ganti 'nama_file.csv' sesuai keinginan Anda)
df.to_csv('dbnet_dataset.csv', index=False)
# Menampilkan beberapa baris pertama dari DataFrame
print(df.head())
