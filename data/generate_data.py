
import pandas as pd
import numpy as np

def generate_sample_data(seed=42):
    np.random.seed(seed)
    n = 500
    control = pd.DataFrame({
        "group": "control",
        "converted": np.random.binomial(1, 0.30, n)
    })
    treatment = pd.DataFrame({
        "group": "treatment",
        "converted": np.random.binomial(1, 0.38, n)
    })
    df = pd.concat([control, treatment], ignore_index=True)
    df.to_csv("data/campaign_data.csv", index=False)

if __name__ == "__main__":
    generate_sample_data()
