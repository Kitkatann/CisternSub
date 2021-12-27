import math
from vector2D import Vector2D
import load
import levelData
from shapes import Circle
from collisionObject import CollisionObject

class Player:
    def __init__(self, active, position, velocity, rotation):
        self.active = active
        #position is center point
        self.position = position.Clone()
        self.velocity = velocity
        self.rotation = rotation
        self.friction = 1.0
        self.collisionObj = CollisionObject(Circle(position.Clone(), 20), "player")
        self.width = 64
        self.height = 35

    def Collide(self, collResult):
        if collResult.objA.collisionType == "wall":
            self.CollideWithWall(collResult)
        if collResult.objA.collisionType == "exit":
            self.CollideWithExit(collResult)
        if collResult.objA.collisionType == "mine":
            self.CollideWithMine(collResult)
    
    def CollideWithWall(self, collResult):
        self.position += collResult.normal * collResult.depth
        
        #bouncy
        self.velocity.Bounce(collResult.normal)
    
    def CollideWithExit(self, collResult):
        collisionObj = collResult.objA
        load.LoadLevelData(collisionObj.exitScreen)
        if collisionObj.exitDirection == "up":
            self.position.y += -levelData.screenHeight + 56
        elif collisionObj.exitDirection == "right":
            self.position.x += -levelData.screenWidth + 56
        elif collisionObj.exitDirection == "down":
            self.position.y += levelData.screenHeight - 56
        elif collisionObj.exitDirection == "left":
            self.position.x += levelData.screenWidth - 56
        
    def CollideWithMine(self, collResult):
        collisionObj = collResult.objA
        #explode the mine
        if collisionObj.parentEntity is not None:
            collisionObj.parentEntity.active = False
        
        #move player away from mine collision
        self.position += collResult.normal * collResult.depth
        
        #bouncy
        self.velocity.Bounce(collResult.normal)

    
    def Update(self, frameTime):
        if self.active:
            self.velocity *= math.exp(-self.friction * frameTime)
            self.position += self.velocity * frameTime
            self.collisionObj.shape.position = self.position.Clone()