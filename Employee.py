import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#Task1(read and understand data)
data=pd.read_csv('Employee Dataset.csv')

#print(data.head())
#print(data.shape)
#print(data.columns)
#print(data.info())

#[From task1 i observed that 1.there are 50 rows and 6 columns
# 2.It has a columns like 'id', 'groups', 'age', 'healthy_eating', 'active_lifestyle', 'salary'
# 3.There are no null values 
# 4.all columns are of int type whereas group column is of object type]

#Task 2(visualize the distribution and relationship between columns)

#Scatter plot between age and salary
#plt.figure(figsize=(11,6))

#sns.scatterplot(data=data,x='age',y='salary',color='blue',alpha=0.5)
#plt.title('Scatter plot bw age and salary',fontsize=15)
#plt.xlabel('Employee age',fontsize=15)
#plt.ylabel('Employee salary',fontsize=15)
#plt.show()
#[I observed that as age increses salary increses. But there are some exceptions with age 62 has less salary]



#Scatter plot between age and healthy_eating
#plt.figure(figsize=(11,6))

#sns.scatterplot(data=data,x='age',y='healthy_eating',color='red',alpha=0.5)
#plt.title('Scatter plot bw age and healthy_eating',fontsize=15)
#plt.xlabel('Employee age',fontsize=15)
#plt.ylabel('Employee healthy_eating',fontsize=15)
#plt.show()
#[I observed that as age increses healthy_eating  increses]


#Scatter plot between salary and active_lifestyle
#plt.figure(figsize=(11,6))

#sns.scatterplot(data=data,x='salary',y='active_lifestyle',color='green',alpha=0.5)
#plt.title('Scatter plot bw salary and active_lifestyle',fontsize=15)
#plt.xlabel('Employee salary',fontsize=15)
#plt.ylabel('Employee active_lifestyle',fontsize=15)
#plt.show()
#[I observed that as salary increses active_lifestyle  decreses]


#Scatter plot between healthy_eating and active_lifestyle
#plt.figure(figsize=(11,6))

#sns.scatterplot(data=data,x='healthy_eating',y='active_lifestyle',color='green',alpha=0.5)
#plt.title('Scatter plot bw healthy_eating and active_lifestyle',fontsize=15)
#plt.xlabel('Employee healthy_eating',fontsize=15)
#plt.ylabel('Employee active_lifestyle',fontsize=15)
#plt.show()
#[I observed that as healthy_eating increses active_lifestyle  increses]


#converting categorical data to numerical data
#data['groups']=pd.Categorical(data['groups'])
#data['groups']=data['groups'].cat.codes


#corr_matrix=data.corr()
#print(corr_matrix)

#Heatmap for correlation matrix
#plt.figure(figsize=(11,6))
#sns.heatmap(corr_matrix,annot=True)
#plt.title('Heatmap of corrilation matrix')
#plt.show()



#histogram for salary distribution
#plt.figure(figsize=(11,6))

#sns.histplot(data=data,x='salary',color='orange',alpha=0.5,bins=10)
#plt.title('hist plot for salary',fontsize=15)
#plt.xlabel('Employee salary',fontsize=15)
#plt.ylabel('count',fontsize=15)
#plt.show()
#[i observed that very less employees have high salary]


#count groups
#plt.figure(figsize=(10,6))
#sns.countplot(data=data,x='groups')
#plt.title('Count of groups')
#plt.xlabel('groups')
#plt.ylabel('count')
#plt.show()
#[i observed that many employees are of A and O group ]



#Employees with healthy_eating >8 and salary<1000
#print(data[(data['healthy_eating']>=8) & (data['salary']<1000)])
#[The employee with id 26 has healthy_eating of 9 and salary is 700 which is to be checked]


