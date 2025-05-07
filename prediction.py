import pandas as pd
import numpy as np
import joblib

# Load model
loaded_model = joblib.load('best_model.pkl')
loaded_scaler = joblib.load('scaler.pkl')

df_dummy = pd.DataFrame({
    "TotalWorkingYears": [13],
    "Age": [32],
    "OverTime": [1], 
    "MaritalStatus": [1],
    "JobLevel": [3],
})

# Scaling dummy input
df_dummy_scaled = df_dummy.copy()
df_dummy_scaled[["TotalWorkingYears","Age"]] = loaded_scaler.transform(df_dummy[["TotalWorkingYears","Age"]])
df_dummy_scaled = df_dummy_scaled[['TotalWorkingYears', 'Age', 'JobLevel', 'OverTime', 'MaritalStatus']]

# Mapping hasil prediksi

mapping = {0: "Karyawan kemungkinan akan Tetap diperusahaan", 1: "Karyawan kemungkinan akan Pergi"}

# Prediksi menggunakan model
prediction = loaded_model.predict(df_dummy_scaled)
probabilities = loaded_model.predict_proba(df_dummy_scaled)

# Probabilitas untuk Tetap diperusahaan (Attrition: 0) dan Pergi dari perusahaan (Attrition: 1)
proba_stay = probabilities[:, 0] * 100 
proba_leave = probabilities[:, 1] * 100 

# Tampilkan hasil
print(f"Prediksi Attrition: {mapping[prediction[0]]}")
print(f"Probabilitas Tetap diperusahaan: {proba_stay[0]:.2f}%")
print(f"Probabilitas Pergi dari perusahaan: {proba_leave[0]:.2f}%")