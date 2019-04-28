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

# View a table display of the data for first 30 entries
print(iris.head(30))

# View a sample of 20 records within the data

print(iris.sample(20))


# Show statistic summary of Iris data set

iris.describe()

# Statistics for each Species
## Details for setosa
setosa=iris[iris['species']=='setosa']
print(setosa.describe())

## Details for versicolor
versicolor =iris[iris['species']=='versicolor']
print(versicolor.describe())

## Details for virginica
virginica =iris[iris['species']=='virginica']
print(virginica.describe())

# 2-D Scatter Plot
iris.plot(kind='scatter', x='sepal_length', y='sepal_width');plt.show()

# 2-D Scatter Plot with colour-coding for each flower type/class
# Using sns from seaborn

sns.set_style("whitegrid");
sns.FacetGrid(iris, hue="species", height=4) \
    .map(plt.scatter, "sepal_length", "sepal_width") \
    .add_legend();
plt.show();    

# Pair-Plot
## Scatterplots for joint relationships and histograms for univariate distributions
sns.pairplot(iris)
plt.show()

## Show different levels of a categorical variable by the color of plot elements:
sns.pairplot(iris, hue="species")
plt.show()