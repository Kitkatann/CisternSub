import pyglet
from pyglet import image
from pyglet.window import key
from pyglet.gl import *
from pyglet import clock
from pyglet.media import StaticSource
from vector2D import Vector2D
import imageUtil
import levelData
import load





window = pyglet.window.Window(levelData.screenWidth, levelData.screenHeight)

levelData.windowWidth = window.get_size()[0]


#enable alpha blending
glEnable(GL_BLEND)
glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

keysDown = {"UP" : False, "RIGHT" : False, "DOWN" : False, "LEFT" : False}

def LoadSound(filename):
    return StaticSource(pyglet.media.load(filename))

#load error tile image
errorImage = imageUtil.LoadImage('images/errorImage.png', False)


#player images
playerImageMap = {"RIGHT": imageUtil.LoadImage('images/playerRight.png', False),
                    "LEFT": imageUtil.LoadImage('images/playerLeft.png', False)}
                    
#background image
background = imageUtil.LoadImage('images/background.png', False)

#load sounds


#load level
load.LoadLevelData("screen1Data")

@window.event
def on_draw():
    window.clear()
    
    glMatrixMode(GL_PROJECTION)
    glPushMatrix()
    
    #draw background
    imageUtil.DrawImage(background, 0, 0)
    
    #draw background level tiles
    for i in levelData.backgroundTiles:
        imageUtil.DrawImage(i.image, i.position.x, i.position.y)
    
    #draw player
    if levelData.player.active == True:
        imageUtil.DrawImage(playerImageMap[levelData.player.rotation], levelData.player.position.x - levelData.player.width / 2, levelData.player.position.y - levelData.player.height / 2)
    
    #draw foreground level tiles
    for i in levelData.foregroundTiles:
        imageUtil.DrawImage(i.image, i.position.x, i.position.y)
        
    #draw entities
    for entity in levelData.entities:
        if entity.image is not None:
            imageUtil.DrawImage(entity.image, entity.x, entity.y)
    
    glMatrixMode(GL_PROJECTION)
    glPopMatrix()
    
@window.event
def on_key_press(symbol, modifiers):
    if symbol == key.UP:
        keysDown["UP"] = True
    elif symbol == key.RIGHT:
        levelData.player.rotation = "RIGHT"
        keysDown["RIGHT"] = True
    elif symbol == key.LEFT:
        levelData.player.rotation = "LEFT"
        keysDown["LEFT"] = True
    elif symbol == key.DOWN:
        keysDown["DOWN"] = True
    

@window.event
def on_key_release(symbol, modifiers):
    if symbol == key.UP:
        keysDown["UP"] = False
    elif symbol == key.RIGHT:
        keysDown["RIGHT"] = False
    elif symbol == key.LEFT:
        keysDown["LEFT"] = False
    elif symbol == key.DOWN:
        keysDown["DOWN"] = False

playerCollisionResults = []

def Update(dt):
    targetVel = Vector2D(0, 0)
    if keysDown["UP"]:
        targetVel.y += levelData.playerSpeed
    if keysDown["RIGHT"]:
        targetVel.x += levelData.playerSpeed
    if keysDown["DOWN"]:
        targetVel.y -= levelData.playerSpeed
    if keysDown["LEFT"]:
        targetVel.x -= levelData.playerSpeed
    
    levelData.player.velocity += targetVel
    
    playerCollisionResults.clear()
    #store all active collision contacts in list
    for c in levelData.collisionObjects:
        c.GenerateContact(levelData.player.collisionObj, playerCollisionResults)
    for e in levelData.entities:
        if e.active and e.collisionObj is not None:
            e.collisionObj.GenerateContact(levelData.player.collisionObj, playerCollisionResults)
    
    #find the collision result with the largest depth
    largestDepth = 0.0
    largestDepthItem = None
    for r in playerCollisionResults:
        if r.depth > largestDepth:
            largestDepth = r.depth
            largestDepthItem = r
    
    #call player's collide method on collision result with largest depth
    if largestDepthItem is not None:
        levelData.player.Collide(largestDepthItem)
    
    #delete inactive entities
    levelData.entities = [e for e in levelData.entities if e.active]
            
    #update player
    if levelData.player.active:
        levelData.player.Update(dt)
        

pyglet.clock.schedule_interval(Update, 1/60.0)
pyglet.app.run()