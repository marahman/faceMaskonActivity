# Proposed title: The Effect of Daily Activities With Face Masks on Oxygen Saturation and Pulse Rate During COVID-19 Pandemic
# This code will plot the SpO2 level for Heavy activity with different face mask
# Code wrirrent on July 04, 2020
# Code wrirrent by ... and .... and


import numpy as np
import math
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

plt.close('all')

#data_loc = 'data/Data_Heavy.csv'
#gapminder = pd.read_csv(data_loc)
#print(gapminder.head(3))
#df1 = gapminder[['Subject','Age','Sex','Profession','RunningSpeed','Height','Weight','LS','SpO2_Resting','Pulse_Rest','SpO2_AE_NoM','Pulse_AE_NoM','SpO2_AE_1SM','Pulse_AE_1SM','SpO2_AE_2SM','Pulse_AE_2SM','SpO2_AE_Kn95M','Pulse_AE_Kn95M']]
#df1 = df1.fillna(0)
#print(df1.head())

data_loc = 'data/Data_Final.xlsx'
xdataf = pd.read_excel(data_loc,sheet_name='Data_Heavy')
print(xdataf.columns.ravel())
df1 = xdataf.fillna(0)
print(df1.head())


cdf = df1[['SpO2_Resting','SpO2_AE_NoM','SpO2_AE_1SM','SpO2_AE_2SM','SpO2_AE_Kn95M']].assign(Speed='Speed=40+')
mdf = pd.melt(cdf, id_vars=['Speed'], var_name=['Index'])
print(mdf.head())


#plt.figure(figsize=(8,6))

plt.xlabel('Different Masks')
plt.ylabel('SpO2')
plt.title('SpO2 level for Different Masks')
plt.ylim(80,100)
#ax = sns.boxplot(x="Location", y="value", hue='Letter', data=mdf)
ax = sns.boxplot(x="Speed", y="value", hue='Index', data=mdf)    

#plt.savefig('boxPlot_rikshaw_SpO2.svg')
plt.show()

#################
## T-value and p-value
################
import scipy

data_NM = df1[['SpO2_AE_NoM']]
data_1SM = df1[['SpO2_AE_1SM']]
data_2SM = df1[['SpO2_AE_2SM']]
data_Kn95M = df1[['SpO2_AE_Kn95M']]

twosample_results = scipy.stats.ttest_ind(data_NM, data_1SM)

res_NM_1SM = [
    ['Data-Pair', 'Test Statistic', 'p-value'],
    ['data_NM, data_1SM', twosample_results[0], twosample_results[1]]
]


twosample_results = scipy.stats.ttest_ind(data_NM, data_2SM)

res_NM_2SM = [
    ['Data-Pair', 'Test Statistic', 'p-value'],
    ['data_NM, data_2SM', twosample_results[0], twosample_results[1]]
]

twosample_results = scipy.stats.ttest_ind(data_NM, data_Kn95M)

res_NM_Kn95M = [
    ['Data-Pair', 'Test Statistic', 'p-value'],
    ['data_NM, data_Kn95M', twosample_results[0], twosample_results[1]]
]

print (res_NM_1SM)
print (res_NM_2SM)
print (res_NM_Kn95M)