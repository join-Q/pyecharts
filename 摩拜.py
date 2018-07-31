Orders["cover_fee"]=Orders["Coupon_fee"].apply(lambda x:str(x))+"_"+Orders["Order_fee"].apply(lambda x:str(x))
Orders["cover"]=Orders["cover_fee"].apply(lambda x:str(x).split("_")[0] if str(x).split("_")[0]>str(x).split("_")[1] else str(x).split("_")[1])
citylist=City_conf['Citycode'].apply(lambda x:str(x))
Orders['city']=Orders["Citycode"].apply(lambda x:str(x) if x in citylist else "others")
covers=Orders[["city","cover"]]
covers['cover']=covers["cover"].astype("float")


covers_sum=covers.groupby("city").sum().reset_index()