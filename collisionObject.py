import math
import mathUtil
from vector2D import Vector2D
import shapes

class CollisionObject:
    def __init__(self, shape, collisionType):
        #position is bottom left point
        self.shape = shape
        self.collisionType = collisionType
        self.parentEntity = None
            
    #check if collision occurs with other collisionObject, if so add results to list
    def GenerateContact(self, other, collResultsList):
        collResult = self.shape.Intersects(other.shape)
        if collResult is not None:
            collResult.objA = self
            collResult.objB = other
            collResultsList.append(collResult)
            
        