from pyglet.gl import *
import levelData
from collisionObject import CollisionObject
from shapes import Rectangle
from shapes import Circle
from visualRectangle import VisualRectangle
from entity import Entity
from vector2D import Vector2D
import tileTypeData
from tileType import TileType
from entityType import EntityType
import entityTypeData

currentScreen = ""
gameStart = False

def LoadLevelData(screen):
    global gameStart
    
    currentScreen = screen
    
    levelData.collisionObjects.clear()
    levelData.backgroundTiles.clear()
    levelData.foregroundTiles.clear()
    levelData.entities.clear()
    
    scale = levelData.windowWidth / levelData.gridWidth
    
    currentCommand = ""

    keywords = ["bgTiles", "fgTiles", "wallTiles", "entity"]
    
    f = open("data/" + currentScreen + ".txt", "r")
    for line in f:
        pos = None
        image = None
        
        if line.split()[0] in keywords:
            #if line describes background tiles
            if line.split()[0] == "bgTiles":
                for word in line.split():
                    #line format: bgTiles <width> <height>
                    currentCommand = "bgTiles"
            #if line describes foreground tiles
            elif line.split()[0] == "fgTiles":
                for word in line.split():
                    #line format: fgTiles <width> <height>
                    currentCommand = "fgTiles"
            #if line describes wall tiles
            elif line.split()[0] == "wallTiles":
                for word in line.split():
                    #line format: wallTiles <width> <height>
                    currentCommand = "wallTiles"
            #if line describes entity
            if line.split()[0] == "entity":
                entityData = []
                for word in line.split():
                    #line format: <entity> <entityTypeID> <x> <y> <attributes>
                    currentCommand = "entity"
                    entityData.append(word)
                attributes = ""
                if len(entityData) > 4:
                    attributes = " ".join(entityData[4:])
                entityType = entityTypeData.GetEntityTypeByID(int(entityData[1]))
                entityTypeName = entityType.name
                pos = Vector2D(float(entityData[2]), float(entityData[3]))
                if entityTypeName == "exit":
                    levelData.collisionObjects.append(CollisionObject(Rectangle(pos, levelData.tileSize, levelData.tileSize), "exit"))
                    levelData.collisionObjects[len(levelData.collisionObjects) - 1].SetAttributes(attributes)
                if entityTypeName == "playerStart":
                    #only set player's starting position if gameStart hasn't been set to true yet
                    if not gameStart:
                        levelData.player.position = pos
                        gameStart = True
                if entityTypeName == "mine":
                    mineEntity = (Entity(entityType, pos.x, pos.y, True))
                    mineEntity.image = entityType.image
                    mineCollObj = CollisionObject(Circle(pos, 32), "mine")
                    mineCollObj.parentEntity = mineEntity
                    mineEntity.collisionObj = mineCollObj
                    levelData.entities.append(mineEntity)
        else:
            cellIndex = 0
            if currentCommand == "bgTiles":
                for word in line.split():
                    #line format: <tileID> <tileID> <tileID> etc.
                    pos = Vector2D(cellIndex % levelData.gridWidth, cellIndex // levelData.gridWidth)
                    pos *= scale
                    if (int(word)) != 0:
                        image = tileTypeData.GetTileTypeByID(int(word)).image
                        levelData.backgroundTiles.append(VisualRectangle(pos, image))
                    cellIndex += 1
            if currentCommand == "fgTiles":
                for word in line.split():
                    #line format: <tileID> <tileID> <tileID> etc.
                    pos = Vector2D(cellIndex % levelData.gridWidth, cellIndex // levelData.gridWidth)
                    pos *= scale
                    if (int(word)) != 0:
                        image = tileTypeData.GetTileTypeByID(int(word)).image
                        levelData.foregroundTiles.append(VisualRectangle(pos, image))
                    cellIndex += 1
            if currentCommand == "wallTiles":
                for word in line.split():
                    #line format: <tileID> <tileID> <tileID> etc.
                    pos = Vector2D(cellIndex % levelData.gridWidth, cellIndex // levelData.gridWidth)
                    pos *= scale
                    if (int(word)) != 0:
                        image = tileTypeData.GetTileTypeByID(int(word)).image
                        levelData.collisionObjects.append(CollisionObject(Rectangle(pos, levelData.tileSize, levelData.tileSize), "wall"))
                        levelData.foregroundTiles.append(VisualRectangle(pos, image))
                    cellIndex += 1
                currentCommand = ""
    f.close()