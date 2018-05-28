f=open("baidu_road_pos_transfer",'r')
all_pos_longitude = []
all_pos_latitude = []
all_pos_count = []
line=f.readline()
while line:
    string=line
    first_num=string.find("count")
    end_num=string.find(")")
    count=int(string[(first_num+7):end_num])
    if count>50:
    	all_pos_count.append(count)
    	first_num=string.find(":")
    	end_num=string.find(",")
    	longitude=string[(first_num+1):end_num]
    	all_pos_longitude.append(longitude)
    	first_num=string.find(":",first_num+1)
    	second_num=string.find(",",end_num+1)
    	latitude=string[(first_num+1):second_num]
    	all_pos_latitude.append(latitude)
    line=f.readline()
f.close()
g=open("baidu_road_point",'w')
g.write("(")
for i in range(0,len(all_pos_longitude)-1):
    g.write(str(all_pos_longitude[i]))
    g.write(',')
g.write(')\n');
g.write("(")
for i in range(0,len(all_pos_latitude)-1):
    g.write(str(all_pos_latitude[i]))
    g.write(",")
g.write(')\n');
g.close;