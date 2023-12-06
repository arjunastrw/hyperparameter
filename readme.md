# Vehicle Dynamics Prediction using Random Forest

## Overview

Proyek ini menggunakan Regresi Random Forest untuk memprediksi kecepatan kendaraan dan sudut kemudi berdasarkan fitur yang disediakan. Dataset, 'dbnet_dataset.csv,' seharusnya mencakup kolom-kolom untuk fitur (misalnya 'video_feature1', 'video_feature2') dan variabel target (kecepatan, sudut kemudi).

## Getting Started

1. **Clone the Repository:**
   ```sh
   git clone https://github.com/arjunastrw/hyperparameter.git
   cd hyperparameter
   ```

## Yang DI Butuhkan

1. **Install Dependencies**

   ```sh
   pip install -r requirements.txt

   ```

2. **Persiapkan Dataset**

- Gantilah 'dbnet_dataset.csv' dengan file dataset sesungguhnya.
- Pastikan dataset mencakup kolom yang diperlukan.

3. **Jalankan Kode**

   ```sh
   python randomforest.py

   ```

4. **Project Structure**

- `randomforest.py`: Skrip utama untuk pelatihan model, prediksi, dan evaluasi.
- `dbnet_dataset.csv` : Contoh dataset
- `requirements.txt` : Daftar pustaka Python yang diperlukan

5. **Result**
   Skrip ini mencetak metrik evaluasi untuk prediksi kecepatan dan sudut kemudi,
   termasuk Mean Squared Error (MSE) dan Mean Absolute Error (MAE).
