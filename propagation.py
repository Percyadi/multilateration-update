import math

#estimated RSSI based on distance, path loss, and wall attenuation

def distance_to_rssi(distance, wall_count, rssi_at_1m=-40, path_loss=2.2, wall_loss=5):
    RSSI = rssi_at_1m - 10*path_loss*math.log10(distance) -(wall_count*wall_loss)

    return RSSI
    
