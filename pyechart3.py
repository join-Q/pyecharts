import pandas as pd
import numpy as np 
from pyecharts  import Bar
title="bar chart"
index=pd.date_range("3/8/2017",periods=6,freq="M")
print(index)
df1=pd.DataFrame(np.random.randn(6),index=index)
df3=pd.DataFrame(np.random.randn(6))
print(np.random.randn(6))
print(df1.index)
df2=pd.DataFrame(np.random.randn(6),index=index)
print(df1.values)

dtvalue1=[i[0] for i in df1.values]
print(dtvalue1)
dtvalue2=[i[0] for i in df2.values]
_index=[i for i in df1.index.format()]

bar=Bar(title,"profit and lossess suation")
bar.add("profit",_index,dtvalue1)
bar.add("lossess",_index,dtvalue2)
bar.render()