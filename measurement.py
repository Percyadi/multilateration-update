from dataclasses import dataclass

# store and format RSSI and distance measurements

@dataclass
class Measurement:
    name: str
    wall_count: int
    wall_aware_rssi: float
    basic_rssi: float
    wall_aware_distance: float
    basic_distance: float

    def __str__(self):
        return (
            f"{self.name}\n"
            f"RSSI: {self.wall_aware_rssi:.2f}\n"
            f"Walls: {self.wall_count}\n"
            f"Basic distance: {self.basic_distance:.2f}\n"
            f"Wall-aware distance: {self.wall_aware_distance:.2f}"
        )
