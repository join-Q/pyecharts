#coding=utf-8
from pyecharts import Bar,Line,Scatter,EffectScatter,Grid,Pie

attr=["衬衫","羊毛衫","雪纺衫","裤子","高跟鞋","袜子"]
v1=[5,20,36,10,75,90]
v2=[10,25,8,60,20,80]
bar=Bar("柱状图示例","副标题",height=720,width=1200,title_pos="65%")
bar.add("商家A",attr,v1,is_stack=True,is_more_utils=True)
bar.add("商家B",attr,v2,is_stack=True,is_more_utils=True,legend_pos="80%")
attr1=["周一","周二","周三","周四","周五","周六","周日"]
v1=[11,11,15,13,12,13,10]
v2=[1,-2,2,5,3,2,0]
line=Line("折线图示例","副标题",height=720,width=1200,title_pos="15%")
line.add("最高气温",attr1,v1,mark_point=["max","min"],mark_line=["average"],legend_pos="30%")
line.add("最高气温",attr1,v2,mark_point=["max","min"],mark_line=["average"])
scatter=Scatter("散点图示例","副标题",title_top="45%",title_pos="15%")
scatter.add("scatter",v1,v2,legend_top="45%",legend_pos="30%")
es=EffectScatter("动态散点图示例","副标题",title_top="45%",title_pos="65%")
es.add("es",v1,v2,effect_scale=10,legend_top="45%",legend_pos="85%")
pie=Pie('饼图示例',title_pos="45%")
pie.add("",attr1,v1,radius=[30,55],legend_pos="65%",legend_orient="vertical")
grid=Grid()
grid.add(bar,grid_bottom="60%",grid_left="60%")
grid.add(line,grid_bottom="60%",grid_right="60%")
grid.add(scatter,grid_top="60%",grid_left="60%")
grid.add(es,grid_top="60%",grid_right="60%")
grid.add(pie,grid_left="50%")
grid.render()


