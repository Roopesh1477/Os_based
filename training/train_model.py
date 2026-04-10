import pandas as pd
from sklearn.ensemble import IsolationForest 
import pickle

df = pd.read_csv("datasets/cicids_sample.csv")

model = IsolationForest(contamination=0.2)
model.fit(df)

with open("models/anomaly_model.pkl","wb") as f:
    pickle.dump(model,f)

print("Training started...")
print("model trained and saved in model/animaly_model.pkl")