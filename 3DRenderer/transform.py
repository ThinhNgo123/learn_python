import numpy as np
import math

def translate(x, y, z):
    return np.array([
        [1, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 1, 0],
        [x, y, z, 1]
    ])

def scale(x, y, z):
    return np.array(
        [[x, 0, 0, 0],
        [0, y, 0, 0],
        [0, 0, z, 0],
        [0, 0, 0, 1]])

def rotateX(radian):
    return np.array([
        [1, 0, 0, 0],
        [0, math.cos(radian), math.sin(radian), 0],
        [0, -math.sin(radian), math.cos(radian), 0],
        [0, 0, 0, 1]
    ])

def rotateY(radian):
    return np.array([
        [math.cos(radian), 0, -math.sin(radian), 0],
        [0, 1, 0, 0],
        [math.sin(radian), 0, math.cos(radian), 0],
        [0, 0, 0, 1]
    ])

def rotateZ(radian):
    return np.array([
        [math.cos(radian), math.sin(radian), 0, 0],
        [-math.sin(radian), math.cos(radian), 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1]
    ]) 