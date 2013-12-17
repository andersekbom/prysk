## Imports ###########################
import sys
import _battle
import _map
import classes
from Tkinter import *
from time import sleep
from termcolor import colored

## Mechanics #####################################################################

def attackTerritory(aTerritory,dTerritory):

    #################################################
    ##
    ## Takes two territory objects and battles it out
    ##
    #################################################

    print colored("Attacker has %s troops in %s,","blue") % (aTerritory.troops,aTerritory.name)
    print colored("Defender has %s troops in %s.","blue") % (dTerritory.troops,dTerritory.name)
    
    if aTerritory.troops > 3:
        maxTroops = 3
    else:
        maxTroops = aTerritory.troops-1 # Need to leave 1 troop to defend

    question = "How many troops to attack with (max %s)? >> " % maxTroops
    numberOfAttackers = int(raw_input(question))

    ## Actual battle
    defenderLost,attackerLost = _battle.doBattle(dTerritory,numberOfAttackers)

    dTerritory.troops -= defenderLost
    aTerritory.troops -= attackerLost
    print colored("Attacker lost %s.","yellow") % attackerLost
    print colored("Defender lost %s.","yellow") % defenderLost
    sleep(1)

    _map.updateTerritory(dTerritory.name,dTerritory.troops,dTerritory.owner)
    _map.updateTerritory(aTerritory.name,aTerritory.troops,aTerritory.owner)

    ## Check results

    if dTerritory.troops > 0 and aTerritory.troops > 1:
        print
        if raw_input("Attack same territory again? (y/n) >> ") == "y":
            attackTerritory(aTerritory,dTerritory)
        elif raw_input("Attack another territory? (y/n) >> ") == "y":
            attacker = selectATerritory(objPlayer)
            print "You are attacking from %s!" % attacker.name
            sleep(1)
            defender = selectDTerritory(objPlayer)
            attackTerritory(attacker,defender)

    elif dTerritory.troops > 0 and aTerritory.troops == 1:
        print colored("You don't have enough troops to attack.","red")
        print colored("%s is still owned by %s.","green") % (dTerritory.name,dTerritory.owner)
        if raw_input("Attack another territory? (y/n) >> ") == "y":
            attacker = selectATerritory(objPlayer)
            print "You are attacking from %s!" % attacker.name
            sleep(1)
            defender = selectDTerritory(objPlayer)
            attackTerritory(attacker,defender)

    elif dTerritory.troops == 0:
        dTerritory.owner = player
        dTerritory.troops = numberOfAttackers-attackerLost
        print colored("%s has been conquered","green") % dTerritory.name,
        print colored("and is now owned by %s.","green") % dTerritory.owner
        _map.updateTerritory(aTerritory.name,aTerritory.troops-dTerritory.troops,aTerritory.owner)
        _map.updateTerritory(dTerritory.name,dTerritory.troops,dTerritory.owner)
        
        if raw_input("Attack another territory? (y/n) >> ") == "y":
            attacker = selectATerritory(objPlayer)
            print "You are attacking from %s!" % attacker.name
            sleep(1)
            defender = selectDTerritory(objPlayer)
            attackTerritory(attacker,defender)

    else:
        print "Ooops."


def drawNewTroops(player):
    print "Drawing troops..."
    player.troops += 3
    sleep(1)



def deployTroops(player):
    # put troops in various territories
    print "Deploying troops..."
    sleep(1)



def moveTroops(player):
    ## Change existing troop counts
    print "Moving troops..."
    sleep(1)




def playerRound(objPlayer):

    drawNewTroops(objPlayer)

    deployTroops(objPlayer)

    if raw_input("Attack? (y/n) >>") == "y":

        attacker = selectATerritory(objPlayer)
        print "You are attacking from %s!" % attacker.name
        sleep(1)
        defender = selectDTerritory(objPlayer)
        
        attackTerritory(attacker,defender)

    if raw_input("Do you wish to move troops? (y/n) >>") == "y":
        moveTroops(player)

    print "End of turn."

    
def selectATerritory(objPlayer):

    print "Select territory to attack from:"
    # get available territories
    availableTerritories = _map.listAttTerritories(objPlayer)
    
    t=1
    for terr in availableTerritories:
        print "[%s] %s (%s)" % (t,terr[0],terr[1])
        t+=1
    
    # select attacking territory
    selectedTerritory = int(raw_input(">> "))
    attTerrName = availableTerritories[selectedTerritory-1][0]
    attTerrTroops = availableTerritories[selectedTerritory-1][1]
    return classes.Territory(attTerrName,attTerrTroops,objPlayer.name)

def selectDTerritory(player):

    print "Select territory to attack:"
    # get available territories
    availableTerritories = _map.listDefTerritories(objPlayer)
    
    t=1
    for terr in availableTerritories:
        print "[%s] %s (%s)" % (t,terr[0],terr[1])
        t+=1
    
    # select attacking territory
    selectedTerritory = int(raw_input(">> "))
    defTerrName = availableTerritories[selectedTerritory-1][0]
    defTerrTroops = availableTerritories[selectedTerritory-1][1]
    defTerrOwner = availableTerritories[selectedTerritory-1][2]
    return classes.Territory(defTerrName,defTerrTroops,defTerrOwner)

## Game ########################################################################


## Setup
_map.initMap()

## Play ########################################################################
# player1 = Player("Red","red")

for player in _map.players:
    print "You are %s!" % player
    objPlayer = classes.Player(player,player)
    playerRound(objPlayer)
    print "Next player!"



## Goodbye

print "Game over."
