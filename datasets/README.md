# Datasets

This project uses the **CICIDS2017 dataset**, a modern intrusion detection dataset created by the Canadian Institute for Cybersecurity.

Dataset source:
https://www.unb.ca/cic/datasets/ids-2017.html

The dataset contains realistic network traffic including:

- Normal traffic
- DDoS attacks
- Port scanning
- Brute force attacks
- Web attacks

Due to its large size (~11GB), the dataset is **not stored in this repository**.

To use the dataset:

1. Download the CSV files from the official website.
2. Place them inside the following directory:

datasets/cicids2017/

Example structure:

datasets/
    cicids2017/
        Monday-WorkingHours.csv
        Tuesday-WorkingHours.csv
        Wednesday-WorkingHours.csv