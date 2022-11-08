class dictionary(dict):
    def __init__(self):
        self = dict()
    
    def addPair(self, key, value):
        self[key] = value
    
    def toString(self):
        for elementKey, elementValue in self.items():
            print("Direcao: ", elementKey, "|| Sala: ", elementValue)
            