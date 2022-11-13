from operator import truediv
from classDict import dictionary
from item import Item
from triggerSala import TriggerSala

class Sala:
    def __init__(self, nome, descricao):
        self.nome = nome
        self.descricao = descricao
        self.salasAdj = dict()
        self.itens = []
        self.containers = []
        self.criaturas = []
        self.trigger = dict()


    def createTrigger(self, newTrigger):
        self.trigger[newTrigger] = newTrigger
        
    def hasTrigger(self):
        if (self.trigger.values != None):
            return True
        else:
            return False
            
    def removeTrigger(self, trigger):
        self.trigger.pop(trigger)

    def putAdjRoom(self,direcao, nomeSala):
        self.salasAdj[direcao] = nomeSala

    def getNome(self):
        return self.nome
    
    def getDescricao(self):
        return self.descricao

    def getTriggers(self):
         return self.trigger

    def getSalasADJ(self):
        for elementKey, elementValue in self.salasAdj.items():
            if(elementKey != None):
                print("Direcao: ", elementKey, "|| Sala: ", elementValue)

   
    def hasSalaAdj(self,key):
        if key in self.salasAdj.keys():
            return True
        else:
            return False

    def returnNameSalaADJ(self,key):
        return self.salasAdj.get(key)

    def addItemSala(self, item):
        self.itens.append(item)

    def removeItemSala(self, item):
        self.itens.remove(item)
    
    def hasEspecificItem(self, item):
        if (self.itens.__contains__(item)):
            return True
        else:
            return False
        
    def hasItem(self):
        if (len(self.itens) > 0):
            return True
        else:
            return False
    
    def getItem(self):
        return self.itens

    def addContainerSala(self, container):
        self.containers.append(container)

    def hasContainer(self):
        if (len(self.containers) > 0):
            return True
        else:
            return False
    
    def getContainer(self):
        return self.containers
    
    def getContainerByIndex(self, index):
        
        return self.containers[index]
    
    def addCriaturaSala(self, criatura):
        self.criaturas.append(criatura)
    
    def hasCriatura(self):
        if (len(self.criaturas) > 0):
            return True
        else:
            return False

    def getCriatura(self):
        return self.criaturas

    def removeCriatura(self, criatura):
        self.criaturas.remove(criatura)