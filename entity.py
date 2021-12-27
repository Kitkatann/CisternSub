class Entity:
    def __init__(self, entityType, x, y, active):
        self.entityType = entityType
        self.x = x
        self.y = y
        self.active = active
        self.collisionObj = None
        self.image = None
    


