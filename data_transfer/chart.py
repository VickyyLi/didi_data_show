#coding:UTF-8
import time
import math



f = open("gps_20161101",'r')               # 返回一个文件对象   
#f = open("gps",'r')
line = f.readline()              # 调用文件的 readline()方法   
pre_driver = ""
pre_customer = ""
pre_x1 = 0.0
pre_y1 = 0.0
pre_time = 0.0
average_speed = [[0.0 for col in range(25)] for row in range(8)]
times = [[0.0 for col in range(25)] for row in range(8)]
numbers= [[0 for col in range(25)] for row in range(8)]
r=0
while line:
	r+=1
	if r % 10000==0:
		print(r)
		print(line)
	string = line
	first_dot = string.find(',')
	start_dot = string.find(',',(first_dot+1))
	mid_dot = string.find(',',(start_dot+1))
	end_dot = string.find(',',(mid_dot+1))
	#information
	driver = string[1:first_dot]
	customer = string[(first_dot+1):start_dot]
	timestamp = float(string[(start_dot+1):mid_dot])
	x1 = float(string[(mid_dot+1):end_dot])
	y1 = float(string[(end_dot+1):])

	time_local = time.localtime(timestamp)
	dt = time.strftime("%Y-%m-%d %H:%M:%S",time_local)
	dt_h = time.strftime("%H",time_local)
	dt_w = time.strftime("%w",time_local)
	dt_h = int(dt_h)#小时
	dt_w = int(dt_w)#星期

	if x1>=104.037 and x1<=104.127 and y1<=30.7005 and y1>=30.6355:
	#if x1>=0 and x1<=200 and y1<=200 and y1>=0:
		if pre_driver==driver and pre_customer==customer:
			distance = ((x1-pre_x1)**2+(y1-pre_y1)**2)**0.5*10
			time_interaction = timestamp-pre_time
			speed = distance/time_interaction
			if speed>0 and speed<0.0001:#5m/s
				numbers[dt_w][dt_h]+=1
			times[dt_w][dt_h]+=1
			average_speed[dt_w][dt_h]+=speed
			pre_x1 = x1
			pre_y1 = y1
			pre_driver = driver
			pre_customer = customer
			pre_time = timestamp
		else:
			pre_x1 = x1
			pre_y1 = y1
			pre_driver = driver
			pre_customer = customer
			pre_time = timestamp
	line = f.readline()  

f.close()

g = open("gps_calculate",'w')    
for i in range(0,8):
	for j in range(0,25):
		if times[i][j]!=0:
			result=average_speed[i][j]/(times[i][j])
			g.write("%d , %d :%f\n"%(i,j,result))
			g.write("time: %f\n"%(times[i][j]))
			g.write("number: %f\n"%(numbers[i][j]))
g.close()