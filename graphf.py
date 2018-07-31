import datetime
import random 
from pyecharts import HeatMap
begin=datetime.date(2017,1,1)
end=datetime.date(2017,12,31)
data=[[str(begin+datetime.timedelta(days=i)),random.randint(2000,25000)] for i in range((end-begin).days+1)]
print(data)
x_axis=["{}a".format(i) for i in range(24)]
y_axis=["Saturday","Friday","Thursday","Wednesday","Tuesday","Monday","Sunday"]
#data=[[i,j,random.randint(0,50)] for i in range(24) for j in range(7)]
heatmap=HeatMap("日历热力图示例","某人2017年微信步数情况")
#heatmap.add("",x_axis,y_axis,data,is_visualmap=True,visual_text_color="#eee",visual_orient="horizontal")
# heatmap.add("",data,is_calendar_heatmap=True,is_visualmap=True,visual_text_color="#eee",visual_range=[2000,25000],visual_orient="horizontal",
# 		visual_pos="center",visual_top="80%")
heatmap.add("", data, is_calendar_heatmap=True,
            visual_text_color='#000', visual_range_text=['', ''],
            visual_range=[1000, 25000], calendar_cell_size=['auto', 30],
            is_visualmap=True, calendar_date_range="2017",
            visual_orient="horizontal", visual_pos="center",
            visual_top="80%", is_piecewise=True)
heatmap.render()