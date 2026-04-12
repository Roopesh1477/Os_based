## Dataset Usage

This project uses a cleaned subset of the CICIDS2017 dataset for training.

- Source: CICIDS2017 (MachineLearningCSV)
- File used: Monday-WorkingHours
- Rows: 10,000
- Selected features:
  - Flow Duration
  - Total Fwd Packets
  - Total Backward Packets
  - Flow Bytes/s
  - Flow Packets/s
- Data cleaning:
  - Removed missing values
  - Removed infinite values

The dataset is located in `datasets/cicids_sample.csv`.