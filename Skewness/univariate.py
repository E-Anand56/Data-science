import pandas as pd

class univariate():
    @staticmethod
    def quanqual(data):
        qual=[]
        quan=[]
        for column in data.columns:
            #print(column)
            if data[column].dtype == "object":        
                #print("qual")
                qual.append(column)
            else:
                quan.append(column)
                #print("qual")
        return quan,qual

    @staticmethod
    def preprocess(data,quan):
        descriptive=pd.DataFrame(index= ['mean','median','mode','Q1:25','Q2:50','Q3:75','Q4:100',
                                             'IQR','1.5rule','Greater','max','Lesser','min','skew','kurtosis'],columns=quan)
        for column in quan:
            descriptive[column]['mean']=data[column].mean()
            descriptive[column]['median']=data[column].median()
            descriptive[column]['mode']=data[column].mode()[0]
            descriptive[column]['Q1:25']=data.describe()[column]['25%']
            descriptive[column]['Q2:50']=data.describe()[column]['50%']
            descriptive[column]['Q3:75']=data.describe()[column]['75%']
            descriptive[column]['Q4:100']=data.describe()[column]['max']
            descriptive[column]['IQR']=data.describe()[column]['75%']-data.describe()[column]['25%'] #IQR=Q3−Q1
            descriptive[column]['1.5 Rule']=1.5*descriptive[column]['IQR'] #1.5*IQR
            descriptive[column]['Greater']=data.describe()[column]['25%']+1.5*descriptive[column]['IQR'] #Q1+1.5×IQR
            descriptive[column]['max']=data[column].max()
            descriptive[column]['Lesser']=data.describe()[column]['25%']-1.5*descriptive[column]['IQR'] #Q1−1.5×IQR
            descriptive[column]['min']=data[column].min()
            descriptive[column]['skew']=data[column].skew()
            descriptive[column]['kurtosis']=data[column].kurtosis()
        return descriptive