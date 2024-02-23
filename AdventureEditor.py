# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 12:54:22 2024

@author: chris
"""
import json
def main():
    #getdefault game
    game = getDefaultGame()
    keepGoing = True
    while keepGoing:
        menuChoice = getMenuChoice()
        if menuChoice == "0":
            keepGoing = False
        elif menuChoice == "1":
            print("Loaded the default game.")
            game = getDefaultGame()
        elif menuChoice == "2":
            print("Loaded game file")
            game = loadGame()
        elif menuChoice == "3":
            print("Saved Game.")
            saveGame(game)
        elif menuChoice == "4":
            print("You may now edit or add a node.")
        elif menuChoice == "5":
            print("You are now playing THE game.")
            playGame(game)
            #playGame(game)
        else:
            print("Please select a valid option from numbers 0-5.")

def getMenuChoice():
    keepGoing = True
    while keepGoing:
        print("""
              0) exit
              1) load default game
              2) load a game file
              3) save the current game
              4) edit or add a node
              5) play the current game""")
        menuChoice = input("What will you do?: ")
        if menuChoice in ("0", "1", "2", "3", "4", "5"):
            keepGoing = False
        else:
            print("Please enter a number within 0-5.")
        return menuChoice

def getDefaultGame():
    game = {
        "start": ["You can start over again or quit the game entirely", "Start over", "start", "Quit", "quit"]}
    return game

def playNode(game, currentGame):
    (description, menuA, nodeA, menuB, nodeB) = game[currentGame]
    keepGoing = True
    while keepGoing:
        print(f"""
              {description}
              1) {menuA}
              2) {menuB}
              """)
        response = input("What is your choice?: ")
        if response == "1":
            nextNode = nodeA
            keepGoing = False
        elif response == "2":
            nextNode = nodeB
            keepGoing = False
        else:
            print("Invalid reponse please try again.")
        return nextNode
def playGame(game):
    game = getDefaultGame()
    currentGame = "start"
    keepGoing = True
    while keepGoing:
        currentGame = playNode(game, currentGame)
        if currentGame == "quit":
            keepGoing = False

def saveGame(game):
    saveFile = open("game.json", "w")
    json.dump(game, saveFile, indent = 2)
    print(json.dump(game, saveFile, indent = 2))
    saveFile.close()

def loadGame():
    loadFile = open("game.json", "r")
    game = json.load(loadFile)
    loadFile.close()
    return game

def editNode(game):
    print("These are the current node names in use")
	#given the current game structure...	list all the current node names in the dictionary of “game”
    print(json.dump(game))
	#create variable “nodeName” that will list out all current node names
    for nodeName in game.keys():
        print(f"{nodeName}")
	#allow the input for a "newNodeName"
    newNodeName = input("Please input a new name. If the node name already exists no new node will be added.: ")
    #if "newNodeName" already exists in the keys within the dictionary of "game"
    if newNodeName in game.keys():
        newNode = game[newNodeName]
    else:
        newNode = ["", "", "", "", ""]
	#copy that node to newNode
	#otherwise...
	#create newNode with empty data
	#for each key in the dictionary it will follow the tuple of (description, menuA, nodeA, menuB, nodeB)
    (description, menuA, nodeA, menuB, nodeB) = newNode
    #use editField() to allow user to edit each node
	#return the the new game that is now using the new edited node
    newDescription = getField("description", description)
    newMenuA = getField("Menu A", menuA)
    newNodeA = getField("Node A", nodeA)
    newMenuB = getField("Menu B", menuB)
    newNodeB = getField("Node B", nodeB)
    
    game[newNode] = [newDescription, newMenuA, newNodeA, newMenuB, newNodeB]
    return game
def getField(prompt, currentValue):
    #	get a field name
    newVal = input(f"{prompt} ({currentValue}): ")
    if newVal == "":
        newVal = currentValue
    return newVal
#	print the field's current value
#	if the user presses 'enter' immediately
#	retain the current value
#	otherwise...
#	use the new value

  
main()