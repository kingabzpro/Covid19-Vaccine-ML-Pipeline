import orchest
import pandas as pd


# Convert the data into a DataFrame.
INPUT_DIR = "Data"
bcell = pd.read_csv(f"{INPUT_DIR}/input_bcell.csv")
covid = pd.read_csv(f"{INPUT_DIR}/input_covid.csv")
sars = pd.read_csv(f"{INPUT_DIR}/input_sars.csv")
bcell_sars = pd.concat([bcell, sars], axis=0, ignore_index=True)

# Output the Vaccine data
print("Outputting converted Vaccine data...")
orchest.output((bcell, covid, sars, bcell_sars), name="data")
print(bcell_sars.shape)
print("Success!")
