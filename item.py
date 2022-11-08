from os import stat


class Item:
    def __init__(self, nome, writing, status, hasAction, print, action):
        self.nome = nome
        self.writing = writing
        if (status == "None"):
            self.status = "---"
        else:
            self.status = status
        self.hasAction = hasAction
        if (self.hasAction == True):
            self.print = print
            self.action = action
        else:
            self.print = ""
            self.action = ""
        self.hidden = False


    def setHidden(self, value):
        self.hidden = value

    def getHidden(self):
        return self.hidden
           
    def getNome(self):
        return self.nome

    def getWriting(self):
        if self.writing == "None":
            return ""
        else:
            return self.writing

    def getStatus(self):
        if self.status == "None":
            return ""
        else:
            return self.status  

    def setStatus(self, status):
        self.status = status

    def setAction(self, state):
        self.action = state 
    
    def getAction(self):
            return self.action


    def getPrint(self):
            return self.print        
