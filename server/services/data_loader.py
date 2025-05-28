import pandas as pd
from kagglehub import KaggleDatasetAdapter, load_dataset

def load_data():
  df = load_dataset(
    KaggleDatasetAdapter.PANDAS,
    "mdabbert/ultimate-ufc-dataset",
    "ufc-master.csv"
  )
  return df
