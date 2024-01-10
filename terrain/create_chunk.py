from ursina import *
from classes.block import Block

#Python file to create chunks used in world

blocks = [] #array to hold blocks

def create_chunk(chunk_size):

    for x in range(chunk_size):
        for y in range(chunk_size):
            for z in range(chunk_size):
                #new block/button
                block = Block(color=color.white, model='cube',  position=(x, y, z), texture='textures/grass.png', type='terrain')
                blocks.append(block)