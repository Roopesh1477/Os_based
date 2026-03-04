import pandas as pd
from sklearn.ensemble import IsolationForest 
import pickle

data = {
    "duration": [10,20,30,500,15,18,600],
    "src_bytes":[200,300,250,10000,210,280,12000],
    "dst_bytes":[150,200,180,9000,160,190,11000]
}

df = pd.DataFrame(data)

model = IsolationForest(contamination=0.2)
model.fit(df)

with open("../models/anomaly_model.pkl","wb") as f:
    pickle.dump(model,f)

print("model trained and saved in model/animaly_model.pkl")