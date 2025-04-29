from database.DB_connect import DBConnect
from model.Aeroporto import Aeroporto
from model.Volo import Volo


class DAO():
    def __init__(self):
        pass

    @staticmethod
    def getAeroporti():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = "SELECT * FROM extflightdelays.airports a"
        cursor.execute(query)

        for row in cursor:
            result.append(Aeroporto(**row))
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getVoli():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """
            SELECT 
                LEAST(f.ORIGIN_AIRPORT_ID, f.DESTINATION_AIRPORT_ID) as ORIGIN_AIRPORT_ID,
                GREATEST(f.ORIGIN_AIRPORT_ID, f.DESTINATION_AIRPORT_ID) as DESTINATION_AIRPORT_ID,
                AVG(f.DISTANCE) as AVERAGE_DISTANCE
            FROM extflightdelays.flights f
            GROUP BY 
                LEAST(f.ORIGIN_AIRPORT_ID, f.DESTINATION_AIRPORT_ID),
                GREATEST(f.ORIGIN_AIRPORT_ID, f.DESTINATION_AIRPORT_ID)
            HAVING COUNT(*) > 0
            ORDER BY 
                LEAST(f.ORIGIN_AIRPORT_ID, f.DESTINATION_AIRPORT_ID),
                GREATEST(f.ORIGIN_AIRPORT_ID, f.DESTINATION_AIRPORT_ID)
            """
        cursor.execute(query)

        for row in cursor:
            result.append(Volo(**row))
        cursor.close()
        conn.close()
        return result

