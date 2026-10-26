
from geometry import distance
from scipy.optimize import least_squares

distances = {
    "A1": 3.6055,
    "A2": 3.6055,
    "A3": 5.0,
    "A4": 5.0
}

candidate = (2,2)


# Calculates distance errors between a position and anchors.
def calc_errors(position, anchors, distances):
    errors = []
    for name, anchor in anchors.items():
        candidate_distance = distance(position, anchor)
        error = candidate_distance - distances[name]
        errors.append(error)

    return errors

# Estimates position using least squares method.
def estimate_position(anchors, distances):
    initial_guess=(3,3)
    result=least_squares(calc_errors, initial_guess, args=(anchors, distances))
    return result.x

# Calculates position error distance.
def position_error(actual, estimated):
    error_distance = distance(actual, estimated)

    return error_distance

print(calc_errors((2,2), ANCHORS, distances))
print(estimate_position(ANCHORS,distances))
