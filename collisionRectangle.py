import math
import mathUtil
from vector2D import Vector2D

class CollisionRectangle:
    def __init__(self, position, width, height, collisionType):
        #position is bottom left point
        self.position = position.Clone()
        self.width = width
        self.height = height
        self.collisionType = collisionType
        self.exitScreen = None
        self.exitDirection = None
    
    def SetAttributes(self, attributes):
        if self.collisionType == "exit":
            print(attributes)
            self.exitScreen = attributes.split()[0] + "Data"
            self.exitDirection = attributes.split()[1]
            if self.exitDirection == "up":
                self.position.y += 32
            if self.exitDirection == "right":
                self.position.x += 32
            if self.exitDirection == "down":
                self.position.y -= 32
            if self.exitDirection == "left":
                self.position.x -= 32
    
    def ClosestPoint(self, point):
        x = point.x
        y = point.y
        px = self.position.x
        py = self.position.y
        qx = px + self.width
        qy = py + self.height
        return Vector2D(mathUtil.Clamp(x, px, qx), mathUtil.Clamp(y, py, qy))
    
    
        
    def PlayerCollisionUpdate(self, player):
        closest = self.ClosestPoint(player.position)
        dist = player.position.DistanceToPoint(closest)
        if (dist < player.hitboxRadius):
            player.Collide(self, closest)
        