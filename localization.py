# Estimates distance from RSSI, accounting for wall as well.
def rssi_to_distance_wall_aware(rssi, wall_count, rssi_at_1=-40, path_loss=2.2, wall_loss=5):
    total_wall_loss = wall_count*wall_loss
    d = 10**((rssi_at_1 - rssi - total_wall_loss)/(10*path_loss))

    return d

# Estimates distance from RSSI using basic path loss model.
def rssi_to_distance(rssi, rssi_at_1 = -40, path_loss = 2.2):
    d = 10**((rssi_at_1 - rssi) / (10*path_loss))

    return d
