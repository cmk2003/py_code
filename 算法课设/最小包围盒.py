import cv2
import numpy as np
import cv2
import numpy as np
from functools import cmp_to_key

# 判断三个点的顺时针、逆时针、共线关系
def orientation(p, q, r):
    val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
    if val == 0:
        return 0  # 共线
    elif val > 0:
        return 1  # 顺时针
    else:
        return 2  # 逆时针

# 比较函数，用于对点进行排序
def compare(p1, p2):
    o = orientation(p0, p1, p2)
    if o == 0:
        if (p1[0] - p0[0]) ** 2 + (p1[1] - p0[1]) ** 2 >= (p2[0] - p0[0]) ** 2 + (p2[1] - p0[1]) ** 2:
            return -1
        else:
            return 1
    else:
        if o == 2:
            return -1
        else:
            return 1

# 找到最低的点（y坐标最小），如果y坐标相同则选择x坐标最小
def find_lowest_point(points):
    min_idx = 0
    n = len(points)
    for i in range(1, n):
        if points[i][0][1] < points[min_idx][0][1] or (points[i][0][1] == points[min_idx][0][1] and points[i][0][0] < points[min_idx][0][0]):
            min_idx = i
    return points[min_idx][0]

# Graham扫描算法
def convex_hull(points):
    n = len(points)
    if n < 3:
        return []

    hull = []

    # 找到最低点并将其放在列表的开头
    lowest = find_lowest_point(points)
    points[0], points[lowest] = points[lowest], points[0]

    global p0
    p0 = points[0][0]

    # 对点进行排序，根据极角的逆时针顺序进行排序
    sorted_points = sorted(points, key=cmp_to_key(compare))

    hull.append(sorted_points[0][0])
    hull.append(sorted_points[1][0])
    hull.append(sorted_points[2][0])

    for i in range(3, n):
        while len(hull) > 1 and orientation(hull[-2], hull[-1], sorted_points[i][0]) != 2:
            hull.pop()
        hull.append(sorted_points[i][0])

    return hull

def min_bounding_box(points):
    # 找到点集的最小和最大的x坐标和y坐标
    xmin = min(points, key=lambda p: p[0])[0]
    xmax = max(points, key=lambda p: p[0])[0]
    ymin = min(points, key=lambda p: p[1])[1]
    ymax = max(points, key=lambda p: p[1])[1]

    # 构造边界框的四条边
    box = [(xmin, ymin), (xmax, ymin), (xmax, ymax), (xmin, ymax)]

    return box

def min_area_rect(cnt):
    # 计算凸包
    hull = cv2.convexHull(cnt)
    # 对凸包点进行排序
    hull = np.squeeze(hull)
    hull = sorted(hull, key=lambda p: np.arctan2(p[1], p[0]))
    # 初始化最小外接矩形的相关变量
    min_area = float('inf')
    min_rect = None
    # 遍历凸包的边
    for i in range(len(hull)):
        # 计算当前边的角度
        angle = np.arctan2(hull[i][1], hull[i][0])

        # 将凸包旋转到与x轴对齐
        rotated_hull = hull - hull[i]
        rotation_matrix = np.array([[np.cos(angle), -np.sin(angle)],
                                    [np.sin(angle), np.cos(angle)]])
        rotated_hull = np.dot(rotated_hull, rotation_matrix)

        # 计算旋转后凸包的最小外接矩形
        rect = cv2.minAreaRect(rotated_hull)

        # 更新最小外接矩形
        area = rect[1][0] * rect[1][1]
        if area < min_area:
            min_area = area
            min_rect = rect

    return min_rect

image = cv2.imread('bgc.png')
# image = cv2.imread('obstacle.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

ret, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

#构造轮廓
for cnt in contours:
    cv2.drawContours(image, [cnt], 0, (255,0, 0), 2)

temp = []
for cnt in contours:
    # 获取凸包
    hull = cv2.convexHull(cnt)
    # hull=convex_hull(cnt)
    # 将凸包点的坐标存入列表中
    points = []
    for i in range(len(hull)):
        points.append((hull[i][0]/2))
    # 将凸包点的坐标存入 temp 列表中
    temp.append(points)
    # 在图像上绘制凸包
    cv2.drawContours(image, [hull], 0, (100, 100, 255), 2)



print(temp)
temp=temp[1:]
print(temp[0])
tempp=[]
tempp=temp[0]
print(tempp[0][0])
print(tempp[0][1])
new=[]
for i in range(len(tempp)):
    a=(tempp[i][0],tempp[i][1])
    new.append(a)

print(new)
temp=[]
for i in new:
    a=(i[0],i[1])
    temp.append(a)

# with open("new_file.txt", "a") as f:
#     result_str = ','.join(map(str, temp))
#     new_line = result_str.replace(')', '')
#     new_line = new_line.replace('(', '')
#     new_line = new_line.replace(' ', '')
#     f.write(new_line)
#     f.write("\n")





for cnt in contours:
    rect = cv2.minAreaRect(cnt)#函数返回值是一个 (center, size, angle) 元组;
    box = cv2.boxPoints(rect)#cv2.boxPoints(rect) 函数可以将最小矩形转换为 4 个点的坐标，它返回一个形如 [[x1,y1],[x2,y2],[x3,y3],[x4,y4]] 的 ndarray 数组。
    #(box)
    box = np.intp(box)#将坐标数组中的浮点数转换为整型
    print("box",box)
    cv2.drawContours(image,[box],0,(0,0,255),2)

# for cnt in contours:
#     x,y,w,h = cv2.boundingRect(cnt)
#     cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0),2)

cv2.imshow('image',image)
cv2.waitKey(0)
cv2.destroyAllWindows()