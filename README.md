# 1 Introduction
This Git Hub repository contains all the files created during my completion of the Programming and Scripting Project 2019 as part of the H.Dip in Data Analytics.  This README contains a summary and my investigations into Fisher’s Iris data set.

# 2 Project Objective
The objective of this project is to research Fisher’s Iris data set and write documentation and code in the Python programing language based on the research carried out.  The outline for this project is:
1. Research background information about the data set and write a summary about it.
2. Keep a list of references you used in completing the project.
3. Download the data set and write some Python code to investigate it.
4. Summarise the data set in Python by, calculating the maximum, minimum and mean of each column of the data set. 
5. Write a summary of your investigations.
6. Include supporting tables and graphics.

# 3 About the Iris Data Set
The Iris flower data set or Fisher’s Iris data set is a multivariate data set introduced by the British statistician and biologist Ronald Fisher in his 1936 paper “The use of multiple measurements in taxonomic problems as an example of linear discriminant analysis”. This is a very famous and widely used dataset by everyone trying to learn machine learning and statistics. The data set consists of 50 samples from each of three species of the Iris flower 
•	Iris Versicolor 
•	Iris Virginica 
•	Iris Setosa

Four features were measured from each flower sample 
1.	Length of the petal in cm
2.	Width of the petal in cm
3.	Length of the sepal in cm
4.	Width of the sepal in cm
 
![](Images/Iris.jpg)

The fifth column in the data set is the species of the flower observed.
Analysis of the Iris Data Set

# 4.0 Analysis of the Iris Data Set
## 4.1 Importing Libraries
To complete the analysis for this project I imported the following modules, functions and objects:

![](Images/Libraries.PNG)

#4.2 Instructions for loading the data set
For this project I saved the Iris Data Set to my GitHub Repository and read the file from there.

![](Images/DataSet.PNG)

#4.3 Summary of the Data Set
To review the data within the data set I looked at the data in different ways:
1. Dimensions of the dataset
2. Viewed the data 
3. Statistical summary of all the attributes
4. Breakdown of the data by the class variable

4.3.1 Dimensions of the dataset
Ran the following python code to view the dimensions of the data set.

![](Images/Shape.PNG) 

This showed that there are 150 instances and 5 attributes within the data set.

![](Images/ShapeResult.PNG) 

4.3.2 The Data
To get an idea of what the data set looked like I wanted to view the column names, the types of species within the dataset and I wanted to take a look at the data set in a table view for the first 30 data set entries, to do this the code I used was.

Column Names within the data set:

![](Images/ColumnNamesCode.PNG) 

![](ColumnNamesOutput.PNG) 

Types of Species and their count within the data set:

![](SpeciesCode.PNG) 

![](SpeciesOuput.PNG) 

Table view of the first 30 entries on the data set:

![](First30code.PNG) 

![](First30code.PNG) 

4.3.3 Statistical Summary
Ran the following python code 

![](Images/Stats.PNG) 

The Python Code outputted the following:

![](Images/StatisticSummary.PNG) 

4.3.4 Breakdown of the data by the class variable


 ![](Images/StatisticSummary.PNG) 
![Scatter Results](Images/Scatter.png)
![Scatter Results in Colour](Images/ColourScatter.png)
![Pair-Plot Results](Images/PairPlot.PNG)

## Summarize the data set

# Conclusion

# References
1.	Wikipedia: Iris flower data set (https://en.wikipedia.org/wiki/Iris_flower_data_set)
2.	Your First Machine Learning Project in Python Step-By-Step (https://machinelearningmastery.com/machine-learning-in-python-step-by-step/)
3.	+20 ML Algorithms +15 Plot for Beginners (https://www.kaggle.com/mjbahmani/20-ml-algorithms-15-plot-for-beginners)
4. Youtube Channel: Applied AI Course (https://www.youtube.com/channel/UCJINtWke3-FMz2WuEltWDVQ)


