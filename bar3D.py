from pyecharts import Bar3D
import random
#(np.random.randint(2,10,size=[4,3]))
attr=[]
a=[i for i in range(0,7)]
b=[i for i in range(0,24)]
c=random.randint(2,8)
for i in a:
	for j in b:
		attr.append(i)
		attr.append(j)
		attr.append(random.randint(0,16))
		
data=[]
for i in range(0,len(attr),3):
	data.append(attr[i:i+3])
print(data)

x_axis1=["{}a".format(i) for i in range(1,13)]
x_axis2=["{}p".format(i) for i in range(1,13)]
bar3d=Bar3D("3D 柱状图示例",width=1200,height=600)
x_axis=x_axis1+x_axis2;
print(x_axis)
y_axis=["Saturday","Friday","Thursday","Wednesday","Tuesday","Monday","Sunday"]
range_color=['#313695', '#4575b4', '#74add1', '#abd9e9', '#e0f3f8', '#ffffbf','#fee090', '#fdae61', '#f46d43', '#d73027', '#a50026']
bar3d.add("",x_axis,y_axis,[[d[1],d[0],d[2]] for d in data],is_visualmap=True,visual_range=[0,50],
	grid3d_width=200,grid3d_depth=80,grid3d_shading='lambert')
bar3d.render()