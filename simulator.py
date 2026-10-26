import random
from geometry import distance, count_walls
from propagation import distance_to_rssi
noise_std = 2

def simulate_rssi(anchor, target, walls, noise_std=noise_std):
    dist_anchor_target = distance(anchor, target)
    sim_count_walls =  count_walls(anchor, target, walls)
    rssi = distance_to_rssi(dist_anchor_target, sim_count_walls)

    return random.gauss(rssi, noise_std)

