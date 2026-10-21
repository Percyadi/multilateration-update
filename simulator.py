import math

def distance(pt1, pt2):
    dist = math.dist(pt1, pt2)

    return dist

def distance_to_rssi(distance, wall_count, rssi_at_1m=-40, path_loss=2.2, wall_loss=5):
    RSSI = rssi_at_1m - 10*path_loss*math.log10(distance) -(wall_count*wall_loss)

    return RSSI

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

def simulate_rssi(anchor, target, walls):
    dist_anchor_target = distance(anchor, target)
    sim_count_walls =  count_walls(anchor, target, walls)
    rssi = distance_to_rssi(dist_anchor_target, sim_count_walls)

    return rssi

ANCHORS = {
    "A1": (0, 0),
    "A2": (6, 0),
    "A3": (0, 6),
    "A4": (6, 6)
}

target = (3,2)

walls = [
    ((2, 3), (5, 3))
]

for name, anchor in ANCHORS.items():
    rssi = simulate_rssi(anchor, target, walls)
    print(name, rssi)

def rssi_to_distance(rssi, rssi_at_1 = -40, path_loss = 2.2):
    d = 10**((rssi_at_1 - rssi) / (10*path_loss))

    return d

for name, anchor in ANCHORS.items():
    rssi = simulate_rssi(anchor, target, walls)
    estimated_distance = rssi_to_distance(rssi)

    print(name, rssi, estimated_distance)

def rssi_to_distance_wall_aware(rssi, wall_count, rssi_at_1=-40, path_loss=2.2, wall_loss=5):
    total_wall_loss = wall_count*wall_loss
    d = 10**((rssi_at_1 - rssi - total_wall_loss)/(10*path_loss))

    return d

print(rssi_to_distance_wall_aware(-60.37734009539241, 1))