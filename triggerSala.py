class TriggerSala:
    def __init__(self, id, tipo, comando, item, condition, print):
            self.id = id
            self.tipo = tipo
            self.comando = comando
            self.item = item
            self.condition = condition
            self.printTrigger = print

       
    def getComando(self):
        return self.comando

    def getItem(self):
        return self.item
    
    def getTipo(self):
        return self.tipo

    def getPrint(self):
        return self.printTrigger