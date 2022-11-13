from operator import inv
import xml.dom.minidom
from modelSala import Sala
import view
from item import Item
from container import Container
from creature import Criatura
from triggerSala import TriggerSala
all_salas = dict()
inventory = dict()
def parseXML():
    DOMTREE = xml.dom.minidom.parse("aventura.xml")
    collection = DOMTREE.documentElement
    
    #Pegar Salas
    salas = collection.getElementsByTagName("room")
    for sala in salas:
        nomeSala = sala.getElementsByTagName("name")[0].childNodes[0].nodeValue
        descSala = sala.getElementsByTagName("description")[0].childNodes[0].nodeValue

        objSala = Sala(nome=nomeSala, descricao=descSala)

        #pegar Bordas

        bordas = sala.getElementsByTagName("border")
        for borda in bordas:
            direction = borda.getElementsByTagName("direction")
            proxSala = borda.getElementsByTagName("name")
            # for x in range(direction.lenght):
            objSala.putAdjRoom(direcao=direction[0].firstChild.nodeValue, nomeSala=proxSala[0].firstChild.nodeValue)

        

        #itens
        
        itens = sala.getElementsByTagName("item")
        for item in itens:
            name = item.getElementsByTagName("name")[0].firstChild.nodeValue
            
            writing = item.getElementsByTagName("writing")
            if (writing):
                writing = writing[0].firstChild.nodeValue
            else:
                writing = "None"
            
            status = item.getElementsByTagName("status")
            if (status):
                status = status[0].firstChild.nodeValue
            else:
                status = "None"

            turnon = item.getElementsByTagName("turnon")
            if (turnon):
                for tag in turnon:
                    printe = tag.getElementsByTagName("print")[0].firstChild.nodeValue
                    action = tag.getElementsByTagName("action")[0].firstChild.nodeValue
                objItem = Item(name, writing=writing, status=status,hasAction=True, print=printe, action=action )         
            else:
                turnon = "None"
                printe = "None"
                action = "None" 
                objItem = Item(name, writing=writing, status=status,hasAction=False, print=printe, action=action )         
  
        objSala.addItemSala(objItem)
    
        #Containers

        containers = sala.getElementsByTagName("container")
        if(containers):
            for container in containers:
                nome = container.getElementsByTagName("name")[0].firstChild.nodeValue

                itemOnContainer = container.getElementsByTagName("item")
                if (itemOnContainer):
                    for itemC in itemOnContainer:
                        name = itemC.getElementsByTagName("name")[0].firstChild.nodeValue
                        
                        writing = itemC.getElementsByTagName("writing")
                        if (writing):
                            writing = writing[0].firstChild.nodeValue
                        else:
                            writing = "None"
                    
                        status = itemC.getElementsByTagName("status")
                        if (status):
                            status = status[0].firstChild.nodeValue
                        else:
                            status = "None"

                        turnon = itemC.getElementsByTagName("turnon")
                        if (turnon):
                            for tag in turnon:
                                printe = tag.getElementsByTagName("print")[0].firstChild.nodeValue
                                action = tag.getElementsByTagName("action")[0].firstChild.nodeValue
                            objItem = Item(name, writing=writing, status=status,hasAction=True, print=printe, action=action )         
                        else:
                            turnon = "None"
                            printe = "None"
                            action = "None" 
                            objItem = Item(name, writing=writing, status=status,hasAction=False, print=printe, action=action )  

                else:
                    objItem = None
                
                
                status = container.getElementsByTagName("status")
                if (status):
                    status = status[0].firstChild.nodeValue
                else:
                    status = "----"
                
                #Trigger dos containers
                trigger = container.getElementsByTagName("trigger")
                if (trigger):
                    for t in trigger:
                        tipoTrigger = t.getElementsByTagName("type")[0].firstChild.nodeValue
                        
                        hasItem = t.getElementsByTagName("has")
                        if (hasItem):
                            hasItem = hasItem[0].firstChild.nodeValue
                            neededItem = t.getElementsByTagName("object")[0].firstChild.nodeValue
                            printT = t.getElementsByTagName("print")[0].firstChild.nodeValue
                            objContainer = Container(nome, objItem, status=status,typeTrigger =tipoTrigger, hasItem=hasItem, objectNeeded=neededItem, printTrigger =printT )
                            objSala.addContainerSala(objContainer)
                        else:
                            tipoTrigger = ""
                            hasItem = ""
                            neededItem = ""
                            printT = ""  
                else:
                    tipoTrigger = ""
                    hasItem = ""
                    neededItem = ""
                    printT = ""
                    objContainer = Container(nome, objItem, status=status,typeTrigger =tipoTrigger, hasItem=hasItem, objectNeeded=neededItem, printTrigger =printT )
                    objSala.addContainerSala(objContainer)

        #criaturas
        criaturas = sala.getElementsByTagName("creature")

        if (criaturas):
            for criatura in criaturas:
                name = criatura.getElementsByTagName("name")[0].firstChild.nodeValue
                vulner = criatura.getElementsByTagName("vulnerability")
                if (vulner):
                    vulner = vulner[0].firstChild.nodeValue
                else:
                    vulner = "Nao Tem"
                
               
                attack = criatura.getElementsByTagName("attack")
                if (attack):
                    objectAttack = criatura.getElementsByTagName("object")[0].firstChild.nodeValue
                    objectAttackCondition = criatura.getElementsByTagName("status")
                    if(objectAttackCondition):
                        objectAttackCondition = objectAttackCondition[0].firstChild.nodeValue
                    else:
                        objectAttackCondition = "---"
                else:
                    objectAttack = ""
                    objectAttackCondition= ""

                actions = criatura.getElementsByTagName("print")
                if (action):
                    listAction = []
                    textoAcao = actions[0].firstChild.nodeValue
                    for item in objSala.getItem():
                        if (item.getNome() in textoAcao):
                            item.setHidden(True)
                    listAction.append(textoAcao)
                else:
                    listAction = []
                

                trigger = criatura.getElementsByTagName("trigger")
                if (trigger):
                        for t in trigger:
                            triggerItem = t.getElementsByTagName("object")[0].firstChild.nodeValue
                            triggerItemCondition = t.getElementsByTagName("status")
                            if(triggerItemCondition):
                                triggerItemCondition = triggerItemCondition[0].firstChild.nodeValue
                            
                else:
                    triggerItem = condition = ""
                    triggerItemCondition = ""
                    
                objCriatura = Criatura(nome=name, vulnerabilidade=vulner, objectAttack=objectAttack, objectAttackCodition=objectAttackCondition, listActions=listAction, triggerItem=triggerItem, triggerCoditionItem=triggerItemCondition)
                objSala.addCriaturaSala(objCriatura)

        triggersSala = sala.getElementsByTagName("trigger")
        if (triggersSala):
            for t in triggersSala:
                tipo = t.getElementsByTagName("type")[0].firstChild.nodeValue
                comand = t.getElementsByTagName("command")
                if (comand):
                    comand = comand[0].firstChild.nodeValue
                else:
                    comand = ""
                hasCodition = t.getElementsByTagName("condition")
                if (hasCodition):
                    hasCodition = hasCodition[0].firstChild.nodeValue

                    itemTrigger = t.getElementsByTagName("object")
                    if (itemTrigger):
                        itemTrigger = itemTrigger[0].firstChild.nodeValue
                    else:
                        itemTrigger = ""                
                printItem = t.getElementsByTagName("print")
                if (printItem):
                    printItem = printItem[0].firstChild.nodeValue
                else:
                    printItem = ""
                
                novoTrigger = TriggerSala(id=len(objSala.getTriggers()), tipo=tipo, comando=comand, item=itemTrigger, condition=hasCodition, print=printItem)
                objSala.createTrigger(newTrigger=novoTrigger)
        all_salas[nomeSala] = objSala



gameOver = False
firstStart = True

# def teste():
#     s = all_salas.get("Entrada")
#     print(s.getNome())
#     print(s.getDescricao())
    
def startGame(salaAtual, flagFirstStart):
    if (flagFirstStart):
        for sala_nome, salaObjeto in all_salas.items():
            if(salaObjeto.hasContainer()):
                listContainers = salaObjeto.getContainer()
                for container in listContainers:
                    itemContainer = container.containerHasItem()
                    if (itemContainer != None):
                        if (salaAtual.hasEspecificItem(itemContainer)):
                            salaObjeto.removeItemSala(itemContainer)

            
   
    while (gameOver == False):
        view.printInfoSala(salaAtual=salaAtual)
        view.actions(salaAtual=salaAtual)

        


def triggerCriatura(salaAtual):
    criatura = salaAtual.getCriatura()[0]
    triggerItem = criatura.getTriggerItem()
    triggerCond = criatura.getTriggerConditionItem()
    if (checkInventoryForItem(triggerItem)):
        if (inventory.get(triggerItem).getStatus() == triggerCond):
            return True
        else:
            return False
    else:
        return False

def addItemtoInventory(item):
    inventory[item.getNome()] = item


def checkInventoryForItem(item_name):
    if (item_name in inventory):
        return True
    else:
        return False

def checkDrop(criatura, salaAtual):
    textoAcao = criatura.getlistAction()[0]
    for item in salaAtual.getItem():
        if (item.getNome() in textoAcao):
            item.setHidden(False)
        

def activateItem(itemName, status):
    if (inventory.get(itemName) != "---" or itemName != "lanterna"):
        inventory.get(itemName).setStatus(status)
        inventory.get(itemName).setAction("")

def returnInventory():
    return inventory
    


def tryAttack(itemNecessario, codItem):
    if(checkInventoryForItem(itemNecessario)):
        if (inventory.get(itemNecessario).getStatus() == codItem):
            return True, "OK"
        else:
            return False, "Cod item"
    else:
        return False, "Faltou item"

def checkRoomTrigger(dir ,salaAtual):
    if (salaAtual.hasTrigger() == False):
        return False
    else:

        triggers = salaAtual.getTriggers()
        for elementKey, elementValue in triggers.items():
                comando = elementValue.getComando()
                if (comando == dir):
                    if (checkInventoryForItem(elementValue.getItem())):
                        if (elementValue.getTipo() == "unico"):
                            salaAtual.removeTrigger(elementValue)
                            return True
                    else:
                        return elementValue.getPrint()
                

def returnSalas():
    return all_salas