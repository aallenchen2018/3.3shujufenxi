import pandas as pd
import numpy as np

s=pd.Series([1,3,5,np.nan,6,8],index=['a','b','c','d','e','f'])
s.index
s.values
s[2:5]
s.index.name='索引'
######Pandas的Dataframe类型
date=pd.date_range('20180101',periods=6)
df=pd.DataFrame(np.random.randn(6,4))
df1=pd.DataFrame(np.random.randint(6,4))


print(df1)