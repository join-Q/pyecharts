from pyecharts import Graph
import random

nodes=[{"name":"结点1","symbolSize":10},
	{"name":"结点2","symbolSize":10},
	{"name":"结点3","symbolSize":10},
	{"name":"结点4","symbolSize":10},
	{"name":"结点5","symbolSize":10},{"name":"结点6","symbolSize":20},
	{"name":"结点7","symbolSize":20},
	{"name":"结点8","symbolSize":10},
]

links=[]
for i in nodes:
	for j in nodes:
		links.append({"source":i.get("name"),"target":j.get("name")})
graph=Graph("关系图-力引导布局示例")#width=1200,height=600)
graph.add("",nodes,links,is_label_show=True,repulsion=8000,graph_layout="circular",label_pos="right")
graph.render()

data=[[i,j,random.randint(0,50)] for i in range(24) for j in range(7)]
print(data)