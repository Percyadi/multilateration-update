from config import ANCHORS, target, walls
from simulator import simulate_rssi
from geometry import count_walls, distance
from localization import rssi_to_distance_wall_aware, rssi_to_distance

for name, anchor in ANCHORS.items():
    rssi = simulate_rssi(anchor, target, walls)
    print(name, rssi)


for name, anchor in ANCHORS.items():
    rssi = simulate_rssi(anchor, target, walls)
    estimated_distance = rssi_to_distance(rssi)

    print(name, rssi, estimated_distance)



# distances = {
#     "A1": 3.6055,
#     "A2": 3.6055,
#     "A3": 5.0,
#     "A4": 5.0
# }

# print(distances)

# candidate = (2,2)


# candidate_distance  = distance(candidate, ANCHORS["A1"])

# error = candidate_distance - distances["A1"]

# errors = []

# def calc_errors(position, anchors, distances):
#     errors = []
#     for name, anchor in anchors.items():
#         candidate_distance = distance(candidate, anchor)
#         error = candidate_distance - distances[name]
#         errors.append(error)

#     return errors

# print(calc_errors((2,2), ANCHORS, distances))