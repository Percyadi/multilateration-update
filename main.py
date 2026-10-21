from config import ANCHORS, target, walls
from simulator import simulate_rssi
from geometry import count_walls
from localization import rssi_to_distance_wall_aware, rssi_to_distance

for name, anchor in ANCHORS.items():
    rssi = simulate_rssi(anchor, target, walls)
    print(name, rssi)


for name, anchor in ANCHORS.items():
    rssi = simulate_rssi(anchor, target, walls)
    estimated_distance = rssi_to_distance(rssi)

    print(name, rssi, estimated_distance)
