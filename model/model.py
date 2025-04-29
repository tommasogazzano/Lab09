from database.DAO import DAO
import networkx as nx

class Model:
    def __init__(self):
        self._aeroporti = DAO.getAeroporti()
        self._grafo = nx.Graph()
        self._idAeroporti = {}
        self._limite = 2000
        for a in self._aeroporti:
            self._idAeroporti[a.ID] = a

    def buildGraph(self):
        self._grafo.add_nodes_from(self._aeroporti)
        self.addEdges(self._limite)

    def addEdges(self, limite):
        collegamenti = DAO.getVoli()
        for volo in collegamenti:
            u = self._aeroporti[volo.ORIGIN_AIRPORT_ID]
            v = self._aeroporti[volo.DESTINATION_AIRPORT_ID]
            peso = float(volo.AVERAGE_DISTANCE)
            if float(limite) < peso:
                self._grafo.add_edge(u, v, weight=peso)

    def getNumNodi(self):
        return len(self._grafo.nodes)

    def getNumArchi(self):
        return len(self._grafo.edges)

    def stampaVoli(self):
        output = ""
        for e in self._grafo.edges(data=True):
            output += f"FROM: {e[0].IATA_CODE} - {e[0].AIRPORT} TO {e[1].IATA_CODE} - {e[1].AIRPORT} -- {e[2]['weight']} miles \n"
        return output

