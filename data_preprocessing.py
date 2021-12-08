# Import Libaries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read input dataset
data =  pd.read_csv('data\Iris.csv', )
print('Data shape before cleaning', data.shape)


# there is outliers in Sepal Width
Q1 = data.SepalWidthCm.quantile(0.25)
Q3 = data.SepalWidthCm.quantile(0.75)
IQR = Q3 - Q1

# droping outliers
data = data[~((data['SepalWidthCm'] < (Q1 - 1.5 *IQR)) | (data['SepalWidthCm'] > (Q3 + 1.5 *IQR)))]
print('drop outliers')

# no missing values

# droping duplicates
data.drop_duplicates(inplace=True)
print('drop duplicates')


# save cleaned dataset
data.to_csv('data\Iris.csv', index=False)

print('Data shape after cleaning', data.shape)
print('Saving data')