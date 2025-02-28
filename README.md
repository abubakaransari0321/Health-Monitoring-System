# Health Monitoring System

## Overview
This project is a **Health Monitoring System** for a diagnostic center that processes health data for **10,000 patients**. It utilizes **Apache Spark** for distributed data processing and **Hadoop MapReduce** for statistical aggregation.

## Features
- **Generated 10,000 Patient Profiles** with randomized health data.
- **Processed Health Data** using Apache Spark to compute **average BP, Sugar, Cholesterol, and Haemoglobin levels**.
- **Implemented MapReduce** to verify results by computing the same averages separately.
- **Dashboard-ready CSV outputs** for further visualization.

## Technologies Used
- **Apache Spark** (Data Processing)
- **Hadoop MapReduce** (Data Aggregation)
- **Python (Pandas, NumPy)** (Data Handling & CSV Generation)

## Data Pipeline
1. **Data Generation:**  
   - 10,000 patients were assigned random **Blood Pressure, Sugar Levels, Cholesterol, and Haemoglobin** values.
   - Names were randomly generated.

2. **Spark Processing:**  
   - The data was processed using **Apache Spark**.
   - Computed **age-wise average Sugar, Cholesterol, and Haemoglobin levels**.
   - Results stored in `health_summary_final.csv`.

3. **MapReduce Execution:**  
   - A separate **MapReduce job** was executed to compute the same statistics.
   - The reducer aggregated **average values per age group**.
   - Output stored in `mapreduce_health_output.csv`.

## Files in Repository
| File Name | Description |
|-----------|-------------|
| `patient_data.csv` | Raw patient data (10,000 records) |
| `health_summary_final.csv` | Spark-processed health statistics |
| `mapreduce_health_output.csv` | MapReduce-generated health statistics |
| `dashboard.ipynb` | Jupyter Notebook for visualization |

## How to Run
1. **Run Spark Processing** (If executing manually):
   ```bash
   spark-submit process_health_data.py
   ```
2. **Run MapReduce (Simulated for Demo):**
   ```bash
   hadoop jar mapreduce_health.jar input output
   ```
3. **Visualize Data:**
   - Open `dashboard.ipynb` and run the cells to generate graphs.

## Conclusion
This project demonstrates the power of **distributed computing** in health analytics, using **Spark & MapReduce** to process large-scale medical data efficiently.
