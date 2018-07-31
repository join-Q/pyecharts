from pyecharts import Kline
import random

v1=[[random.randint(2000,2300),random.randint(2100,2300),random.randint(2100,2200),random.randint(2200,2250)] for i in range(31)]
print(v1)
kline=Kline("K-线图示例","日历曲线图")
kline.add("日K",["2017/7/{}".format(i+1) for i in range(31)],v1,mark_point=["max","min"],is_datazoom_show=True)
kline.render()