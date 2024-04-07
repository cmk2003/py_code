step=input()
input_array=[]
for i in range(int(step)):
    input_=""
    for j in range(8):
        tmp=input()
        input_+=tmp
    # print(input_)
    input_array.append(input_)
    time=0
    for i in input_array:
        if i==input_:
            time+=1
    print(time)
