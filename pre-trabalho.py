import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

url='/kaggle/input/alzheimers-disease-patient-data/alzheimers_disease_patient_data.csv'
alzheimer = pd.read_csv(url)
alzheimer