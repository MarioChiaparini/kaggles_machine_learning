import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt

class Ploting:
    def __init__(self,data=None,ax=None,fig=None, x=None, y=None):
        self.data = data
        #self.ax = ax
        #self.fig = fig
        self.x = x
        self.y = y
    def ShowSub(self,data,x,y):
        fig, ax = plt.subplots(1,figsize=(12,12))
        vary = data[y]
        varx = data[x]
        return plt.show(varx,vary)
class Change:
    def __init__(self,data=None,value=None,dataframe=None,label=None):
        self.data = dataframe
        self.label = label
        self.value = value
    def CHangeValue(self,dataframe,label,value):
        self.dataframe = self.dataframe.loc[(self.dataframe[self.label]==self.value)]

data1 = pd.read_csv("../Desktop/scripts/ML_Day/data/WHOregionLifeExpectancyAtBirth.csv")
data2 = pd.read_csv("../Desktop/scripts/ML_Day/data/HALeWHOregionLifeExpectancyAtBirth.csv")

dataframe_1 = pd.DataFrame(data1)
dataframe_2 = pd.DataFrame(data2)

dataframe_1['Dim1'] = dataframe_1['Dim1'].replace(['Male'],1)
dataframe_1['Dim1'] = dataframe_1['Dim1'].replace(['Female'],0)
dataframe_1['Dim1'] = dataframe_1['Dim1'].replace(['Both sexes'],2)

americas1 = dataframe_1.loc[(dataframe_1['Location']) == 'Americas']
americas2 = dataframe_2.loc[(dataframe_2['Location']) == 'Americas']

americas1['Location'] = americas1['Location'].replace(['Americas'],3)
americas2['Location'] = americas2['Location'].replace(['Americas'],3)

africa1 = dataframe_1.loc[(dataframe_1['Location']) == 'Africa']
africa2 = dataframe_2.loc[(dataframe_2['Location']) == 'Africa']

africa1 = africa1.drop('Indicator',axis=1)
africa2 = africa2.drop('Indicator',axis=1)

africa1['Location'] = africa1['Location'].replace(['Africa'],4)
africa2['Location'] = africa2['Location'].replace(['Africa'],4)

dictdata1 = {'Africa Age':africa1['First Tooltip'].values,
                                       'Americas Age':americas1['First Tooltip'].values,
                                       'Gender Africa':africa1['Dim1'].values,
                                       'Gender Americas':americas1['Dim1'].values }
#dictdata2 = {'Africa Age':africa2['First Tooltip'].values,
#                                       'Americas Age':americas2['First Tooltip'].values,
#                                       'Gender Africa':africa2['Dim1'].values,
#                                       'Gender Americas':americas2['Dim1'].values }
dataframe_test = pd.DataFrame().from_dict(dictdata1



