from pyecharts import Bar,Pie,Grid
import random
attr=["{}天".format(i) for i in range(1,6)]
v1=[]
v2=[]
for i in range(1,6):
	v1.append(random.randint(100,200))
	v2.append(random.randint(10,150))
print(v1)
bar=Bar("降水量","单位为ms")
bar.add("降水量",attr,v1,mark_line=["average"],mark_point=["max","min"],is_more_utils=True)
bar.add("蒸发量",attr,v2,mark_line=["average"],mark_point=["max","min"])
pie=Pie("饼图-玫瑰饼图示例",title_pos='center',width=900)
#pie.add("商品A",attr,v1,is_random=True,radius=[30,75],rosetype='radius',legend_pos="70%",legend_orient="vertical")
pie.add("商品A",attr,v1,is_random=True,radius=[30,75],rosetype='area',is_legend_show=False,is_label_show=True)
pie.render()

