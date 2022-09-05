import numpy as np
import pandas as pd
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

df=pd.read_csv('D:/git/Quantum internship/Quantum-internship-Data-Science/data/internship_train.csv')
test=pd.read_csv('D:/git/Quantum internship/Quantum-internship-Data-Science/data/internship_hidden_test.csv')
class modeling:
    def __init__(self,train_df, test_df):
        self.train_df=train_df
        self.test_df=test_df
        
    def preprocessing(self,df):
        data=df['6'].to_numpy().copy()
        x_ = PolynomialFeatures(degree=2, include_bias=False).fit_transform(data.reshape(-1, 1))
        return x_
        
    def training(self):
        x=self.preprocessing(self.train_df)
        y=self.train_df['target']
        x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.33, random_state=42)
        model=LinearRegression().fit(x_train,y_train)
        
        print(f'RMAE on train :{mean_squared_error(y_test,model.predict(x_test),squared=True)}')
        return model
    
    def summorize(self):
        x=self.preprocessing(self.test_df)
        result=self.training().predict(x)
        pd.DataFrame(index=self.test_df.index,columns=['result'],data=result).to_csv('out.csv')
        return result
        
m=modeling(df,test)
m.summorize()
    
    