from pyglet.gl import *
from player import Player
from vector2D import Vector2D
import tileTypeData
from tileType import TileType
from entityType import EntityType
import entityTypeData


tileTypeData.LoadTileTypes()
entityTypeData.LoadEntityTypes()

tileSize = 32

windowWidth = 0

player = Player(True, Vector2D(200, 200), Vector2D(0, 0), "RIGHT")
playerSpeed = 5.0

scale = 0

collisionRectangles = []
backgroundTiles = []
foregroundTiles = []

entities = []

gridWidth = 33
gridHeight = 24

screenWidth = gridWidth * tileSize
screenHeight = gridHeight * tileSize

