import os

import pandas as pd


data = {
    "Name": ["Aarav", "Ananya", "Rohan", "Priya", "Kabir", "Meera", "Arjun", "Isha", "Vikram", "Neha"],
    "Age": [25, 28, 22, 30, 27, 24, 32, 26, 29, 23],
    "City": ["Delhi", "Mumbai", "Pune", "Chennai", "Jaipur", "Kolkata", "Bengaluru", "Hyderabad", "Ahmedabad", "Lucknow"],
}

df = pd.DataFrame(data)

data_dir = "Data"
os.makedirs(data_dir, exist_ok=True)

file_path = os.path.join(data_dir, "sample_data.csv")
df.to_csv(file_path, index=False)

print(f"CSV file saved: {file_path}")
