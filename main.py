# config has defination of sources and walls
from config import ANCHORS, target, walls
from simulator import simulate_rssi
from geometry import count_walls, distance
from localization import rssi_to_distance_wall_aware, rssi_to_distance
from measurement import Measurement
from multilateration import estimate_position, position_error,calc_errors


signal_points = []

for name, anchor in ANCHORS.items():
    wall_count = count_walls(anchor, target, walls)
    wall_aware_rssi = simulate_rssi(anchor, target, walls)
    basic_rssi = simulate_rssi(anchor, target, [])

    m = Measurement(
        name=name,
        wall_count=wall_count,
        wall_aware_rssi=wall_aware_rssi,
        basic_rssi=basic_rssi,
        wall_aware_distance=rssi_to_distance_wall_aware(wall_aware_rssi, wall_count),
        basic_distance=rssi_to_distance(wall_aware_rssi),
    )
    signal_points.append(m)


for m in signal_points:
    print(m)
    print()


distances = {
    "A1": 3.6055,
    "A2": 3.6055,
    "A3": 5.0,
    "A4": 5.0
}

estimated = estimate_position(ANCHORS, distances)
actual = target
error = position_error(actual, estimated)

print("Estimated position:", estimated)
print("Actual position:", actual)
print("Position error:", error)

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
#imported all the functions from multilateration
#using distance dictionary found out estiamted position, actual position and position error and printed it 