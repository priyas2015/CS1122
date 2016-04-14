# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
This file contains all of the agents that can be selected to control Pacman.  To
select an agent, use the '-p' option when running pacman.py.  Arguments can be
passed to your agent using '-a'.  For example, to load a SearchAgent that uses
depth first search (dfs), run the following command:

> python pacman.py -p SearchAgent -a fn=depthFirstSearch

"""

from game import Directions
from game import Agent
from game import Actions
import util
import time
import search
import random

# this is an example Agent
class GoWestAgent(Agent):
    "An agent that goes West until it can't."

    def getAction(self, state):
        "The agent receives a GameState (defined in pacman.py)."
        if Directions.WEST in state.getLegalPacmanActions():
            return Directions.WEST
        else:
            return Directions.STOP

# Part 1
# implement this
class RandomAgent(Agent):
    def __init__(self):
        # This is the constructor. You can initialize data here if you want.
        # You do not need to write anything here if you don't want to.



    def getAction(self, state):
        movement = random.randint(0, len(state.getLegalPacmanActions())-1)
        return state.getLegalPacmanActions()[movement]

# Part 2
# implement this
class SurroundingsAwareAgent(Agent):
    def __init__(self):
        # This is the constructor. You can initialize data here if you want.
        # You do not need to write anything here if you don't want to.
        self.currentAction = Directions.WEST

        self.commands = []
        self.legalCommands = []
        self.pos = ()
        
        self.surroundings = {"above":"", "below":"", "right":"", "left":""}
        
        self.directionalInput = {"above":Directions.NORTH, "below":Directions.SOUTH, "right":Directions.EAST, "left":Directions.WEST}
    
    def getAction(self, state):
        
        self.mapPacman(state)
        self.legalCommands = []
        
        for direction, food in self.surroundings.iteritems():
            
            if food == "food":
                
                self.legalCommands.append(self.directionalInput[direction])
    
        if len(self.legalCommands) == 0:
            
            self.legalCommands = self.commands
                
        if self.currentAction not in self.legalCommands or self.currentAction == Directions.STOP:
            
            self.currentAction = self.legalCommands[random.randint(0, len(self.legalCommands)-1)]
        
        return self.currentAction

    def mapPacman(self, state):
        
        self.position = state.getPacmanPosition()
        self.commands = state.getLegalPacmanActions()
        
        food = state.getFood()
        
        if food[self.pos[0]][self.pos[1]+1]:
            
            self.surroundings["above"] = "food"
        
        else:
            self.surroundings["above"] = ""
        
        
        if food[self.pos[0]][self.pos[1]-1]:
            
            self.surroundings["below"] = "food"
        
        else:
            self.surroundings["below"] = ""
        
        
        if food[self.pos[0]+1][self.pos[1]]:
            
            self.surroundings["right"] = "food"

        else:
            self.surroundings["right"] = ""

        
        if food[self.pos[0]-1][self.pos[1]]:
            
            self.surroundings["left"] = "food"

        else:
            self.surroundings["left"] = ""

