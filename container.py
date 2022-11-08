class Container:
    def __init__(self, name, item, status, typeTrigger, hasItem, objectNeeded, printTrigger):
        self.name = name
        self.item = item
        self.status = status
        self.typeTrigger = typeTrigger
        self.hasItemCodition = hasItem
        self.neededItem = objectNeeded
        self.printTrigger = printTrigger


    def getNome(self):
        return self.name


    def getTypeTrigger(self):
        return self.typeTrigger

    def hasTrigger(self):
        if (self.typeTrigger != ""):
            return True
        else:
            return False

    def getNeededItem(self):
        return self.neededItem

    def getStatus(self):
        return self.status
    
    def containerTakeItem(self):
        self.item = None

    def containerHasItem(self):
        if(self.item != None):
            return self.item
        else:
            return None
    
    def changeStatus(self):
        if (self.status == "bloqueado"):
            self.status = "desbloqueado"
        elif(self.status == "inativo" or self.status == "Inativo"):
            self.status = "ativo"
        elif(self.status == "em"):
            self.status = "em"
        elif (self.status == "fechado"):
            self.status = "aberto"
        
        
