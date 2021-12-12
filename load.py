from pyglet.gl import *
import levelData
from collisionRectangle import CollisionRectangle
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
    
    levelData.collisionRectangles.clear()
    levelData.backgroundTiles.clear()
    levelData.foregroundTiles.clear()
    levelData.entities.clear()
    
    print("Loading data for level: " + currentScreen)
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
                pos = Vector2D(int(entityData[2]), int(entityData[3]))
                if entityTypeName == "exit":
                    levelData.collisionRectangles.append(CollisionRectangle(pos, levelData.tileSize, levelData.tileSize, "exit"))
                    levelData.collisionRectangles[len(levelData.collisionRectangles) - 1].SetAttributes(attributes)
                if entityTypeName == "playerStart":
                    #an entity of type playerStart should only be added if gameStart hasn't been set to true yet
                    if not gameStart:
                        levelData.player.position = pos
                        gameStart = True
                levelData.entities.append(Entity(entityType, pos.x, pos.y, False, attributes))
        else:
            cellIndex = 0
            if currentCommand == "bgTiles":
                for word in line.split():
                    #line format: <tileID> <tileID> <tileID> etc.
                    pos = Vector2D(cellIndex % levelData.gridWidth, cellIndex // levelData.gridWidth)
                    pos *= scale
                    if (int(word)) != 0:
                        image = tileTypeData.GetTileTypeByID(int(word)).image
                        levelData.collisionRectangles.append(CollisionRectangle(pos, levelData.tileSize, levelData.tileSize, "water"))
                        levelData.backgroundTiles.append(VisualRectangle(pos, image))
                    cellIndex += 1
            if currentCommand == "fgTiles":
                for word in line.split():
                    #line format: <tileID> <tileID> <tileID> etc.
                    pos = Vector2D(cellIndex % levelData.gridWidth, cellIndex // levelData.gridWidth)
                    pos *= scale
                    if (int(word)) != 0:
                        image = tileTypeData.GetTileTypeByID(int(word)).image
                        levelData.collisionRectangles.append(CollisionRectangle(pos, levelData.tileSize, levelData.tileSize, "water"))
                        levelData.foregroundTiles.append(VisualRectangle(pos, image))
                    cellIndex += 1
            if currentCommand == "wallTiles":
                for word in line.split():
                    #line format: <tileID> <tileID> <tileID> etc.
                    pos = Vector2D(cellIndex % levelData.gridWidth, cellIndex // levelData.gridWidth)
                    pos *= scale
                    if (int(word)) != 0:
                        image = tileTypeData.GetTileTypeByID(int(word)).image
                        levelData.collisionRectangles.append(CollisionRectangle(pos, levelData.tileSize, levelData.tileSize, "wall"))
                        levelData.backgroundTiles.append(VisualRectangle(pos, image))
                    cellIndex += 1
                currentCommand = ""
    f.close()