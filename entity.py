class Entity:
    def __init__(self, entityType, x, y, active):
        self.entityType = entityType
        self.x = x
        self.y = y
        self.active = active
        self.collisionObj = None
        self.image = None
        
        #exit attributes
        self.exitScreen = None
        self.exitDirection = None
        
    def SetAttributes(self, attributes):
        if self.entityType.name == "exit":
            self.exitScreen = attributes.split()[0] + "Data"
            self.exitDirection = attributes.split()[1]
            if self.exitDirection == "up":
                self.collisionObj.shape.position.y += 32
            if self.exitDirection == "right":
                self.collisionObj.shape.position.x += 32
            if self.exitDirection == "down":
                self.collisionObj.shape.position.y -= 32
            if self.exitDirection == "left":
                self.collisionObj.shape.position.x -= 32

