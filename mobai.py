import pandas as pd 

Metro=pd.DataFrame({"name":["中官村地铁站","望京地铁站"],"Lng":[121.442132,121.0284938],"Lat":[24.22421,24.09839]})
print(Metro)
Orders=pd.DataFrame({"ID":[1,2],"Lng":[121.442132,121.0284938],"Lat":[24.22421,24.09839],"Time":["2017-07-02 22:12:14",
	"2017-07-01 22:11:15"]})
print(Orders)

Metro["lng"]=Metro["Lng"].apply(lambda x:str(x)[0:6])
Metro["lat"]=Metro["Lat"].apply(lambda x:str(x)[0:6])
print(Metro)
Orders["lng"]=Orders["Lng"].apply(lambda x:str(x)[0:6])
Orders["lat"]=Orders["Lat"].apply(lambda x:str(x)[0:6])
tables=pd.merge(Metro[["name","lng","lat"]],Orders[["ID","lat","lng","Time"]],on=["lat","lng"])
#tables1=pd.merge(Metro,Orders,on=["lat","lng","Lat","Lng"])
print(tables)
tables["date"]=tables["Time"].apply(lambda x:str(x).split(" ")[0][5:])
tables["time"]=tables["Time"].apply(lambda x:str(x).split(" ")[1][:5])
print(tables)

tables=tables[tables["date"]=="07-01"]
tables=tables[tables["time"]>="07:00"]
print(tables)
table_top10=tables[["ID","name","date","time"]].copy()

table_top10["count"]=1
table_top10=table_top10.groupby('ID').count().reset_index().sort_values(by="ID").head(10)
print(table_top10)

