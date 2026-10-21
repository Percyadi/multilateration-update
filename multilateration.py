from config import ANCHORS, target, walls
from simulator import simulate_rssi
from geometry import count_walls, distance
from localization import rssi_to_distance_wall_aware, rssi_to_distance
from scipy.optimize import least_squares

distances = {
    "A1": 3.6055,
    "A2": 3.6055,
    "A3": 5.0,
    "A4": 5.0
}

candidate = (2,2)

def calc_errors(position, anchors, distances):
    errors = []
    for name, anchor in anchors.items():
        candidate_distance = distance(position, anchor)
        error = candidate_distance - distances[name]
        errors.append(error)

    return errors

def estimate_position(anchors, distances):
    initial_guess=(3,3)
    result=least_squares(calc_errors, initial_guess, args=(anchors, distances))
    return result.x

def position_error(actual, estimated):
    error_distance = distance(actual, estimated)

    return error_distance

print(calc_errors((2,2), ANCHORS, distances))
print(estimate_position(ANCHORS,distances))
