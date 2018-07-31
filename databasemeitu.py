import pandas as pd 

# Orders={"Order_fee":[2.0,3.0,4.0,5.0],"Coupon_fee":[1.0,2.0,3.0,4.0]}

# Orders['cover']=Orders['Order_fee'].apply(lambda x:str(x))+'_'+Orders['Coupon_fee'].apply(lambda x:str(x))
# Orders['cover']=Orders['cover'].apply(lambda x:x.split('_')[1] if x.split('_')[0]>x.split('_')[1] else x.split('_')[0])
# print(Orders['cover'])
x='123_456'
x.split('_')
print(x.split('_')[0])
df=pd.DataFrame({'key1':list('aabba'),'Key2':["one","two","three","four","five"],
	"data1":['1','2','3','4','5'],"data2":['2','4','6','8','10']})
df['key3']=df['Key2'].apply(lambda x:str(x)[1:2])
print(df)
df2=df[['key1','data1']]
print(df2)
grouped=df.groupby(['key1']).sum().reset_index()
print(grouped)
df["count"]=1
df=df.groupby('key1').sum().sort_values(by='count',ascending=False).head(10).reset_index()
print(df)

def1=pd.DataFrame({"A":["A{}".format(i) for i in range(4)],"B":["B{}".format(i) for i in range(4)],"C":["C{}".format(i) for i in range(4)],
	"D":["D{}".format(i) for i in range(4)]})
def2=pd.DataFrame({"A":["A{}".format(i) for i in range(4,8)],"B":["B{}".format(i) for i in range(4,8)],"C":["C{}".format(i) for i in range(4,8)],
	"D":["D{}".format(i) for i in range(4,8)]})
print(def2)
def3=[def1,def2]
result=pd.concat(def3)
print(result)
result=result.reset_index(drop=True)
print(result)
