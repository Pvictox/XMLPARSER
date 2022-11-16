import math
from unittest import case
import modelSala
import Controller
import os
import time


clear = lambda: os.system('cls')

def printInfoSala(salaAtual):
    clear()
    print("=========================")
    print("Voce está na: ", salaAtual.getNome())
    print(salaAtual.getDescricao())
    print(salaAtual.getSalasADJ())
    if (salaAtual.hasItem()):
        print("******** Itens: ********")
        for item in salaAtual.getItem():
            if (item.getHidden() == False):
                print(item.getNome())
    
    if (salaAtual.hasContainer()):
        print("||||||| Containers: |||||||||")
        for container in salaAtual.getContainer():
            index = salaAtual.getContainer().index(container)
            print("Indice: ", index, "Nome: ", container.getNome())
    
    if (salaAtual.hasCriatura()):
            criat = salaAtual.getCriatura()[0]
            if (criat.hasTrigger()):
                if (Controller.triggerCriatura(salaAtual=salaAtual)):
                    print(" ---------- CRIATURA ----------")
                    for criat in salaAtual.getCriatura():
                        print(criat.getNome())
    
    
    print("=========================")


def actions(salaAtual):
    print("1 - Mover-se")
    print("I - Mostrar inventário")
    if (salaAtual.hasItem()):
        print("2 - Pegar Item")
    if(salaAtual.hasContainer()):
        print("3 - Checar Container")
    if(salaAtual.hasCriatura()):
        print("4 - Enfrentar Criatura")
    entrada = input("Digite o vlor\n")
    if (entrada == "1"):
        dir = input("Digite a direcao\n")
        if (salaAtual.hasSalaAdj(dir) == False):
            print("Digite uma direcao valida")
        else:

                resultTrigger = Controller.checkRoomTrigger(dir, salaAtual=salaAtual)
                if(resultTrigger == True or resultTrigger == None):
                    print("Entrou")
                    Controller.applyMovemment(dir, salaAtual=salaAtual)
                elif(resultTrigger != False):
                    print(resultTrigger)
                    time.sleep(1.2)

    elif (entrada == "2"):
        nomeItem = input("Digite o nome do item\n")
        if (salaAtual.hasItem()):
            for item in salaAtual.getItem():
                if (item.getNome() == nomeItem):
                    salaAtual.removeItemSala(item)
                    Controller.addItemtoInventory(item)
            print("Digite o nome corretamente")    
        else:
            print("Não há itens na sala")
    elif (entrada == "I" or entrada == "i"):
        clear()
        inv = Controller.returnInventory()
        if (len(inv) == 0):
            print("Sem nada por enquanto!")
            
        else:
            for key, value in inv.items():
                print("Chave: ", key, " || Descrição: ", value.getWriting())
                print("Status:", value.getStatus())
                if (value.getAction() != "" and value.getAction() != "---"):
                    print("É possível ativar")
                print("=====================")
            item_escolha = input("Digite o nome do item para ativar (0 para sair)\n")
            if (item_escolha == "0"):
                    Controller.startGame(salaAtual=salaAtual, flagFirstStart=False)
            if not inv.get(item_escolha):
                    print("Digite o nome corretamente")
            else:
                    Controller.activateItem(item_escolha, "aceso")
                
            
            time.sleep(2.0)
    elif(entrada == "3"):
        index = input("Digite o indice do container\n")
        index = int(index)
        container = salaAtual.getContainerByIndex(index)
        if(container != None):
            showContainerInfo(container=container, salaAtual=salaAtual)
        else:
            print("Digite um nome válido")
            time.sleep(2.0)
            Controller.startGame(salaAtual=salaAtual, flagFirstStart=False)
    elif(entrada == "4"):
        criatura = salaAtual.getCriatura()[0]
        itemPreciso = criatura.getObjectAttack()
        conditionItemPreciso = criatura.getItemCodition()
        flag, texto = Controller.tryAttack(itemNecessario=itemPreciso, codItem=conditionItemPreciso)
        if (flag == False):
            print("Ataque falhou! Motivo: ")
            if (texto == "Cod item"):
                print("Item não esta ", conditionItemPreciso)
            elif(texto == "Faltou item"):
                print("Faltou item ", itemPreciso)
            time.sleep(2.0)
            Controller.startGame(salaAtual=salaAtual, flagFirstStart=False)
        else:       
            print("Ataque Sucesso!")
            print(criatura.getlistAction()[0])
            Controller.checkDrop(criatura=criatura, salaAtual=salaAtual)
            salaAtual.removeCriatura(criatura)
            time.sleep(2.0)
            Controller.startGame(salaAtual=salaAtual, flagFirstStart=False)



def showContainerInfo(container, salaAtual):
   
    print("Nome: ", container.getNome())
    print("Status do container: ", container.getStatus())
    if (container.containerHasItem() != None):
        print("Item dentro: ", container.containerHasItem().getNome())
        print("Digite 1 para pegar o item")
        itemPegar = input()
        if (itemPegar == "1"):
            item = container.containerHasItem()
            Controller.addItemtoInventory(item=item)
            container.containerTakeItem()
            Controller.startGame(salaAtual=salaAtual, flagFirstStart=False)

    else:
        print("Não tem item dentro")
    
    
    if (container.hasTrigger()):
        print("Digite T para verificar Trigger")
        inputTrigger = input()
        if (inputTrigger == "T" or inputTrigger == "t"):
            if(Controller.checkInventoryForItem(container.getNeededItem())):
                container.changeStatus()
                print("SUCESSO!")
                time.sleep(1.0)
                Controller.startGame(salaAtual=salaAtual, flagFirstStart=False)
            else:
                print("Trigger falhou, vc nao possui: ", container.getNeededItem() )
    print("Digite 0 para voltar")
    ent = input()
    if (ent == "0"):
        Controller.startGame(salaAtual=salaAtual, flagFirstStart=False)


        
