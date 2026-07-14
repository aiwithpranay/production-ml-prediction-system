import pandas as pd
import os

class DataIngestion:

    def initiate(self):

        os.makedirs("artifacts/data", exist_ok=True)

        df = pd.read_csv("data/raw/data.csv")

        df.to_csv("artifacts/data/data.csv", index=False)

        print("Data Ingestion Completed")