# Data plotting and visualization
import matplotlib.pyplot as plt
import seaborn as sns

# CSV management
import pandas as pd

# Math and arrays
import numpy as np

# Open the CSV
train = pd.read_csv("csv/train.csv")
# See what's up
print(train.columns)
print(train["belongs_to_collection"][0])
