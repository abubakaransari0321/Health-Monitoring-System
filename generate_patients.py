import pandas as pd
import numpy as np
from faker import Faker

# Initialize Faker
fake = Faker()

# Define number of patients
num_patients = 10000

# Generate patient IDs
patient_ids = np.arange(1, num_patients + 1)

# Generate random names
names = [fake.name() for _ in range(num_patients)]

# Generate random ages (18 to 90)
ages = np.random.randint(18, 90, num_patients)

# Randomly assign gender
genders = np.random.choice(['Male', 'Female'], num_patients)

# Generate Blood Pressure (Systolic & Diastolic) in mmHg
bp_systolic = np.random.randint(90, 180, num_patients)  # Normal: 90-120
bp_diastolic = np.random.randint(60, 120, num_patients)  # Normal: 60-80

# Generate Sugar Level (mg/dL)
sugar_levels = np.random.randint(70, 300, num_patients)  # Normal: 70-140

# Generate Cholesterol Level (mg/dL)
cholesterol_levels = np.random.randint(100, 300, num_patients)  # Normal: <200

# Generate Haemoglobin (g/dL) and round to 2 decimal places
haemoglobin_levels = np.round(np.random.uniform(8.0, 17.0, num_patients), 2)

# Create a DataFrame
df = pd.DataFrame({
    'Patient_ID': patient_ids,
    'Name': names,
    'Age': ages,
    'Gender': genders,
    'BP_Systolic': bp_systolic,
    'BP_Diastolic': bp_diastolic,
    'Sugar_Level': sugar_levels,
    'Cholesterol_Level': cholesterol_levels,
    'Haemoglobin': haemoglobin_levels
})

# Save to CSV
df.to_csv('patient_data.csv', index=False)

print("Patient data generated and saved as 'patient_data.csv'.")
