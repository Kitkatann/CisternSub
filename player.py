import math
from vector2D import Vector2D
import load
import levelData

class Player:
    def __init__(self, active, position, velocity, rotation):
        self.active = active
        #position is center point
        self.position = position.Clone()
        self.velocity = velocity
        self.rotation = rotation
        self.friction = 1.0
        self.hitboxRadius = 20
        self.width = 64
        self.height = 35

    def Collide(self, collisionObj, closestPoint):
        if collisionObj.collisionType == "wall":
            self.CollideWithWall(closestPoint)
        if collisionObj.collisionType == "exit":
            self.CollideWithExit(collisionObj)
    
    def CollideWithWall(self, closestPoint):
        a = closestPoint - self.position
        dLen = self.hitboxRadius + 0.1 - a.Length()
        a.Normalize()
        d = a * dLen
        self.position -= d
        #bouncy
        self.velocity -= d * 100
    
    def CollideWithExit(self, collisionObj):
        print(collisionObj.exitScreen + " " + collisionObj.exitDirection)
        load.LoadLevelData(collisionObj.exitScreen)
        if collisionObj.exitDirection == "up":
            self.position.y -= levelData.screenHeight
        elif collisionObj.exitDirection == "right":
            self.position.x -= levelData.screenWidth
        elif collisionObj.exitDirection == "down":
            self.position.y += levelData.screenHeight
        elif collisionObj.exitDirection == "left":
            print("here")
            self.position.x += levelData.screenWidth
        
    
    def Update(self, frameTime):
        if self.active:
            self.velocity *= math.exp(-self.friction * frameTime)
            self.position += self.velocity * frameTime