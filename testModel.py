from model.model import Model

m = Model()
m.buildGraph()
print("num nodi:", m.getNumNodi())
print("num archi:", m.getNumArchi())