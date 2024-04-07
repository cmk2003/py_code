with open("target.list",'r') as f:
    data=f.read().strip().split('\n')

# print(data)
with open('target_new.list','w')as f:
    for i in data:
        data_new=i.split('/')[-1]
        f.write(data_new+'\n')
        print(data_new)

with open("target_new.list",'r') as f:
    data=f.read().strip().split('\n')

print(data)

with open("msf.list",'r') as f:
    data1=f.read().strip().split('\n')

print(data1)

for i in data1:
    if i in data:
        print(i)