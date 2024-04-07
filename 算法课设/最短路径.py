import pygame
import math

WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK=(0,0,0)

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
pygame.init()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("路径选择")

# 设置背景颜色为白色
background_color = (255, 255, 255)
screen.fill(background_color)
pygame.display.update()

# 创建按钮,设置button位置
button_width = 100
button_height = 50
button_x=0
button_y=0
button_rect = pygame.Rect(button_x, button_y, button_width, button_height)
button_rect_1 = pygame.Rect(button_x+button_width+20, button_y, button_width, button_height)
button_rect_2 = pygame.Rect(button_rect_1.x+button_width+20, button_y, button_width, button_height)
button_rect_3 = pygame.Rect(button_rect_2.x+button_width+20, button_y, button_width, button_height)
button_rect_4 = pygame.Rect(button_rect_3.x+button_width+20, button_y, button_width, button_height)

#

# 记录四个点的列表
points = []
points_start_end=[]
points_all =[]
length =[];#四列三行的二维数组
road=[]
road_points = []

#构造所有点的数组
def addPoints():
    points_all.append(points_start_end[0])
    with open('new_point.txt', 'r') as f_in:
        for line in f_in:
            lst = line.split(',')  # 用逗号分隔字符串并生成一个列表
            points = [[int(lst[i]), int(lst[i + 1])] for i in range(0, len(lst), 2)]
            points = [(tuple(item) if isinstance(item, list) else item) for item in points]
            for i in points:
                points_all.append(i)

    points_all.append(points_start_end[1])


#判断点是否在多边形内部 在的话为真
def is_in_dbx(p, quadrilateral):
    n=0
    if is_on_edge(p,quadrilateral):
        return False
    if p in quadrilateral:
        return False
    for i in range(0,len(quadrilateral)):
        j=(i+1)%len(quadrilateral)
        p1=quadrilateral[i]
        p2=quadrilateral[j]

        if (p1[1] > p[1]) != (p2[1] > p[1]):
            t = (p[1] - p1[1]) / (p2[1] - p1[1])
            x = p1[0] + t * (p2[0] - p1[0])
            if x - p[0] > 0 and t > 0 and t < 1:
                n += 1
            if x - p[0] == 0:
                return False
    return n % 2 == 1;
#判断点是否在边上
def is_on_edge(p, quadrilateral):
    # 判断点是否在四边形的外接矩形内，如果不在则肯定不在其边上

    min_x = min(quadrilateral[0][0], quadrilateral[1][0], quadrilateral[2][0], quadrilateral[3][0])
    max_x = max(quadrilateral[0][0], quadrilateral[1][0], quadrilateral[2][0], quadrilateral[3][0])
    min_y = min(quadrilateral[0][1], quadrilateral[1][1], quadrilateral[2][1], quadrilateral[3][1])
    max_y = max(quadrilateral[0][1], quadrilateral[1][1], quadrilateral[2][1], quadrilateral[3][1])
    if p[0] < min_x or p[0] > max_x or p[1] < min_y or p[1] > max_y:
        return False

    # 遍历四边形的每一条边，计算该边所在直线与点之间的距离
    epsilon = 1e-10
    for i in range(4):
        j = (i + 1) % 4
        # 计算点到直线的距离
        x1, y1 = quadrilateral[i]
        x2, y2 = quadrilateral[j]
        distance = abs((y2 - y1) * p[0] - (x2 - x1) * p[1] + x2 * y1 - y2 * x1) / ((y2 - y1) ** 2 + (x2 - x1) ** 2) ** 0.5
        # 如果距离小于等于 epsilon，则认为点在当前边上
        if distance <= epsilon:
            # 判断点是否恰好落在顶点上
            if abs(p[0] - x1) <= epsilon and abs(p[1] - y1) <= epsilon or \
               abs(p[0] - x2) <= epsilon and abs(p[1] - y2) <= epsilon:
                continue
            else:
                return True

    # 如果点不在四边形的任何一条边上，则返回 False
    return False

#判断两个线段是否相交：l1 = [(100, 100), (200, 200)] l2 = [(0, 0), (0, 100)]
# def is_intersect(l1, l2):
#     if min(l1[0][0], l1[1][0]) > max(l2[0][0], l2[1][0]) or \
#        max(l1[0][0], l1[1][0]) < min(l2[0][0], l2[1][0]) or \
#        min(l1[0][1], l1[1][1]) > max(l2[0][1], l2[1][1]) or \
#        max(l1[0][1], l1[1][1]) < min(l2[0][1], l2[1][1]):
#         # 两条线段所在的矩形没有相交部分，直接返回不相交
#         return False
#
#     # 计算向量叉积
#     def cross(p1, p2):
#         return p1[0] * p2[1] - p2[0] * p1[1]
#
#     # 判断点 p 是否在线段 l 上
#     def on_segment(p, l):
#         return min(l[0][0], l[1][0]) <= p[0] <= max(l[0][0], l[1][0]) and \
#                min(l[0][1], l[1][1]) <= p[1] <= max(l[0][1], l[1][1])
#
#     # 判断两个线段是否相交
#     p1, p2, p3, p4 = l1[0], l1[1], l2[0], l2[1]
#     if cross((p2[0]-p1[0], p2[1]-p1[1]), (p3[0]-p1[0], p3[1]-p1[1])) * \
#        cross((p2[0]-p1[0], p2[1]-p1[1]), (p4[0]-p1[0], p4[1]-p1[1])) > 0 or \
#        cross((p4[0]-p3[0], p4[1]-p3[1]), (p1[0]-p3[0], p1[1]-p3[1])) * \
#        cross((p4[0]-p3[0], p4[1]-p3[1]), (p2[0]-p3[0], p2[1]-p3[1])) > 0:
#         # 两条线段的延长线相交或者其中一条线段的两个端点在另一条线段同侧，都认为不相交
#         return False
#
#     # 其余情况都认为相交
#     return True
#线段是否相交
def is_intersect(l1, l2):
    p1, p2, p3, p4 = l1[0], l1[1], l2[0], l2[1]
    x1, x2, x3, x4 = p1[0], p2[0], p3[0], p4[0]
    y1, y2, y3, y4 = p1[1], p2[1], p3[1], p4[1]

    # 判断p1p2线段是否与p3p4线段平行
    a = (y4 - y3) * (x2 - x1)
    b = (x4 - x3) * (y2 - y1)

    if abs(a - b) < 1e-8:
        # 判断p1是否在p3p4上
        c = (x1 - x3) * (y4 - y3)
        d = (y1 - y3) * (x4 - x3)
        if abs(c - d) < 1e-8 and c == d:
            return False

        # 判断p2是否在p3p4上
        c = (x2 - x3) * (y4 - y3)
        d = (y2 - y3) * (x4 - x3)
        if abs(c - d) < 1e-8 and c == d:
            return False

        # 判断p3是否在p1p2上
        c = (x3 - x1) * (y2 - y1)
        d = (y3 - y1) * (x2 - x1)
        if abs(c - d) < 1e-8 and c == d:
            return False

        # 判断p4是否在p1p2上
        c = (x4 - x1) * (y2 - y1)
        d = (y4 - y1) * (x2 - x1)
        if abs(c - d) < 1e-8 and c == d:
            return False

        return False
    else:
        # t为交点在p1p2上的位置（比值）,u为交点在p3p4上的位置(比值)
        d = (y4 - y3) * (x2 - x1) - (x4 - x3) * (y2 - y1)
        t = ((x4 - x3) * (y1 - y3) - (y4 - y3) * (x1 - x3)) / d
        u = ((x2 - x1) * (y1 - y3) - (y2 - y1) * (x1 - x3)) / d

        if 0 < t < 1 and 0 < u < 1:
            return True
        else:
            return False

#判断点是否在所有多边形内部 在的话返回真
def is_in_all_abx(p):
    with open('new_file.txt', 'r') as f_in:
        for line in f_in:
            lst = line.split(',')  # 用逗号分隔字符串并生成一个列表
            points = [[int(lst[i]), int(lst[i + 1])] for i in range(0, len(lst), 2)]
            pp=result = tuple(sublst[0] for sublst in p)
            if(is_in_dbx(pp,points)):
                return True

    return False

#判断线段是否和已经存在的多边形相交：放一个线段：l2 = [(0, 0), (10, 10)]
def is_cross_dbx(l):
    with open('new_file.txt', 'r') as f_in:
        for line in f_in:#取出第i个多边形
            lst = line.split(',')  # 用逗号分隔字符串并生成一个列表
            points = [[int(lst[i]), int(lst[i + 1])] for i in range(0, len(lst), 2)]
            points=[(tuple(item) if isinstance(item, list) else item) for item in points]
            for j in range(0,4):
                if(is_intersect(l,(points[j],points[(j+1)%len(points)]))):
                    return True
    return False

#构造路径的长度
def getlength():
    temp=[]
    for i in points_all:
        for j in points_all:
            if i!=j:
                p=[[(i[0]+j[0])/2],[(i[1]+j[1])/2]]
                if not is_cross_dbx([i,j]) and not is_in_all_abx(p):#如果两个点的连线不与四边形相交且中点不在四边形里面
                    l = math.sqrt((i[0] - j[0]) * (i[0] - j[0]) + (i[1] - j[1]) * (i[1] - j[1]))
                    temp.append(l)


                else:
                    temp.append(10000)
            else:temp.append(0)
        length.append(temp)
        temp=[]

    print(length)



#迪杰斯特拉算法
def Dijkstra():
    global road
    number=len(points_all)
    #length=[[None]*number for i in range(number)]#n行n列的二维矩阵表示每个点到每一个点的距离
    getlength()
    final = [False]*number
    dist = [10000]*number
    path = [-1]*number
    final[0] = 1
    dist[0] = 0
    print("all_points")
    print(points_all)
    print(length)
    #get_length()
    for i in range(0,number):
        if length[0][i] != 0 and length[0][i] < 10000:
            dist[i] = length[0][i]
            path[i] = 0
    for i in range(0,number):
        min_val = 10000
        pos = -1
        for j in range(0,number):
            if final[j] == 0 and dist[j] < min_val:
                min_val = dist[j]
                pos = j
        final [pos] = 1

        for k in range(0,number):
            if final[k] == 0 and length[pos][k] + dist[pos] < dist[k]:
                dist[k] = length[pos][k] + dist[pos]
                path[k] = pos
    p = path[number - 1]
    road.append(points_start_end[1])
    while p != -1:
        road.append(points_all[p])
        p = path[p]
    road.append(points_start_end[0])
    print(road)

    #road = list(set(road))
    print(road)
    # ll_sorted = sorted(road, key=lambda x: x[0])
    # for i in range(0,len(ll_sorted)):
    #     if i!=len(ll_sorted)-1:
    #         pygame.draw.line(screen, RED, ll_sorted[i], ll_sorted[i + 1], 2)
    #ll_sorted = sorted(road, key=lambda x: x[0])

    for i in range(0,len(road)):
        if i!=len(road)-1:
            pygame.draw.line(screen, BLACK, road[i], road[i + 1], 2)
def reset():
    points_start_end.clear()
    points_all.clear()
    length.clear()  # 四列三行的二维数组
    road.clear()
    road_points.clear()
    global count
    count = 0
    global start_end
    start_end = False
    print("重置成功")


#次数
count=0
running = True
start_end=False
struct_by_pink=False
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if count!=4 :
                x, y = event.pos
                points.insert(1, event.pos)
                # points_test.append(event.pos)
                count +=1
                pygame.draw.circle(screen, (255, 0, 0), event.pos, 2)
                print(f"鼠标点击位置：({x}, {y})")
            if start_end and len(points_start_end)<2:
                x, y = event.pos
                pygame.draw.circle(screen, (255, 0, 0), event.pos, 5)
                points_start_end.insert(1, event.pos)
                # points_test.append(event.pos)
                #print(f"鼠标点击位置：({x}, {y})")
                print(points_start_end)
                if(len(points_start_end)==2):
                    start_end=False
# 此部分为点击鼠标构造
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 :

            if button_rect.collidepoint(event.pos) and count==4:

                pygame.draw.polygon(screen, (0, 255, 0), points)
                print(points)
                with open("new_file.txt", "a") as f:
                    result_str = ','.join(map(str,points))
                    new_line = result_str.replace(')', '')
                    new_line = new_line.replace('(', '')
                    new_line = new_line.replace(' ', '')
                    f.write(new_line)
                    f.write("\n")

                points.clear()
                count=0
                print("四边形已画出")
            if button_rect.collidepoint(event.pos) and count != 4:
                points.clear()
                count=0
                print("请点击四个点！")
#此部分为读文件构造
            if button_rect_1.collidepoint(event.pos):
                #temp_point=[]
                with open('new_file.txt', 'r') as f_in, open('new_point.txt', 'w') as f_out:
                    for line in f_in:
                        new_line = line.replace(')', '')
                        new_line = new_line.replace('(', '')
                        new_line = new_line.replace(' ', '')
                        f_out.write(new_line)
                    print("文件转换成功")
                with open('new_point.txt', 'r') as f_in:
                    for line in f_in:
                        lst = line.split(',')  # 用逗号分隔字符串并生成一个列表
                        points = [[int(lst[i]), int(lst[i + 1])] for i in range(0, len(lst), 2)]
                        points = [(tuple(item) if isinstance(item, list) else item) for item in points]
                        pygame.draw.polygon(screen, (0, 0, 0), points,1)
#此部分为选取起点和终点
            if button_rect_2.collidepoint(event.pos):
                start_end=True
#此部分为构造最短路径
            if button_rect_3.collidepoint(event.pos):
                addPoints()
                print(points_all)
                Dijkstra()
                print("构造最短路径成功")
                #reset()
# 此部分为重置
            if button_rect_4.collidepoint(event.pos):
                reset()
                print(points_start_end)
                screen.fill(background_color)
                pygame.display.update()


    # 绘制按钮0 顺时针选取四个点，连起来
    pygame.draw.rect(screen, BLACK, button_rect, border_radius=5)
    font = pygame.font.SysFont(None, 15)
    text = font.render("struct by point", True, WHITE)
    text_rect = text.get_rect(center=button_rect.center)
    screen.blit(text, text_rect)
# 绘制按钮1 读取文件，完成障碍构造
    pygame.draw.rect(screen, BLACK, button_rect_1, border_radius=5)
    font1 = pygame.font.SysFont(None, 15)
    text1 = font1.render("struct by file", True, WHITE)
    text_rect1 = text1.get_rect(center=button_rect_1.center)
    screen.blit(text1, text_rect1)
# 绘制按钮2 获取起点和终点
    pygame.draw.rect(screen, BLACK, button_rect_2, border_radius=5)
    font2 = pygame.font.SysFont(None, 15)
    text2 = font2.render("select start and end", True, WHITE)
    text_rect2 = text2.get_rect(center=button_rect_2.center)
    screen.blit(text2, text_rect2)
# 绘制按钮3 计算最短路径
    pygame.draw.rect(screen, BLACK, button_rect_3, border_radius=5)
    font3 = pygame.font.SysFont(None, 15)
    text3 = font3.render("get min road", True, WHITE)
    text_rect3 = text3.get_rect(center=button_rect_3.center)
    screen.blit(text3, text_rect3)
# 绘制按钮4 重置
    pygame.draw.rect(screen, BLACK, button_rect_4, border_radius=5)
    font4 = pygame.font.SysFont(None, 15)
    text4 = font3.render("reset", True, WHITE)
    text_rect4 = text4.get_rect(center=button_rect_4.center)
    screen.blit(text4, text_rect4)
    # 刷新屏幕
    pygame.display.update()

pygame.quit()