from pyecharts import Bar,Line,Overlap,EffectScatter
import random
attr=["{}".format(i) for i in range(1,7)]
attr1=["{}天".format(i) for i in range(30)]
v1=[]
v2=[] 
for i in range(1,7):
	v1.append(random.randint(50,120))
	v2.append(random.randint(70,140))

v3=[random.randint(20,50) for _ in range(30)]
print(v3)

bar=Bar("Bar-line示例")
bar.add("bar",attr,v1,mark_point=['max','min'],mark_line=['average'],is_more_utils=True)
line=Line()
line.add("line",attr,v2,mark_point=['max','min'],is_label_show=True)

overlap=Overlap()
overlap.add(bar)
overlap.add(line)

bar1=Bar("bar-datazoom-slider示例")
bar1.add("温度",attr1,v3,legend_top="5%",is_label_show=True,is_more_utils=True,is_datazoom_show=True,datazoom_type="both",xaxis_rotate=30,yaxis_rotate=30,
	yaxis_max=60)

es=EffectScatter("动态散点图示例")
es.add("EffectScatter-v1",attr,v1)
es.add("EffectScatter-v2",attr,v2,mark_point=['max','min'],is_more_utils=True)
#overlap.render()
es.render()
