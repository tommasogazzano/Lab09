from dataclasses import dataclass


@dataclass
class Volo:
    ORIGIN_AIRPORT_ID: int
    DESTINATION_AIRPORT_ID: int
    AVERAGE_DISTANCE: float

    def __hash__(self):
        return hash(self.ORIGIN_AIRPORT_ID)

    def __eq__(self, other):
        return (self.ORIGIN_AIRPORT_ID == other.ORIGIN_AIRPORT_ID and self.DESTINATION_AIRPORT_ID == other.DESTINATION_AIRPORT_ID)