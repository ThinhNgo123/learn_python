from math import *
import OpenGL.GL as gl
import OpenGL.GLU as glu 
import pygame, sys, random
from pygame.math import Vector3, Vector2

def color_random():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

def convert_sphere_to_decac(radius, radian_phi, radian_theta):
    x = radius * cos(radian_phi) * sin(radian_theta)
    y = radius * sin(radian_phi)
    z = radius * cos(radian_phi) * cos(radian_theta)
    return Vector3(x, y, z)

def draw_sphere(center: Vector3, radius, vertical_divide: int, horizontal_divide: int):
    if vertical_divide < 2 or horizontal_divide < 2:
        return
    phi_step = pi / vertical_divide
    theta_step = (2 * pi) / horizontal_divide
    phi1 = pi / 2

    gl.glBegin(gl.GL_TRIANGLE_FAN)
    gl.glVertex3f(center.x, center.y + radius, center.z)
    for h_part in range(horizontal_divide):
        # print("part", h_part)
        gl.glColor3d(*color_random())
        vector1 = convert_sphere_to_decac(radius, phi1 - phi_step, h_part * theta_step) + center
        vector2 = convert_sphere_to_decac(radius, phi1 - phi_step, (h_part + 1) * theta_step) + center
        gl.glVertex3f(vector1.x, vector1.y, vector1.z)
        gl.glVertex3f(vector2.x, vector2.y, vector2.z)
    gl.glEnd()
    
    for v_part in range(vertical_divide - 2):
        phi1 -= phi_step
        phi2 = phi1 - phi_step
        gl.glBegin(gl.GL_QUAD_STRIP)
        for h_part in range(horizontal_divide + 1):
            gl.glColor3d(*color_random())
            vector1 = convert_sphere_to_decac(radius, phi1, theta_step * h_part) + center
            vector2 = convert_sphere_to_decac(radius, phi2, theta_step * h_part) + center
            # print(vector1, vector2, center)
            gl.glVertex3f(vector1.x, vector1.y, vector1.z)
            gl.glVertex3f(vector2.x, vector2.y, vector2.z)
        gl.glEnd()

    gl.glBegin(gl.GL_TRIANGLE_FAN)
    gl.glVertex3f(center.x, center.y - radius, center.z)
    for h_part in range(horizontal_divide):
        # print("part", h_part)
        gl.glColor3d(*color_random())
        vector1 = convert_sphere_to_decac(radius, phi1 - phi_step, h_part * theta_step) + center
        vector2 = convert_sphere_to_decac(radius, phi1 - phi_step, (h_part + 1) * theta_step) + center
        gl.glVertex3f(vector1.x, vector1.y, vector1.z)
        gl.glVertex3f(vector2.x, vector2.y, vector2.z)
    gl.glEnd()

win = pygame.display.set_mode((500, 500), flags=pygame.DOUBLEBUF | pygame.OPENGL)
width = win.get_width()
height = win.get_height()

clock = pygame.time.Clock()
fps = 30
running = True

#setup gl
gl.glFrontFace(gl.GL_CCW)
gl.glEnable(gl.GL_CULL_FACE)
# gl.glCullFace(gl.GL_BACK)
gl.glEnable(gl.GL_DEPTH_TEST)
# gl.glClearColor(255, 255, 255, 255)
gl.glClear(gl.GL_COLOR_BUFFER_BIT | gl.GL_DEPTH_BUFFER_BIT)
# gl.glPolygonMode(gl.GL_FRONT, gl.GL_LINE)
gl.glPolygonMode(gl.GL_FRONT_AND_BACK, gl.GL_FILL)
gl.glMatrixMode(gl.GL_MODELVIEW)
gl.glLoadIdentity()
gl.glOrtho(-width / 2, width / 2, -height / 2, height / 2, -width / 2, width / 2)
glu.gluLookAt(1.5, 1.5, 1.5, 0, 0, 0, 0, 1, 0)
# draw_sphere(Vector3(0, 0, 0), 200, 40, 40)
# gl.glLineWidth()
angle = 0
while running:
    for event in pygame.event.get():
        if (event.type == pygame.QUIT) or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            running = False

    gl.glClear(gl.GL_COLOR_BUFFER_BIT | gl.GL_DEPTH_BUFFER_BIT)
    # gl.glRotated(angle, 0, 1, 0)
    draw_sphere(Vector3(0, 0, 0), 200, 40, 40)
    # glu.gluLookAt(1.5, y, 1.5, 0, 0, 0, 0, 1, 0)
    # angle += 0.02

    pygame.display.set_caption(f"FPS: {clock.get_fps()}")
    pygame.display.flip()
    clock.tick(fps)
    # pygame.time.wait(500)
pygame.quit
sys.exit() 