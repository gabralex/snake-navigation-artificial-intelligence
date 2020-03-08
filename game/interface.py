####################################################################################################################################
# Snake game agent navigation via the use of artificial intelligence
#
# Copyright (C) 2019 Project contributors
#
# This program is free software: you can redistribute it and/or modify it under the terms of the GNU Affero General Public License
# as published by the Free Software Foundation, either version 3 of the License, or any later version.
#
# This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License along with this program. If not, see
# <http://www.gnu.org/licenses/>.

####################################################################################################################################
from pyglet.gl import *
import pyglet
from math import floor
from pyglet.window import key

from game.constant import WorldElement


def vec(*args):
    return (GLfloat * len(args))(*args)


####################################################################################################################################
INTERFACE_WIDTH = 1600
INTERFACE_HEIGHT = 900
SEPARATION_WIDTH = 2
INTERFACE_ORIGIN = 0

WORLD_ELEMENT_WIDTH = 109
WORLD_ELEMENT_HEIGHT = 37

WORLD_ELEMENT_INTERFACE_SIZE = 10

COLOUR_WHITE = vec(1.0, 1.0, 1.0, 1.0)

EMPTY_WORLD_ELEMENT_COLOUR_A = vec(0.01, 0.05, 0.1, 1.0)
EMPTY_WORLD_ELEMENT_COLOUR_B = vec(0.01, 0.1, 0.05, 1.0)


####################################################################################################################################
colour_mapping = {WorldElement.AGENT_HEAD: vec(0.0, 0.6, 0.5, 1.0),
                  WorldElement.AGENT_TAIL: vec(0.0, 0.5, 0.5, 1.0),
                  WorldElement.OBSTACLE: vec(0.55, 0.27, 0.08, 1.0)}

test_world = {(1, 1): WorldElement.OBSTACLE,
              (0, 0): WorldElement.AGENT_HEAD,
              (-1, 3): WorldElement.AGENT_TAIL,
              (-5, -1): WorldElement.OBSTACLE,
              (-1, -1): WorldElement.OBSTACLE}


####################################################################################################################################
class UserInterface(pyglet.window.Window):
    current_x = 0
    current_y = 0

    def __init__(self):
        configuration = Config(sample_buffers=1,
                               samples=16,
                               depth_size=16,
                               double_buffer=True)
        self.init__ = super(UserInterface, self).__init__(config=configuration,
                                                          resizable=False,
                                                          width=INTERFACE_WIDTH,
                                                          height=INTERFACE_HEIGHT)

    def on_resize(self, width, height):
        glEnable(GL_MULTISAMPLE)
        glEnable(GL_LINE_SMOOTH)
        glViewport(INTERFACE_ORIGIN, INTERFACE_ORIGIN, width, height)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        glOrtho(INTERFACE_ORIGIN, width, height, INTERFACE_ORIGIN, -1.0, 1.0)

        return pyglet.event.EVENT_HANDLED

    def on_draw(self):
        _clear_all()
        self.drawWorldSection()
        self.drawAgentSection()

        # glScalef(-1.0, 1.0, 1.0)
        text = pyglet.text.Label("Test", font_name='arial', font_size=12, x=1350,
                                      y=100, anchor_y='top', width=1000, multiline=True)
        text.draw()

    def on_key_press(self, symbol, modifiers):
        test_world[(self.current_x, self.current_y)] = WorldElement.AGENT_TAIL
        if symbol == key.UP:
            self.current_x += 1
        elif symbol == key.DOWN:
            self.current_x += -1
        elif symbol == key.LEFT:
            self.current_y -= -1
        elif symbol == key.RIGHT:
            self.current_y += -1

        test_world[(self.current_x, self.current_y)] = WorldElement.AGENT_HEAD

    def drawWorldSection(self):
        _draw_border(INTERFACE_ORIGIN, INTERFACE_ORIGIN, 1298, 450, SEPARATION_WIDTH)
        # _draw_border(ORIGIN_HEIGHT, 1302, section_bottom, INTERFACE_WIDTH, SEPARATION_WIDTH)
        interface_offset = INTERFACE_ORIGIN + (SEPARATION_WIDTH * 2)
        _draw_elements(test_world, interface_offset, interface_offset, 0, 0)

    def drawAgentSection(self):
        # section_top = (INTERFACE_HEIGHT / 2) + (SEPARATION_WIDTH / 2)
        # _draw_border(section_top, ORIGIN_WIDTH, INTERFACE_HEIGHT, 1298, SEPARATION_WIDTH)
        # _draw_border(section_top, 1302, INTERFACE_HEIGHT, INTERFACE_WIDTH, SEPARATION_WIDTH)
        self.drawAgentElement()

    @staticmethod
    def draw_world_element():
        # glColor4fv(COLOUR_OTHER)
        glBegin(GL_QUADS)
        element_top = SEPARATION_WIDTH + SEPARATION_WIDTH
        element_left = SEPARATION_WIDTH + SEPARATION_WIDTH
        # element_offset = ELEMENT_SIZE + SEPARATION_WIDTH

        # for x in range(0, 108):
        #     for y in range(0, 41):
                # glVertex2d(element_left + (x * element_offset), INTERFACE_HEIGHT - (element_top + (y * element_offset)))
                # glVertex2d(element_left + ELEMENT_SIZE + (x * element_offset), INTERFACE_HEIGHT - (element_top + (y * element_offset)))
                # glVertex2d(element_left + ELEMENT_SIZE + (x * element_offset), INTERFACE_HEIGHT - (element_top + ELEMENT_SIZE + (y * element_offset)))
                # glVertex2d(element_left + (x * element_offset), INTERFACE_HEIGHT - (element_top + ELEMENT_SIZE + (y * element_offset)))

        glEnd()

    def drawAgentElement(self):
        # glColor4fv(COLOUR_MORE)
        glBegin(GL_QUADS)

        # for x in range(0, 106):
        #     for y in range(0, 36):
                # glVertex2d(4 + (x * 12), INTERFACE_HEIGHT - (455 + (y * 12)))
                # glVertex2d(14 + (x * 12), INTERFACE_HEIGHT - (455 + (y * 12)))
                # glVertex2d(14 + (x * 12), INTERFACE_HEIGHT - (465 + (y * 12)))
                # glVertex2d(4 + (x * 12), INTERFACE_HEIGHT - (465 + (y * 12)))

        glEnd()

    def show(self):
        pyglet.app.run()


####################################################################################################################################
def _clear_all():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT | GL_ACCUM_BUFFER_BIT | GL_STENCIL_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    # glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)


def _draw_border(interface_x_offset, interface_y_offset, width, height, thickness):
    glColor4fv(COLOUR_WHITE)

    glBegin(GL_QUADS)

    glVertex2f(interface_x_offset, interface_y_offset)
    glVertex2f(interface_x_offset, interface_y_offset + thickness)
    glVertex2f(interface_x_offset + width, interface_y_offset + thickness)
    glVertex2f(interface_x_offset + width, interface_y_offset)

    glVertex2f(interface_x_offset, interface_y_offset + height - thickness)
    glVertex2f(interface_x_offset, interface_y_offset + height)
    glVertex2f(interface_x_offset + width, interface_y_offset + height)
    glVertex2f(interface_x_offset + width, interface_y_offset + height - thickness)

    glVertex2f(interface_x_offset, interface_y_offset + thickness)
    glVertex2f(interface_x_offset, interface_y_offset + height - thickness)
    glVertex2f(interface_x_offset + thickness, interface_y_offset + height - thickness)
    glVertex2f(interface_x_offset + thickness, interface_y_offset + thickness)

    glVertex2f(interface_x_offset + width - thickness, interface_y_offset + thickness)
    glVertex2f(interface_x_offset + width - thickness, interface_y_offset + height - thickness)
    glVertex2f(interface_x_offset + width, interface_y_offset + height - thickness)
    glVertex2f(interface_x_offset + width, interface_y_offset + thickness)

    glEnd()


def _draw_elements(elements, interface_x_offset, interface_y_offset, world_x_offset, world_y_offset):
    offset = WORLD_ELEMENT_INTERFACE_SIZE + SEPARATION_WIDTH
    size = WORLD_ELEMENT_INTERFACE_SIZE

    xx = floor((WORLD_ELEMENT_WIDTH - 1) / 2)
    x_range = range(xx * -1, xx)
    yy = floor((WORLD_ELEMENT_HEIGHT - 1) / 2)
    y_range = range(yy * -1, yy)

    glBegin(GL_QUADS)

    for x in range(0, WORLD_ELEMENT_WIDTH):
        for y in range(0, WORLD_ELEMENT_HEIGHT):
            element_x = x - xx + world_x_offset
            element_y = y - yy + world_y_offset
            if (element_x, element_y) in elements:
                glColor4fv(colour_mapping[elements[(element_x, element_y)]])
            elif (x + y) % 2 == 0:
                glColor4fv(EMPTY_WORLD_ELEMENT_COLOUR_A)
            else:
                glColor4fv(EMPTY_WORLD_ELEMENT_COLOUR_B)

            glVertex2d(interface_x_offset + (x * offset), interface_y_offset + (y * offset))
            glVertex2d(interface_x_offset + (x * offset), interface_y_offset + size + (y * offset))
            glVertex2d(interface_x_offset + size + (x * offset), interface_y_offset + size + (y * offset))
            glVertex2d(interface_x_offset + size + (x * offset), interface_y_offset + (y * offset))

    glEnd()
