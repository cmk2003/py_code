# 导入pygame和math模块
import pygame
import math

# 定义一些常用颜色
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK=(0,0,0)

# 定义窗口大小并初始化pygame
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 800
pygame.init()

# 创建窗口对象和设置窗口标题
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("路径选择")

# 设置背景颜色为白色
background_color = (255, 255, 255)
screen.fill(background_color)
pygame.display.update()

# 加载背景图片，并设置其位置和大小
bg_img = pygame.image.load("img_3.png")
bg_img = pygame.transform.scale(bg_img, (800, 600))

# 创建按钮对象，并设置其位置和大小
button_width = 100
button_height = 50
button_x=0
button_y=0
button_rect = pygame.Rect(button_x, button_y, button_width, button_height)
button_rect_1 = pygame.Rect(button_x+button_width+20, button_y, button_width, button_height)
button_rect_2 = pygame.Rect(button_rect_1.x+button_width+20, button_y, button_width, button_height)
button_rect_3 = pygame.Rect(button_rect_2.x+button_width+20, button_y, button_width, button_height)
button_rect_4 = pygame.Rect(button_rect_3.x+button_width+20, button_y, button_width, button_height)

# 绘制背景图片
screen.blit(bg_img, (0, 100))

# 记录所有点坐标的列表
points = []
points_start_end=[]
points_all =[]
length =[]; # 四列三行的二维数组
road=[]
# road_points = []

# 向 points_all 中添加起点和终点，同时从文件中读取其余点的坐标，并添加到 points_all 中
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

# 判断一个点是否在一个四边形内部
def is_in_dbx(p, quadrilateral):
    x, y = p
    n = len(quadrilateral)
    inside = False

    # 计算多边形的边界
    x_min, y_min = map(min, zip(*quadrilateral))
    x_max, y_max = map(max, zip(*quadrilateral))

    # 如果点在多边形边界之外，则返回 False
    if x < x_min or x > x_max or y < y_min or y > y_max:
        return False

    # 计算点向右射线与多边形的交点数
    i = 0
    j = n - 1
    while i < n:
        if ((quadrilateral[i][1] > y) != (quadrilateral[j][1] > y)) and \
                (x < (quadrilateral[j][0] - quadrilateral[i][0]) * (y - quadrilateral[i][1]) /
                 (quadrilateral[j][1] - quadrilateral[i][1]) + quadrilateral[i][0]):
            inside = not inside
        j = i
        i += 1

    return inside



def is_on_edge(p, vertices):
    # 判断点是否在多边形的外接矩形内，如果不在则肯定不在其边上

    min_x = min(v[0] for v in vertices)
    max_x = max(v[0] for v in vertices)
    min_y = min(v[1] for v in vertices)
    max_y = max(v[1] for v in vertices)
    if p[0] < min_x or p[0] > max_x or p[1] < min_y or p[1] > max_y:
        return False

    # 遍历多边形的每一条边，计算该边所在直线与点之间的距离
    epsilon = 1e-10
    for i in range(len(vertices)):
        j = (i + 1) % len(vertices)
        # 计算点到直线的距离
        x1, y1 = vertices[i]
        x2, y2 = vertices[j]
        distance = abs((y2 - y1) * p[0] - (x2 - x1) * p[1] + x2 * y1 - y2 * x1) / ((y2 - y1) ** 2 + (x2 - x1) ** 2) ** 0.5
        # 如果距离小于等于 epsilon，则认为点在当前边上
        if distance <= epsilon:
            # 判断点是否恰好落在顶点上
            if abs(p[0] - x1) <= epsilon and abs(p[1] - y1) <= epsilon or \
               abs(p[0] - x2) <= epsilon and abs(p[1] - y2) <= epsilon:
                continue
            else:
                return True

    # 如果点不在多边形的任何一条边上，则返回 False
    return False


#两条线段是否相交
def is_intersect(l1, l2):

    p1, p2, p3, p4 = l1[0], l1[1], l2[0], l2[1]
    x1, x2, x3, x4 = p1[0], p2[0], p3[0], p4[0]
    y1, y2, y3, y4 = p1[1], p2[1], p3[1], p4[1]

    # 判断p1p2线段是否与p3p4线段平行
    a = (y4 - y3) * (x2 - x1)
    b = (x4 - x3) * (y2 - y1)

    if abs(a - b) < 1e-8:
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

        # 判断p1是否在p3p4上 是否共线
        c = (x1 - x3) * (y4 - y3)
        d = (y1 - y3) * (x4 - x3)
        if abs(c - d) < 1e-8 and c == d:
            return False

        # 判断p2是否在p3p4上
        c = (x2 - x3) * (y4 - y3)
        d = (y2 - y3) * (x4 - x3)
        if abs(c - d) < 1e-8 and c == d:
            return False



        return False
    else:
        # t为交点在p1p2上的位置（比值）,u为交点在p3p4上的位置(比值)
        d = (y4 - y3) * (x2 - x1) - (x4 - x3) * (y2 - y1)  # 两条线段的斜率分母
        t = ((x4 - x3) * (y1 - y3) - (y4 - y3) * (x1 - x3)) / d  # 计算交点在p1p2上的位置（比值）
        u = ((x2 - x1) * (y1 - y3) - (y2 - y1) * (x1 - x3)) / d  # 计算交点在p3p4上的位置（比值）

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
            for j in range(0,len(points)):
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
    number=len(points_all)# 计算点集的数量
    #length=[[None]*number for i in range(number)]#n行n列的二维矩阵表示每个点到每一个点的距离
    getlength()# 调用getlength函数，构造路径的长度
    final = [False] * number  # 定义final数组，表示是否已经找到最短路径
    dist = [10000] * number  # 定义dist数组，表示源点到各个点的最短距离
    path = [-1] * number  # 定义path数组，表示最短路径中到达该点的前一个点的序号
    final[0] = 1  # 初始时，源点为已知最短路径
    dist[0] = 0

    # 初始化dist和path数组
    for i in range(0,number):
        if length[0][i] != 0 and length[0][i] < 10000:
            dist[i] = length[0][i]
            path[i] = 0
    # 对于剩余的未知点进行计算
    for i in range(0,number):
        min_val = 10000
        pos = -1
        # 找到当前未知点中距离源点最近的那个点
        for j in range(0,number):
            if final[j] == 0 and dist[j] < min_val:
                min_val = dist[j]
                pos = j
        # 将找到的点标记为已经找到了最短路径
        final [pos] = 1
        # 更新dist和path数组
        for k in range(0,number):
            if final[k] == 0 and length[pos][k] + dist[pos] < dist[k]:
                dist[k] = length[pos][k] + dist[pos]
                path[k] = pos
    # 构造最短路径
    p = path[number - 1]
    road.append(points_start_end[1])
    while p != -1:
        road.append(points_all[p])
        p = path[p]
    road.append(points_start_end[0])
    print(road)
    for i in range(0,len(road)):
        if i!=len(road)-1:
            pygame.draw.line(screen, BLACK, road[i], road[i + 1], 2)

def reset():
    points_start_end.clear()
    points_all.clear()
    length.clear()
    road.clear()
    # road_points.clear()
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
            if count!=30 :
                x, y = event.pos
                if y>50:#最多五十个点（点击规则）
                    points.insert(1, event.pos)
                    # points_test.append(event.pos)
                    count += 1
                    pygame.draw.circle(screen, (255, 0, 0), event.pos, 2)
                    print(f"鼠标点击位置：({x}, {y})")

            if start_end and len(points_start_end)<2:#点击起点和终点的点击规则
                x, y = event.pos
                pygame.draw.circle(screen, (255, 0, 0), event.pos, 5)
                points_start_end.insert(1, event.pos)
                # points_test.append(event.pos)
                #print(f"鼠标点击位置：({x}, {y})")
                print(points_start_end)
                if(len(points_start_end)==2):
                    start_end=False
# 此部分为点击鼠标构造
        if event.type == pygame.MOUSEBUTTONDOWN  :

            if button_rect.collidepoint(event.pos) :

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
                print("多边形已画出")
            # if button_rect.collidepoint(event.pos) and count != 10:
            #     points.clear()
            #     count=0
            #     print("请点击四个点！")
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
                with open('new_file.txt', 'r') as f_in:
                    for line in f_in:
                        lst = line.split(',')  # 用逗号分隔字符串并生成一个列表
                        points = [[int(lst[i]), int(lst[i + 1])] for i in range(0, len(lst), 2)]
                        points = [(tuple(item) if isinstance(item, list) else item) for item in points]
                        print(points)
                        for i in points:
                            pygame.draw.circle(screen, (255, 0, 0), i, 2)

                        pygame.draw.polygon(screen, (0, 0, 0), points,1)
                        points.clear()

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