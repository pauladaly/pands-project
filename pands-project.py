import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import seaborn as sns
sns.set(color_codes=True)

%matplotlib inline
%pylab inline
Populating the interactive namespace from numpy and matplotlib
df = pd.read_csv('https://github.com/pauladaly/pands-project.git/input/Iris.csv')
df.head()