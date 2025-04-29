from dataclasses import dataclass


@dataclass
class Aeroporto:
    ID: int
    IATA_CODE: str
    AIRPORT: str
    CITY: str
    STATE: str
    COUNTRY: str
    LATITUDE: float
    LONGITUDE: float
    TIMEZONE_OFFSET: int

    def __hash__(self):
        return hash(self.ID)

    def __eq__(self, other):
        return self.ID == other.ID

    def str(self):
        return f"{self.IATA_CODE} - {self.AIRPORT}"
