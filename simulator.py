import random
from geometry import distance, count_walls
from propagation import distance_to_rssi
noise_std = 2

#Simulates a noisy RSSI measurement between an anchor and target by accounting for distance, wall obstructions, and Gaussian noise.

def simulate_rssi(anchor, target, walls, noise_std=noise_std):
    dist_anchor_target = distance(anchor, target)
    sim_count_walls =  count_walls(anchor, target, walls)
    rssi = distance_to_rssi(dist_anchor_target, sim_count_walls)
    noisy_rssi = random.gauss(rssi, noise_std)
    return noisy_rssi

