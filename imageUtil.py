import pyglet
from pyglet import image
from pyglet.gl import *

def LoadImage(filename):
    im = image.load(filename)
    texture = im.get_texture()
    glEnable(texture.target)
    glBindTexture(texture.target, texture.id)
    glTexParameteri(texture.target, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
    return im

def DrawImage(image, x, y):
    image.blit(x, y)

def DisplayText(text, x, y, fontSize):
    label = pyglet.text.Label(text,
                    font_name='Times New Roman',
                    font_size=fontSize,
                    color=(255,255,255,255),
                    x=x, y=y,
                    anchor_x='center', anchor_y='center')
    label.draw()