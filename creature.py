class Criatura:

    def __init__(self, nome, vulnerabilidade, objectAttack, objectAttackCodition, listActions, triggerItem, triggerCoditionItem):
        self.nome = nome
        self.objectAttack = objectAttack
        self.objectAttackCodition = objectAttackCodition
        self.listActions = listActions
        self.vulnerabilidade = vulnerabilidade
        self.triggerItem = triggerItem
        self.triggerCoditionItem= triggerCoditionItem
    
    def getNome(self):
        return self.nome
    
    def getlistAction(self):
        return self.listActions
    
    def getObjectAttack(self):
        return self.objectAttack
    
    def getItemCodition(self):
        return self.objectAttackCodition

    def hasTrigger(self):
        if self.triggerItem != "":
            return True
        else:
            return False
            
    def getTriggerItem(self):
        return self.triggerItem
    
    def getTriggerConditionItem(self):
        return self.triggerCoditionItem