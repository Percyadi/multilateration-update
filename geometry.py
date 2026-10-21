import math

def distance(pt1, pt2):
    dist = math.dist(pt1, pt2)

    return dist

def ccw(A, B, C):
    x1, y1 = A
    x2, y2 = B
    x3, y3 = C

    if ((y3-y1)*(x2-x1)>(y2-y1)*(x3-x1)):
        return True
    else: return False

def segments_intersect(A, B, C, D):

    if((ccw(A,C,D) != ccw(B,C,D)) and (ccw(A,B,C) != ccw(A,B,D))):
        return True

    else: return False

def count_walls(anchor, target, walls):
    wall_count = 0
    for i in range(len(walls)):
        wall_start = walls[i][0]
        wall_end = walls[i][1]
        if(segments_intersect(anchor, target, wall_start, wall_end)):
            wall_count = wall_count + 1

    return wall_count
