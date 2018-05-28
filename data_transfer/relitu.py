import math

def gcj02_to_bd09(lng, lat):
    z = math.sqrt(lng * lng + lat * lat) + 0.00002 * math.sin(lat * math.pi)
    theta = math.atan2(lat, lng) + 0.000003 * math.cos(lng * math.pi)
    bd_lng = z * math.cos(theta) + 0.0065
    bd_lat = z * math.sin(theta) + 0.006
    return [bd_lng, bd_lat]


all_pos_longitude = []
all_pos_latitude = []
all_pos_count = []
f = open("order_20161101",'r')               # 返回一个文件对象   
line = f.readline()              # 调用文件的 readline()方法   
r=0
while line:
    r+=1
    string = line                   # 后面跟 ',' 将忽略换行符   
    print(r)
    print(line)
    first_num = string.find(',')
    second_num = string.find(',',first_num+1)
    start_num = string.find(',',second_num+1)
    mid_num = string.find(',',start_num+1)
    end_num = string.find(',',mid_num+1)
    road_pos1 = string[(start_num+1):mid_num]
    road_pos2 = string[(mid_num+1):end_num]
    input_a = float(road_pos1)
    input_b = float(road_pos2)
    [on_pos1_trans,on_pos2_trans]=gcj02_to_bd09(input_a,input_b)
    on_pos1_trans=round(on_pos1_trans,5)
    on_pos2_trans=round(on_pos2_trans,5)
    flag=0;
    for i in range(0,len(all_pos_longitude)):
        if all_pos_longitude[i]==on_pos1_trans and all_pos_latitude[i]==on_pos2_trans:
            all_pos_count[i]+=1;
            flag=1;
            break;
    if flag==0:
        all_pos_longitude.append(on_pos1_trans);
        all_pos_latitude.append(on_pos2_trans);
        all_pos_count.append(1);
    line = f.readline()
f.close()    

g = open("baidu_road_pos_transfer",'w')
for i in range(0,len(all_pos_longitude)-1):
    g.write('{\"lng\":');
    g.write(str(all_pos_longitude[i]));
    g.write(',\"lat\":');
    g.write(str(all_pos_latitude[i]));
    g.write(',\"count\":');
    g.write(str(all_pos_count[i]));
    g.write(')},\n');
g.write('{\"lng\":');
g.write(str(all_pos_longitude[len(all_pos_longitude)-1]));
g.write(',\"lat\":');
g.write(str(all_pos_latitude[len(all_pos_longitude)-1]));
g.write(',\"count\":');
g.write(str(all_pos_count[len(all_pos_longitude)-1]));
g.write(')};\n');
g.close;