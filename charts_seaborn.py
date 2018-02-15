import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd 
from pylab import savefig

sns.set(color_codes=True)

#histogram
x= np.random.normal(size=100)
sns.distplot(x,bins = 20, kde= False, rug=True,label = 'Histogram w/o Density') #bins mean number of bin
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Histogram of a random sample from a normal distribution')
plt.legend()

plt.show()

#Scatter plot with regression line and univariate grapha
mean, cov = [5,10],[(1,0.5),(0.5,1)]
data = np.random.multivariate_normal(mean, cov, 200)
data_frame = pd.DataFrame(data, columns=['x','y'])

sns.jointplot(x = 'x', y = 'y', data= data_frame, kind='reg').set_axis_labels("x",'y')
#jointplot function to display a scatter plot of two variables with regression line through the points and histograms for each of the variables
plt.suptitle('Join plot of two bariables with biavariate and univariate grapha')
plt.show()

#Pairwise bivariate scatter plots with univariate histograms
iris = sns.load_dataset('iris')
sns.pairplot(iris)
#pairplot function to display pairwise bivariate scatter plots and histograms for all of the variables in the dataset
plt.show()


#Box plots conditioning on several variables
tips = sns.load_dataset('tips')
sns.factorplot(x ='time', y= 'total_bill', hue='smoker',col='day',data=tips,kind='box',size=4,aspect=0.5)
#factorplot function to display box plots of the relationship between two variables for different values of a third variable. while conditioning on another variable
plt.show()


#linear regression model with bootstrap confidence interval
sns.lmplot(x = 'total_bill', y = 'tip', data=tips)
#lmplot function to display a scatter plot and linear regression model through the points, it also display a bootstrap confidence interval around the line
plt.legend()
plt.show()

#logistic regression model with bootstrap confidence interval
tips['big_tip'] = (tips.tip/tips.total_bill) >0.15
sns.lmplot(x= 'total_bill',y = 'big_tip',data=tips,logistic=True,y_jitter=0.03).set_axis_labels('Total Bill', 'Big Tip')

plt.title('Logistic Regression of big Tip vs Total Bill')
plt.show()
