# -*- coding: utf-8 -*-
"""
@author: gy19cp

Student ID: 201376715

University of Leeds
___________________


agentframework.py works with both developermodel.py and usermodel.py

developermodel.py contains detailed explanatory comments, testing and debugging.
usermodel.py contains basic comments.

"""

# Libraries imported:
import random

# Constructing Agent (Sheep) class.
class Agent():
    
    def __init__(self, environment, agents, foxes):
        """Initiate class Agents (Sheep) and randomly generate the xy coordinates, environment and food store. 
        All inputs are from the developermodel.py and the usermodel.py"""
        self.x = random.randint(0,99) # Randomly generated. 
        self.y = random.randint(0,99) # Randomly generated.
        self.environment = environment
        self.agents = agents
        self.foxes = foxes
        self.store = 0 # Personal Sheep food storage, at 0 as Sheep haven't eaten yet.
                
    def __str__(self):
        """Returns string with randomly generated xy values, so coordinates can be traced back."""
        return "x=" + str(self.x) + ", y=" + str(self.y)
       
    def distance_between(self, agent): 
        """Calculates distance between Agents (Sheep). Here x and y are randomly generated."""
        return (((self.x - agent.x) **2) + ((self.y - agent.y)**2))**0.5  
    
    def eat(self): 
        """Agents (Sheep) eat grass within the environment, once eaten the patch is darker and pixels are reduced."""
        if self.environment[self.y][self.x] > 10: 
            # If grass patch has greater than 10 units available, it can be eaten. Prevents overgrazing.
            self.environment[self.y][self.x] -= 10 # Eat 10 units of grass.
            self.store += 10 # 10 units of grass to Sheep food store.  
    
    def share_with_neighbours(self, neighbourhood):
        """Distance between two Agents (Sheep) is calculated. If Agents are sufficiently close together food is shared. 
        Neighbourhood defined in both developermodel.py and usermodel.py """
        for i in range(0, len(self.agents)):
            distance = self.distance_between(self.agents[i])
        if distance <= neighbourhood: 
            sum = self.store + self.agents[i].store # Ensures Total Food store is calculated and food is shared equally.
            average = sum/2
            self.store = average 
            self.agents[i].store = average
            #print ("Sharing" + str(distance) + " " + str(average)) # Prints distance between Sheep that are sharing food. 
            # Prints to check it is working correctly.               
               
    def move(self):
        """Sheep move randomly. If the random number generated is greater than 0.5, both the xy coordinates increase by 1 
        and the Sheep moves either North or East. If the number generated is less than 0.5, both the xy coordinates decrease
        by 1 and the Sheep moves either South or West."""        
        if random.random() < 0.5:
            self.y += 1 
        else: 
            self.y -= 1
        if random.random() < 0.5:
            self.x += 1 
        else:
            self.x -= 1     
    # Boundary Effect - Agents prevented from wandering off the model edge.
        if self.y < 0:
            self.y = 0
        if self.x < 0:
            self.x = 0
        if self.y > 99:
            self.y = 99
        if self.x > 99:
            self.x = 99
                       
    def __del__(self):
        """When Foxes are sufficiently close to Sheep, the Sheep point is removed/ 'killed' and the x y coordinates for 
        where the Sheep was removed is printed."""
        print(self.__str__() + "Sheep Killed")


# Constructing Agent (Foxes) class.            
class Foxes(): 
    
    def __init__(self, environment, agents, foxes, y, x):
        """Initiate class Foxes and set up the xy coordinates. Environment and agents (Sheep) can continue to be used 
        from previous code above (within the Agent Framework) and from the model."""
        if (x == None): # If no x value is found from the webpage, a random x coordinate is assigned.
            self.x = random.randint(0,99)
        else:
            self.x = x # Use x coordinate from webpage.
        if (y == None): # If no y value is found from the webpage, a random y coordinate is assigned.
            self.y = random.randint(0,99)
        else:
            self.y = y # Use y coordinate from webpage.
        self.agents = agents    
        self.store = 0 # Foxes Personal Food Store.
   
    def distance_between_foxes(self, agent): 
        """Calculates Distance between Sheep and Foxes."""
        return (((self.x - agent.x) **2) + ((self.y - agent.y)**2))**0.5 # Here x and y are randomly generated.     
     
    def move(self):
        """Foxes move randomly. If the random number generated is greater than 0.5, both the xy coordinates increase 
        by 1 and the Fox moves either North or East. If the number generated is less than 0.5, both the xy coordinates 
        decrease by 1 and the Fox moves either South or West."""
        if random.random() < 0.5:
            self.y += 1 
        else: 
            self.y -= 1
        if random.random() < 0.5:
            self.x += 1 
        else:
            self.x -= 1         
    # Boundary effect - Agents prevented from wandering off the model edge.
        if self.y < 0:
            self.y = 0
        if self.x < 0:
            self.x = 0
        if self.y > 99:
            self.y = 99
        if self.x > 99:
            self.x = 99
            
    def eat_sheep(self,agent):
        """Agents (Foxes) eat/remove the agent (Sheep) and the Foxes food store increases by 1."""
        self.agents.remove(agent)
        self.store += 1               
