import math
import mathUtil
from vector2D import Vector2D
import shapes

class CollisionObject:
    def __init__(self, shape, collisionType):
        #position is bottom left point
        self.shape = shape
        self.collisionType = collisionType
        self.exitScreen = None
        self.exitDirection = None
        self.parentEntity = None
    
    def SetAttributes(self, attributes):
        if self.collisionType == "exit":
            self.exitScreen = attributes.split()[0] + "Data"
            self.exitDirection = attributes.split()[1]
            if self.exitDirection == "up":
                self.shape.position.y += 32
            if self.exitDirection == "right":
                self.shape.position.x += 32
            if self.exitDirection == "down":
                self.shape.position.y -= 32
            if self.exitDirection == "left":
                self.shape.position.x -= 32   
    
        
            
    #check if collision occurs with other collisionObject, if so add results to list
    def GenerateContact(self, other, collResultsList):
        collResult = self.shape.Intersects(other.shape)
        if collResult is not None:
            collResult.objA = self
            collResult.objB = other
            collResultsList.append(collResult)
            
        