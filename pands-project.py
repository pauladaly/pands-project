# Load libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Download the iris data set from github repository
url = 'https://github.com/pauladaly/pands-project.git/iris.csv'

# load iris.csv into pandas dataframe
iris = pd.read_csv("iris.csv")

# Data Points and features
print (iris.shape)

# Column names in the dataset
print (iris.columns)

# How many Flowers for each Species?
iris["species"].value_counts()