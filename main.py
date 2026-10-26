from config import ANCHORS, target, walls
from simulator import simulate_rssi
from geometry import count_walls, distance
from localization import rssi_to_distance_wall_aware, rssi_to_distance
from measurement import Measurement
from multilateration import estimate_position, position_error,calc_errors

n_samples = 15  

rssi_samples = {}  #{"A1": [15 values], ....}

for name, anchor in ANCHORS.items():
    samples = [] # list of values

    for i in range (n_samples):
        rssi = simulate_rssi(anchor, target, walls)
        samples.append(rssi)

    rssi_samples[name] = samples



# measurement array
measurement_array = []

# Collects simulated RSSI and distance measurements for all anchors.
for i in range(15):
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
    measurement_array.append(signal_points) # append the subarrays(signal_points) to the master array(measurement_array)

# Prints each signal measurement
for m in signal_points:
    print(m)
    print()


# Building the distance dictionary
distances = {}

for m in  measurement_array:  # iterating through the master array
        for i in m:  # iterating through the sub array
            distances[i.name]=i.wall_aware_distance

# Estimates position and calculates the error against the actual target.
estimated = estimate_position(ANCHORS, distances)
actual = target
error = position_error(actual, estimated)

print("Estimated position:", estimated)
print("Actual position:", actual)
print("Position error:", error)
