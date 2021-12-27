from vector2D import Vector2D
import mathUtil

class Shape:
    def __init__(self, position):
        self.position = position.Clone()

class CollisionResult:
    def __init__(self, objA, objB, intersect, normal, depth):
        self.objA = objA
        self.objB = objB
        self.intersect = intersect
        self.normal = normal
        self.depth = depth

class Circle(Shape):
    def __init__(self, position, radius):
        super().__init__(position)
        self.radius = radius
    
    def Intersects(self, other):
        if isinstance(other, Circle):
            d = other.position - self.position
            dist = d.Length()
            if dist < self.radius + other.radius:                
                depth = self.radius + other.radius - dist
                normal = d.Clone()
                normal.Normalize()
                intersect = self.position + normal * (self.radius - depth)
                return CollisionResult(None, None, intersect, normal, depth)
        if isinstance(other, Rectangle):
           pass
        return None
        
class Rectangle(Shape): 
    def __init__(self, position, width, height):
        super().__init__(position)
        self.width = width
        self.height = height
    
    def ClosestPoint(self, point):
        x = point.x
        y = point.y
        px = self.position.x
        py = self.position.y
        qx = px + self.width
        qy = py + self.height
        return Vector2D(mathUtil.Clamp(x, px, qx), mathUtil.Clamp(y, py, qy))
        
    def Intersects(self, other):
        if isinstance(other, Circle):
            closest = self.ClosestPoint(other.position)
            dist = other.position.DistanceToPoint(closest)
            if dist < other.radius:
                depth = other.radius - dist
                normal = other.position - closest
                normal.Normalize()
                intersect = closest - normal * depth
                return CollisionResult(None, None, intersect, normal, depth)
        if isinstance(other, Rectangle):
            pass
        return None
            