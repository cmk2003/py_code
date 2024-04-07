# n,m=map(int,input().split())
n,m=map(int,input().split())
n,m=int(n),int(m)
temp_x=0;
temp_y=0;
for i in range(0,n):
    dx,dy=input().split();
    dx,dy=int(dx),int(dy)
    temp_x=temp_x+dx
    temp_y=temp_y+dy;

for i in range(0,m):
    x,y=input().split()
    x,y=int(x),int(y)
    x=x+temp_x
    y=y+temp_y
    print(x,y)