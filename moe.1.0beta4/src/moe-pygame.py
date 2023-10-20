#!/usr/bin/env python
# -*- coding: iso-8859-15 -*-
#
# Mines of Elderlore
# An Ascii roguelike with :
# * Permanent levels
# * Simple and easy gameplay
# * High scores that you can compare with others
# http://landsof.elderlore.com
#
# Released under the GNU General Public License
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA

"""
Mines of Elderlore Pygame
"""

import pygame
import os
import sys
import time
import pickle
import random
import Numeric as N
import moe
import rltile

###############################################################################
# Constants
###############################################################################
VERSION = "1.0 beta4"
PYGAME_COLOR = ((0, 0, 0),
                (0, 127, 255),
                (99, 175, 255),
                (51, 155, 0),
                (255, 190, 255),
                (230, 146, 150),
                (255, 255, 255),
                (252, 235, 95),
                (0, 0, 0),
                (0, 127, 255),
                (99, 175, 255),
                (51, 155, 0),
                (255, 190, 255),
                (230, 146, 150),
                (255, 255, 255),
                (252, 235, 95))
            
TILE_WALL = 0
TILE_FLOOR = 1
TILE_DOOR = 2
TILE_STAIRSUP = 3
TILE_STAIRSDOWN = 4
TILE_GROUNDS = (TILE_WALL, TILE_FLOOR, TILE_DOOR, TILE_STAIRSUP, 
                TILE_STAIRSDOWN)

surf_dungeon = pygame.image.load(os.path.join("data", "tiles", "dungeon.png"))
TILE_DUNGEON = [None]
TILE_DUNGEON_LIT = [None]
tile = pygame.Surface((32, 32))
for i in range(10): # 9 levels to go
    lit = []
    unlit = []
    for j in TILE_GROUNDS:
        tile.blit(surf_dungeon, (0, 0), (i*32, j*64, 32, 32))
        unlit.append(tile.copy())
        tile.blit(surf_dungeon, (0, 0), (i*32, j*64+32, 32, 32))
        lit.append(tile.copy())
    TILE_DUNGEON.append(unlit)
    TILE_DUNGEON_LIT.append(lit)

# Monster and number tiles
surf_tiles = pygame.image.load(os.path.join("data", "tiles", "tiles.png"))

TILE_MONSTER = []
TILE_NUMBER = []

for i in range(10):
    tile = pygame.Surface((32, 32), pygame.SRCALPHA, 32)
    tile.blit(surf_tiles, (0, 0), (i*32, 0, 32, 32))
    TILE_MONSTER.append(tile.copy())
    tile = pygame.Surface((32, 32), pygame.SRCALPHA, 32)
    tile.blit(surf_tiles, (0, 0), (i*32, 32, 32, 32))
    TILE_NUMBER.append(tile.copy())
# Weapon tiles
TILE_SWORD, TILE_AXE, TILE_SPEAR, TILE_WARHAMMER = [], [], [], []
for i in range(5):
    tile = pygame.Surface((32, 32), pygame.SRCALPHA, 32)
    tile.blit(surf_tiles, (0, 0), (i*32, 32*2, 32, 32))
    TILE_SWORD.append(tile.copy())
    tile = pygame.Surface((32, 32), pygame.SRCALPHA, 32)
    tile.blit(surf_tiles, (0, 0), ((i+5)*32, 32*2, 32, 32))
    TILE_AXE.append(tile.copy())
    tile = pygame.Surface((32, 32), pygame.SRCALPHA, 32)
    tile.blit(surf_tiles, (0, 0), (i*32, 32*3, 32, 32))
    TILE_SPEAR.append(tile.copy())
    tile = pygame.Surface((32, 32), pygame.SRCALPHA, 32)
    tile.blit(surf_tiles, (0, 0), ((i+5)*32, 32*3, 32, 32))
    TILE_WARHAMMER.append(tile.copy())
tile = pygame.Surface((32, 32), pygame.SRCALPHA, 32)
tile.blit(surf_tiles, (0, 0), (0, 32*4, 32, 32))
TILE_SWORD.append(tile.copy())
TILE_WEAPON = (TILE_SWORD, TILE_AXE, TILE_SPEAR, TILE_WARHAMMER)
# Other tiles
TILE_ZZ = pygame.Surface((32, 32), pygame.SRCALPHA, 32)
TILE_ZZ.blit(surf_tiles, (0, 0), (32, 32*4, 32, 32))
TILE_POTION = pygame.Surface((32, 32), pygame.SRCALPHA, 32)
TILE_POTION.blit(surf_tiles, (0, 0), (32*2, 32*4, 32, 32))
TILE_MUSHROOM = pygame.Surface((32, 32), pygame.SRCALPHA, 32)
TILE_MUSHROOM.blit(surf_tiles, (0, 0), (32*3, 32*4, 32, 32))
# Equipment constants
RL_CLOAK = (rltile.TUILEP_CAPE_BROWN,
            rltile.TUILEP_CAPE_RED,
            rltile.TUILEP_CAPE_BLUE,
            rltile.TUILEP_CAPE_MAGENTA,
            rltile.TUILEP_CAPE_WHITE,
            rltile.TUILEP_CAPE_GRAY,
            rltile.TUILEP_CAPE_GREEN,
            rltile.TUILEP_CAPE_CYAN,
            rltile.TUILEP_CAPE_YELLOW,
            rltile.TUILEP_CAPE_BLACK)
RL_BOOTS = (rltile.TUILEP_PIEDS_SHORT_BROWN,
            rltile.TUILEP_PIEDS_MIDDLE_BROWN,
            rltile.TUILEP_PIEDS_MIDDLE_GREEN,
            rltile.TUILEP_PIEDS_MESH_RED,
            rltile.TUILEP_PIEDS_MESH_BLUE,
            rltile.TUILEP_PIEDS_LONG_RED,
            rltile.TUILEP_PIEDS_MIDDLE_PURPLE,
            rltile.TUILEP_PIEDS_MIDDLE_GRAY,
            rltile.TUILEP_PIEDS_MIDDLE_GOLD,
            rltile.TUILEP_PIEDS_MESH_BLACK)
RL_HELMET = (None,
             rltile.TUILEP_TETE_FEATHER_YELLOW,
             rltile.TUILEP_TETE_IRON1,
             rltile.TUILEP_TETE_IRON2,
             rltile.TUILEP_TETE_IRON3,
             rltile.TUILEP_TETE_YELLOW_WING,
             rltile.TUILEP_TETE_HELM_GREEN,
             rltile.TUILEP_TETE_BROWN_GOLD,
             rltile.TUILEP_TETE_BLACK_HORN,
             rltile.TUILEP_TETE_ART_DRAGONHELM)
RL_GAUNTLETS = (rltile.TUILEP_BRAS_GLOVE_BROWN,
            rltile.TUILEP_BRAS_GLOVE_RED,
            rltile.TUILEP_BRAS_GLOVE_GRAY,
            rltile.TUILEP_BRAS_GLOVE_BLUE,
            rltile.TUILEP_BRAS_GLOVE_BLACK,
            rltile.TUILEP_BRAS_GLOVE_ORANGE,
            rltile.TUILEP_BRAS_GLOVE_PURPLE,
            rltile.TUILEP_BRAS_GLOVE_WHITE,
            rltile.TUILEP_BRAS_GLOVE_GOLD,
            rltile.TUILEP_BRAS_GLOVE_BLACK2)
RL_ARMOR = (rltile.TUILEP_TORSE_GIMLI,
            rltile.TUILEP_TORSE_ARAGORN,
            rltile.TUILEP_TORSE_LEATHER_HEAVY,
            rltile.TUILEP_TORSE_LEATHER_METAL,
            rltile.TUILEP_TORSE_CHAINMAIL,
            rltile.TUILEP_TORSE_SCALEMAIL,
            rltile.TUILEP_TORSE_HALF_PLATE,
            rltile.TUILEP_TORSE_CRYSTAL_PLATE,
            rltile.TUILEP_TORSE_DRAGONARM_GOLD,
            rltile.TUILEP_TORSE_PLATE_BLACK)
RL_SWORD = (rltile.TUILEP_MAIN_D_LONG_SWORD,
            rltile.TUILEP_MAIN_D_SABRE,
            rltile.TUILEP_MAIN_D_BLOODBANE,
            rltile.TUILEP_MAIN_D_JIHAD,
            rltile.TUILEP_MAIN_D_SINGING_SWORD,
            rltile.TUILEP_MAIN_D_SWORD_BREAKER)
RL_AXE = (rltile.TUILEP_MAIN_D_AXE_SMALL,
          rltile.TUILEP_MAIN_D_HAND_AXE,
          rltile.TUILEP_MAIN_D_AXE,
          rltile.TUILEP_MAIN_D_GREAT_AXE,
          rltile.TUILEP_MAIN_D_ARGA)
RL_SPEAR = (rltile.TUILEP_MAIN_D_QUARTERSTAFF1,
            rltile.TUILEP_MAIN_D_SPEAR2,
            rltile.TUILEP_MAIN_D_SPEAR5,
            rltile.TUILEP_MAIN_D_LANCE,
            rltile.TUILEP_MAIN_D_QUARTERSTAFF3)
RL_WARHAMMER = (rltile.TUILEP_MAIN_D_HAMMER2,
                rltile.TUILEP_MAIN_D_HAMMER,
                rltile.TUILEP_MAIN_D_MACE,
                rltile.TUILEP_MAIN_D_LARGE_MACE,
                rltile.TUILEP_MAIN_D_MORNINGSTAR2)
RL_WEAPON = (RL_SWORD, RL_AXE, RL_SPEAR, RL_WARHAMMER)      
        
###############################################################################
# Functions
###############################################################################

def Tab3(tab, color):
    """
    Build Numeric array of colors
    tab is a Numeric array
    color is a (a, b, c) tuple
    """
    tab3 = N.ones((tab.shape[0], tab.shape[1], 3))
    for i in range(3):
        tab3[:, :, i] = tab 
    return tab3 * color

def round_map(player):
    """
    Creates a map from a dungeon floor
    """
    # The mask of known positions
    tab = Tab3(player.known == 1, PYGAME_COLOR[moe.COLOR_WHITE])
    alpha = pygame.surfarray.make_surface(tab)
    alpha.set_colorkey(PYGAME_COLOR[moe.COLOR_WHITE])
    # The walls, floor and doors map 
    tab = Tab3(player.dungeon.special == moe.SPECIAL_DOOR, 
               PYGAME_COLOR[moe.COLOR_WHITE]) + \
               Tab3((player.dungeon.floor == moe.DUNGEON_FLOOR) & 
                    (player.dungeon.special <> moe.SPECIAL_DOOR), 
                    (127, 127, 127)) + \
               Tab3((player.dungeon.floor == moe.DUNGEON_WALL) & 
                    (player.dungeon.special <> moe.SPECIAL_DOOR), 
                    (64, 64, 64))
    floor = pygame.surfarray.make_surface(tab)
    floor.blit(alpha, (0, 0))
    # The special stuff map
    tab = Tab3(player.dungeon.special == moe.SPECIAL_UPSTAIRS, 
                    PYGAME_COLOR[moe.COLOR_YELLOW]) + \
               Tab3(player.dungeon.special == moe.SPECIAL_DOWNSTAIRS1, 
                    PYGAME_COLOR[moe.COLOR_RED]) + \
               Tab3(player.dungeon.special == moe.SPECIAL_DOWNSTAIRS2, 
                    PYGAME_COLOR[moe.COLOR_RED]) + \
               Tab3(player.dungeon.special == moe.SPECIAL_MUSHROOM, 
                    PYGAME_COLOR[moe.COLOR_MAGENTA]) + \
               Tab3(player.dungeon.special == moe.SPECIAL_POTION, 
                    PYGAME_COLOR[moe.COLOR_YELLOW]) + \
               Tab3(player.dungeon.special >= moe.SPECIAL_SWORD, 
                    PYGAME_COLOR[moe.COLOR_BLUE])
    special = pygame.surfarray.make_surface(tab)
    special.blit(alpha, (0, 0))
    special.set_colorkey((0, 0, 0))
    player_pos = pygame.Surface((1, 1))
    player_pos.fill(PYGAME_COLOR[moe.COLOR_GREEN])
    special.blit(player_pos, player.pos)
    # We blit all on map
    map = pygame.transform.scale2x(pygame.transform.scale2x(floor))
    map.blit(pygame.transform.scale2x(pygame.transform.scale2x(special)), 
             (0, 0))
    # Let's resize at the good shape
    return pygame.transform.scale(map, (224, 224))


def BorderText(font, text, coul, shift=1):
    """
    Return a surface of white text with black border
    """
    coul_text = (0, 0, 0)
    surf_name = font.render(text, True, coul_text)
    surf = pygame.Surface((surf_name.get_width() + 2 * shift + 1, 
                           surf_name.get_height() + 2 * shift + 1), 
                           pygame.SRCALPHA, 32)
    if shift >= 0:
        for i in range(0, 2 * shift + 1):
            for j in range(0, 2 * shift + 1):
                surf.blit(surf_name, (i, j))

    surf.blit(font.render(text, True, coul), (shift, shift))
    return surf

################################################################################
# Main class
################################################################################

class Game:
    def __init__(self):
        """
        Inits game
        """
        self._load_config()
        self.init_display()
        self.init_startscreen()
        self.clock = pygame.time.Clock()
        self.exit = False
        self.music_initiated = False
        
    def start(self):
        """
        Starts playing games
        """
        while not self.exit:
            self.init_player()
            self.init_menu()
            if not self.music_initiated:
                self.music_initiated = True
                self.init_sound()
                self.init_music()
                self.init_ambiance()
            self.display_menu()
        
    
    def _load_config(self):
        """
        Loads config from moe.ini file
        """
        self.conf_game, self.conf_movie, self.conf_curses, \
        self.conf_pygame = moe.load_config()
        mine_name, self.DUNGEON_WIDTH, self.DUNGEON_HEIGHT = self.conf_game
        if mine_name in ("Random", "random"):
            self.MINE_NAME = moe.MName().New()
        else:
            self.MINE_NAME = mine_name
        self.RECORD, self.replay_speed = self.conf_movie
        self.FONT_SIZE, self.PYGAME_DIRS, screenwidth, screenheight, \
        self.FULLSCREEN, self.PLAY_MUSIC = self.conf_pygame
        self.SCREEN_SIZE = (screenwidth, screenheight)
        self.COLS = 35
    
    def init_display(self):
        """
        Display init
        """        
        pygame.init()
        pygame.key.set_repeat(100)
        icon = TILE_MONSTER[-1]
        pygame.display.set_icon(icon)
        pygame.display.set_caption("Mines of Elderlore %s" % VERSION)
        self.font = pygame.font.Font(os.path.join("data", 'gui', 
                                                  "LiberationMono-Bold.ttf"), 
                                                  self.FONT_SIZE)
        if self.FULLSCREEN:
            self.screen = pygame.display.set_mode(self.SCREEN_SIZE, 
                                                  pygame.FULLSCREEN)
        else:
            self.screen = pygame.display.set_mode(self.SCREEN_SIZE)
        
        self.FONT_WIDTH = self.font.render(" ", True, (0, 0, 0)).get_width()
        
        self.background = pygame.Surface(self.SCREEN_SIZE)
        panel = pygame.image.load(os.path.join("data", 'gui', "SidePanel.png"))
        self.background.blit(panel, (self.SCREEN_SIZE[0]-256, 0))
        
        
    def init_startscreen(self):
        """
        Start screen init
        """
        startsurf = pygame.image.load(os.path.join('data', 'gui', 
                                                   'abstra_blue.png'))
        self.startscreen = pygame.transform.scale(startsurf, self.SCREEN_SIZE)
        title = pygame.image.load(os.path.join('data', 'gui', 'title.png'))
        self.startscreen.blit(title, ((self.SCREEN_SIZE[0] - 
                                       title.get_width()) / 2, 0))
        version = BorderText(self.font, _("v%s") % VERSION, 
                             PYGAME_COLOR[moe.COLOR_CYAN], 2)
        self.startscreen.blit(version, 
                              (self.SCREEN_SIZE[0] - version.get_width(), 
                               self.SCREEN_SIZE[1] - version.get_height()))
        self.screen.blit(self.startscreen, (0, 0))
        pygame.display.flip()
        
        
    def init_sound(self):
        """
        Sounds init
        """
        posl = (530, 300)
        #pygame.mixer.init()#22050, -16, 2, 4*1024)
        pygame.mixer.quit()
        pygame.mixer.init(44100, -16, 1, 4096)
        
        pygame.mixer.set_reserved(3)
        
        self._nb_lines = 0
        
        self.screen.blit(BorderText(self.font, _("Loading sounds"), 
                                    PYGAME_COLOR[moe.COLOR_BLUE], 2), 
                        (posl[0],posl[1] + self._nb_lines * self.FONT_SIZE))
        self._nb_lines += 1
        
        self.PYGAME_SOUND = {}
        self.PYGAME_SOUND[moe.CHANNEL_SOUNDS] = pygame.mixer.Channel(0)
        self.PYGAME_SOUND[moe.SOUND_PLAYER_ATTACK] = \
        pygame.mixer.Sound(os.path.join("data", "sound", "attack.ogg"))
        self.PYGAME_SOUND[moe.SOUND_PLAYER_KILL] = \
        pygame.mixer.Sound(os.path.join("data", "sound", "kill.ogg"))
        self.PYGAME_SOUND[moe.SOUND_MONSTER_ATTACK] = \
        pygame.mixer.Sound(os.path.join("data", "sound", "monster_attack.ogg"))
        self.PYGAME_SOUND[moe.SOUND_MONSTER_KILL] = \
        pygame.mixer.Sound(os.path.join("data", "sound", "monster_kill.ogg"))
        self.PYGAME_SOUND[moe.SOUND_OPEN_DOOR] = \
        pygame.mixer.Sound(os.path.join("data", "sound", "open_door.ogg"))
        self.PYGAME_SOUND[moe.SOUND_GRAB_STUFF] = \
        pygame.mixer.Sound(os.path.join("data", "sound", "receive.ogg"))
        self.PYGAME_SOUND[moe.SOUND_DRINK] = \
        pygame.mixer.Sound(os.path.join("data", "sound", "drink.ogg"))
        self.PYGAME_SOUND[moe.SOUND_REST] = \
        pygame.mixer.Sound(os.path.join("data", "sound", "chimes.ogg"))
        self.PYGAME_SOUND[moe.SOUND_PLAYER_LEVELUP] = \
        pygame.mixer.Sound(os.path.join("data", "sound", "levelup.ogg"))
        self.PYGAME_SOUND[moe.SOUND_MONSTER_LEVELUP] = \
        pygame.mixer.Sound(os.path.join("data", "sound", "levelup.ogg"))
        self.PYGAME_SOUND[moe.SOUND_MONSTER_SUMMON] = \
        pygame.mixer.Sound(os.path.join("data", "sound", "summon.ogg"))
        
        self.screen.blit(BorderText(self.font, _("Sounds loaded!"), 
                                    PYGAME_COLOR[moe.COLOR_WHITE], 2), 
                         (posl[0], posl[1] + self._nb_lines * self.FONT_SIZE))
        pygame.display.flip()
        self._nb_lines += 2
        
        
    def init_music(self):
        """
        Music init
        """
        posl = (530, 300)
        
        self.music_channel = pygame.mixer.Channel(1)
        self.music_channel.set_volume(0.8)
        self.PYGAME_MUSIC = []
            
        if self.PLAY_MUSIC:
            self.screen.blit(BorderText(self.font, _("Loading music"), 
                              PYGAME_COLOR[moe.COLOR_BLUE], 2), 
                   (posl[0], posl[1]+self._nb_lines * self.FONT_SIZE))
            pygame.display.flip()
            self._nb_lines += 1
            n = 0   
            for music in os.listdir(os.path.join("data", "music")):
                self.screen.blit(BorderText(self.font, _("."), 
                                  PYGAME_COLOR[moe.COLOR_WHITE], 2), 
                                  (posl[0] + n * self.FONT_WIDTH, posl[1] + self._nb_lines * self.FONT_SIZE))
                pygame.display.flip()
                n += 1
                self.PYGAME_MUSIC.append(pygame.mixer.Sound(os.path.join("data", "music", 
                                                                    music)))
            self.screen.blit(BorderText(self.font, _(" Music loaded!"), 
                                    PYGAME_COLOR[moe.COLOR_WHITE], 2), 
                            (posl[0] + n * self.FONT_WIDTH, posl[1] + self._nb_lines * self.FONT_SIZE))
            pygame.display.flip()
            self._nb_lines += 1
            
        
    def init_ambiance(self):
        """
        Ambiance init
        """
        posl = (530, 300)
        self._nb_lines += 1
        self.screen.blit(BorderText(self.font, _("Loading ambiance sounds"), 
                          PYGAME_COLOR[moe.COLOR_BLUE], 2), 
                          (posl[0], posl[1] + self._nb_lines * self.FONT_SIZE))
        pygame.display.flip()
        self._nb_lines += 1
            
        self.ambiance_channel = pygame.mixer.Channel(2)
        self.ambiance_channel.set_volume(0.5)
        self.PYGAME_AMBIANCE = []
        n = 0
        for ambiance in os.listdir(os.path.join("data", "ambiance")):
            self.screen.blit(BorderText(self.font, _("."), PYGAME_COLOR[moe.COLOR_WHITE], 2), 
                            (posl[0] + n * self.FONT_WIDTH, posl[1] + self._nb_lines * self.FONT_SIZE))
            pygame.display.flip()
            n += 1
            self.PYGAME_AMBIANCE.append(pygame.mixer.Sound(os.path.join("data", 
                                                                   "ambiance", 
                                                                   ambiance)))
        self.screen.blit(BorderText(self.font, _(" Ambiance sounds loaded!"), 
                                    PYGAME_COLOR[moe.COLOR_WHITE], 2), 
                            (posl[0] + n * self.FONT_WIDTH, posl[1] + self._nb_lines * self.FONT_SIZE))
        pygame.display.flip()
        self._nb_lines += 1
        
            
    def init_menu(self):
        """
        Menu init
        """
        posl = (20, 300)
        
        if self.replay:
            self.button_start_on = pygame.image.load(os.path.join('data', 'gui', 'playmovie_on.png'))
            self.button_start_off = pygame.image.load(os.path.join('data', 'gui', 'playmovie_off.png'))
        elif self.player.round == 0:
            self.button_start_on = pygame.image.load(os.path.join('data', 'gui', 'newgame_on.png'))
            self.button_start_off = pygame.image.load(os.path.join('data', 'gui', 'newgame_off.png'))
        else:
            self.button_start_on = pygame.image.load(os.path.join('data', 'gui', 'continuegame_on.png'))
            self.button_start_off = pygame.image.load(os.path.join('data', 'gui', 'continuegame_off.png'))
        self.button_exit_on = pygame.image.load(os.path.join('data', 'gui', 'exit_on.png'))
        self.button_exit_off = pygame.image.load(os.path.join('data', 'gui', 'exit_off.png'))
        self.x1_butt = (self.SCREEN_SIZE[0] - self.button_start_on.get_width()) / 2
        self.y1_butt = self.SCREEN_SIZE[1] - 175
        self.x2_butt = (self.SCREEN_SIZE[0] - self.button_exit_on.get_width()) / 2
        self.y2_butt = self.SCREEN_SIZE[1] - 90
        self.button_backgrnd1 = pygame.Surface(self.button_start_on.get_size())
        self.button_backgrnd1.blit(self.startscreen, (0, 0), (self.x1_butt, self.y1_butt,
                                                         self.button_start_on.get_width(),
                                                         self.button_start_on.get_height()))
        self.button_backgrnd2 = pygame.Surface(self.button_exit_on.get_size())
        self.button_backgrnd2.blit(self.startscreen, (0, 0), (self.x2_butt, self.y2_butt,
                                                         self.button_exit_on.get_width(),
                                                         self.button_exit_on.get_height()))
        
        self.screen.blit(self.startscreen, (0, 0))
        self.screen.blit(BorderText(self.font, _("%s ranks :") % self.player.dname_full, 
                    PYGAME_COLOR[moe.COLOR_RED], 2), 
                   (posl[0], posl[1] + 0 * self.FONT_SIZE))
        if self.player.scores.has_key(self.player.dname_full):
            nbl = min(10, (self.SCREEN_SIZE[1] - 500) / self.FONT_SIZE)
            l = min(nbl, len(self.player.scores[self.player.dname_full]))
            for i in range(l):
                self.screen.blit(BorderText(self.font, _("%03d : %s") % \
                        (i+1, self.player.scores[self.player.dname_full][i][1]), 
                        PYGAME_COLOR[moe.COLOR_WHITE], 2), 
                        (posl[0], posl[1] + (2+i) * self.FONT_SIZE))   
        
        self._blit_button(self.button_start_off, 1)
        self._blit_button(self.button_exit_off, 2)
        
        pygame.display.flip()
        
        
    def _blit_button(self, surf, n=1, m=2):
        """
        Blits button n among m to the menu screen
        """
        x = (self.SCREEN_SIZE[0] - surf.get_width()) / 2
        y = self.SCREEN_SIZE[1] - 90 - 85 * (m - n)
        self.screen.blit(surf, (x, y))
        
        
    def display_menu(self):
        """
        Menu display
        """
        exit = False
        pos_mouse = 0
        while not exit:
            events = pygame.event.get()
            
            for event in events:
                
                if event.type == pygame.QUIT \
                    or (event.type == pygame.KEYDOWN and \
                        event.key == pygame.K_ESCAPE):
                    self.exit = True
                    exit = True
                
                elif event.type == pygame.MOUSEMOTION:
                    pos = pygame.mouse.get_pos()
                    if self.x1_butt + self.button_start_on.get_width() > pos[0] > self.x1_butt \
                    and self.y1_butt + self.button_start_on.get_height() > pos[1] > self.y1_butt:
                        if pos_mouse <> 1:
                            #self.screen.blit(self.startscreen, (0, 0))
                            self._blit_button(self.button_backgrnd1, 1)
                            self._blit_button(self.button_start_on, 1)
                            self._blit_button(self.button_backgrnd2, 2)
                            self._blit_button(self.button_exit_off, 2)
                            pygame.display.flip()
                            pos_mouse = 1
                    elif self.x2_butt + self.button_exit_on.get_width() > pos[0] > self.x2_butt \
                    and self.y2_butt + self.button_exit_on.get_height() > pos[1] > self.y2_butt:
                        if pos_mouse <> 2:
                            #self.screen.blit(self.startscreen, (0, 0))
                            self._blit_button(self.button_backgrnd1, 1)
                            self._blit_button(self.button_start_off, 1)
                            self._blit_button(self.button_backgrnd2, 2)
                            self._blit_button(self.button_exit_on, 2)
                            pygame.display.flip()
                            pos_mouse = 2
                    else:
                        if pos_mouse <> 0:
                            pos_mouse = 0
                            #self.screen.blit(self.startscreen, (0, 0))
                            self._blit_button(self.button_backgrnd1, 1)
                            self._blit_button(self.button_start_off, 1)
                            self._blit_button(self.button_backgrnd2, 2)
                            self._blit_button(self.button_exit_off, 2)
                            pygame.display.flip()
                        
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if pos_mouse == 1:
                        self.play()
                        exit = True
                    elif pos_mouse ==2:
                        self.exit = True
                        exit = True
                        
    def init_player(self):
        """
        Load player
        """
        if len(sys.argv) == 2:
            ########################################################################
            # Load movie
            ########################################################################
            if os.path.isfile(sys.argv[1]):
                print _("Load movie %s...") % sys.argv[1]
                pkl_file = open(sys.argv[1], 'rb')
                desc = pickle.load(pkl_file)
                size = pickle.load(pkl_file)
                name = pickle.load(pkl_file)
                self.history = pickle.load(pkl_file)
                seed = pickle.load(pkl_file)
                known_dungeon = pickle.load(pkl_file)
                pkl_file.close()
                self.replay = True
                self.player = moe.Player(size, seed.pop(0), name, self.COLS, {}, 
                                    known_dungeon)
                
            else:
                print _("Error : no movie file '%s' found.") % sys.argv[1]
                print _("List of available movies :")
                print _("--------------------------")
                if not os.path.isdir('movies'):
                    os.mkdir('movies')
                for moviename in os.listdir('movies'):
                    print "Filename : %s" % moviename
                    pkl_file = open(os.path.join('movies', moviename), 'rb')
                    desc = pickle.load(pkl_file)
                    size = pickle.load(pkl_file)
                    name = pickle.load(pkl_file)
                    pkl_file.close()
                    print _("Dungeon : %s (%s x %s)") % (name, size[0], size[1])
                    print desc
                    print "--------------------------"                    
                sys.exit(0)
                
        else:
            ########################################################################
            # Player init
            ########################################################################
            self.replay = False
            seed = time.time()
            if os.path.isfile('moe.sav'):
                pkl_file = open('moe.sav', 'rb')
                self.player = pickle.load(pkl_file)
                pkl_file.close()
                if self.player.exit == 0:
                    # the game continues
                    print _("Game loaded...")
                    self.player.update_seed(seed)
                else:
                    # Let's start with a new player
                    print _("New game initiated in the mines of %s...") % self.MINE_NAME
                    self.player = moe.Player((self.DUNGEON_WIDTH, 
                                              self.DUNGEON_HEIGHT), 
                                              seed, 
                                              self.MINE_NAME, 
                                              self.COLS, 
                                              self.player.scores, 
                                              self.player.known_dungeon, 
                                              self.RECORD)
            else:
                print _("No save file yet")
                self.player = moe.Player((self.DUNGEON_WIDTH, 
                                          self.DUNGEON_HEIGHT), 
                                          seed, 
                                          self.MINE_NAME, 
                                          self.COLS, 
                                          {}, 
                                          {}, 
                                          self.RECORD)
                  
        if self.replay:
            self.player.add_message(_("Playing movie file '%s'.") % desc, moe.COLOR_CYAN)
        else:
            if self.player.round == 0:
                self.player.add_message(_("You enter the mines of %s.") % self.player.dname, 
                                   moe.COLOR_WHITE)
                self.player.add_message(_("Hit 'h' anytime for in-game help."), 
                                   moe.COLOR_CYAN)
                self.player.add_message(_("Good luck!"), moe.COLOR_WHITE)

        # Player tile
        self.tp = rltile.Tuile_Perso()
        self.basetile_player = rltile.bodytile(self.tp, rltile.TUILEP_CORPS_HUMAN_M, 
                                         rltile.TUILEP_JAMBES_PANTS_BLACK,
                                         rltile.TUILEP_CHEVEUX_SHORT_BLACK,
                                         -1, True)
        self.tile_player = rltile.playertile(self.tp, self.basetile_player,
                                        RL_CLOAK[self.player.level-1],
                                        RL_BOOTS[self.player.level-1],
                                        None,
                                        RL_GAUNTLETS[self.player.level-1],
                                        RL_ARMOR[self.player.level-1],
                                        RL_WEAPON[self.player.active_weapon]\
                                        [self.player.weapon_flavor[self.player.active_weapon]],
                                        None)
        
        
    def _blit_map(self):
        """
        Blits a map from a dungeon floor to the screen
        """
        # The mask of known positions
        tab = Tab3(self.player.known == 1, PYGAME_COLOR[moe.COLOR_WHITE])
        alpha = pygame.surfarray.make_surface(N.array(tab))
        alpha.set_colorkey(PYGAME_COLOR[moe.COLOR_WHITE])
        # The walls, floor and doors map 
        tab = Tab3(self.player.dungeon.special == moe.SPECIAL_DOOR, 
                   PYGAME_COLOR[moe.COLOR_WHITE]) + \
                   Tab3((self.player.dungeon.floor == moe.DUNGEON_FLOOR) & 
                        (self.player.dungeon.special <> moe.SPECIAL_DOOR), 
                        (127, 127, 127)) + \
                   Tab3((self.player.dungeon.floor == moe.DUNGEON_WALL) & 
                        (self.player.dungeon.special <> moe.SPECIAL_DOOR), 
                        (64, 64, 64))
        floor = pygame.surfarray.make_surface(tab)
        floor.blit(alpha, (0, 0))
        # The special stuff map
        tab = Tab3(self.player.dungeon.special == moe.SPECIAL_UPSTAIRS, 
                        PYGAME_COLOR[moe.COLOR_YELLOW]) + \
                   Tab3(self.player.dungeon.special == moe.SPECIAL_DOWNSTAIRS1, 
                        PYGAME_COLOR[moe.COLOR_RED]) + \
                   Tab3(self.player.dungeon.special == moe.SPECIAL_DOWNSTAIRS2, 
                        PYGAME_COLOR[moe.COLOR_RED]) + \
                   Tab3(self.player.dungeon.special == moe.SPECIAL_MUSHROOM, 
                        PYGAME_COLOR[moe.COLOR_MAGENTA]) + \
                   Tab3(self.player.dungeon.special == moe.SPECIAL_POTION, 
                        PYGAME_COLOR[moe.COLOR_YELLOW]) + \
                   Tab3(self.player.dungeon.special >= moe.SPECIAL_SWORD, 
                        PYGAME_COLOR[moe.COLOR_BLUE])
        special = pygame.surfarray.make_surface(tab)
        special.blit(alpha, (0, 0))
        special.set_colorkey((0, 0, 0))
        player_pos = pygame.Surface((1, 1))
        player_pos.fill(PYGAME_COLOR[moe.COLOR_GREEN])
        special.blit(player_pos, self.player.pos)
        # We blit all on map
        floor.blit(special, (0, 0))
        # Let's resize at the good shape
        self.screen.blit(pygame.transform.scale(floor, (224, 224)), 
                         (self.SCREEN_SIZE[0] - 256 + 16, 16))
        
    def _blit_info(self):
        """
        Blits the info bar on the screen
        """
        info = _("Lvl   | HP    /    | XP     /     for lvl    | !   |") \
               + _(" *   |     | M    /   /   ")
        self.screen.blit(BorderText(self.font, info, PYGAME_COLOR[moe.COLOR_WHITE], 2), (0, 0))
                                
        self.screen.blit(BorderText(self.font, "%d" % self.player.deepness, 
                          PYGAME_COLOR[moe.COLOR_WHITE], 2), (4 * self.FONT_WIDTH, 0))
        if self.player.hp < self.player.hpmax / 3:
            color_hp = PYGAME_COLOR[moe.COLOR_RED]
        elif self.player.hp < 2 * self.player.hpmax / 3:
            color_hp = PYGAME_COLOR[moe.COLOR_YELLOW]                               
        else:
            color_hp = PYGAME_COLOR[moe.COLOR_WHITE]
        self.screen.blit(BorderText(self.font, "%03d" % self.player.hp, color_hp, 2), (11 * self.FONT_WIDTH, 0))
        self.screen.blit(BorderText(self.font, "%03d" % self.player.hpmax, 
                          PYGAME_COLOR[moe.COLOR_WHITE], 2), (15 * self.FONT_WIDTH, 0))
        self.screen.blit(BorderText(self.font, "%04d" % self.player.xp, 
                          PYGAME_COLOR[moe.COLOR_WHITE], 2), (24 * self.FONT_WIDTH, 0))
        self.screen.blit(BorderText(self.font, "%04d" % self.player.levels[self.player.level], 
                          PYGAME_COLOR[moe.COLOR_WHITE], 2), (29 * self.FONT_WIDTH, 0))
        self.screen.blit(BorderText(self.font, "%02d" % (self.player.level+1), 
                          PYGAME_COLOR[moe.COLOR_WHITE], 2), (42 * self.FONT_WIDTH, 0))
        self.screen.blit(BorderText(self.font, "%02d" % self.player.potion, 
                          PYGAME_COLOR[moe.COLOR_WHITE], 2), (48 * self.FONT_WIDTH, 0))
        self.screen.blit(BorderText(self.font, "%02d" % self.player.mushroom, 
                          PYGAME_COLOR[moe.COLOR_WHITE], 2), (54 * self.FONT_WIDTH, 0))
        self.screen.blit(BorderText(self.font, "%03d" % self.player.round, 
                          PYGAME_COLOR[moe.COLOR_WHITE], 2), (59 * self.FONT_WIDTH, 0))
        if self.player.mood < self.player.mood_level[1]:
            color_mood = PYGAME_COLOR[moe.COLOR_WHITE]
        elif self.player.mood < self.player.mood_level[2]:
            color_mood = PYGAME_COLOR[moe.COLOR_YELLOW]
        else:
            color_mood = PYGAME_COLOR[moe.COLOR_MAGENTA]
        self.screen.blit(BorderText(self.font, "%03d" % self.player.mood, color_mood, 2), (67 * self.FONT_WIDTH, 0))
        self.screen.blit(BorderText(self.font, "%03d" % self.player.mood_level[1], 
                          PYGAME_COLOR[moe.COLOR_WHITE], 2), (71 * self.FONT_WIDTH, 0))
        self.screen.blit(BorderText(self.font, "%03d" % self.player.mood_level[2], 
                          PYGAME_COLOR[moe.COLOR_WHITE], 2), (75 * self.FONT_WIDTH, 0))
    
    def _blit_tile(self, posp, poss):
        """
        Blits the according tile 
        s : pygame screen
        player : the player object
        posp : pos of the tile for the player
        poss : pos of the tile on the screen
        """
        if self.player.known[posp]:                            
                                
            if self.player.seen[posp]:
                if self.player.dungeon.floor[posp] == moe.DUNGEON_WALL:
                    self.screen.blit(TILE_DUNGEON_LIT[self.player.deepness][TILE_WALL], poss)
                    
                else:
                    if self.player.dungeon.has_special(posp, moe.SPECIAL_UPSTAIRS):
                        self.screen.blit(TILE_DUNGEON_LIT[self.player.deepness][TILE_STAIRSUP], 
                               poss)
                    
                    elif self.player.dungeon.has_special(posp, moe.SPECIAL_DOWNSTAIRS1) \
                       or self.player.dungeon.has_special(posp, moe.SPECIAL_DOWNSTAIRS2):
                        self.screen.blit(TILE_DUNGEON_LIT[self.player.deepness][TILE_STAIRSDOWN], 
                               poss)
                        
                    elif self.player.dungeon.has_special(posp, moe.SPECIAL_DOOR):
                        self.screen.blit(TILE_DUNGEON_LIT[self.player.deepness][TILE_DOOR], poss)
                    
                    else:
                        self.screen.blit(TILE_DUNGEON_LIT[self.player.deepness][TILE_FLOOR], poss)
                    
                    if self.player.dungeon.has_special(posp, moe.SPECIAL_MUSHROOM):
                        self.screen.blit(TILE_MUSHROOM, poss)
                        self.player.add_mushroom_seen(posp)            
                        
                    if self.player.dungeon.has_special(posp, moe.SPECIAL_POTION):
                        self.screen.blit(TILE_POTION, poss) 
                    
                    if self.player.dungeon.monster.has_key(posp):
                        # Display a monster
                        lvl = self.player.dungeon.monster[posp].level
                        self.screen.blit(TILE_MONSTER[lvl-1], poss)
                        if self.player.dungeon.monster[posp].is_awake() and lvl < 10:
                            self.screen.blit(TILE_NUMBER[lvl], poss)
                        else:
                            self.screen.blit(TILE_ZZ, poss)
                        self.player.dungeon.monster[posp].awake()                                
                    
            else:
                if self.player.dungeon.floor[posp] == moe.DUNGEON_WALL:
                    self.screen.blit(TILE_DUNGEON[self.player.deepness][TILE_WALL], poss)
                    
                elif self.player.dungeon.has_special(posp, moe.SPECIAL_UPSTAIRS):
                    self.screen.blit(TILE_DUNGEON[self.player.deepness][TILE_STAIRSUP], poss)
                    
                elif self.player.dungeon.has_special(posp, moe.SPECIAL_DOWNSTAIRS1) or \
                     self.player.dungeon.has_special(posp, moe.SPECIAL_DOWNSTAIRS2):
                    self.screen.blit(TILE_DUNGEON[self.player.deepness][TILE_STAIRSDOWN], poss)
                    
                elif self.player.dungeon.has_special(posp, moe.SPECIAL_DOOR):
                    self.screen.blit(TILE_DUNGEON[self.player.deepness][TILE_DOOR], poss)    
                    
                else:
                    self.screen.blit(TILE_DUNGEON[self.player.deepness][TILE_FLOOR], poss)
                    
            if self.player.dungeon.special[posp] >= moe.SPECIAL_SWORD:
                # Display a weapon
                weap_flav, weap_type = self.player.dungeon.weapon_params(posp)
                self.screen.blit(TILE_WEAPON[weap_type][weap_flav], poss)
                self.screen.blit(TILE_NUMBER[weap_flav], poss)
                
            if posp[0] == self.player.pos[0] and posp[1] == self.player.pos[1]:
                self.screen.blit(self.tile_player, poss)
    
    def _blit_messages(self):
        """
        Blits player messages to the screen
        """
        nb = min((self.SCREEN_SIZE[1] - 320) / self.FONT_SIZE, len(self.player.message))
        for i in range(nb):
            col_mess = self.player.message[nb-i-1][1]
            if col_mess > 7:
                shift = 2
            else:
                shift = 1
            self.screen.blit(BorderText(self.font, self.player.message[nb-i-1][0], 
                              PYGAME_COLOR[col_mess], shift), 
                              (self.SCREEN_SIZE[0]-250, 300 + i * self.FONT_SIZE))
        
    def display_game(self):
        """
        Display the dungeon floor on the given curses
        """
        # Blit the background
        self.screen.blit(self.background, (0, 0))
        center = ((self.SCREEN_SIZE[0] - 250) / 64, self.SCREEN_SIZE[1] / 64)
        # Blit tiles
        for y in range(self.SCREEN_SIZE[1] / 32):
            yy = self.player.pos[1] + y - center[1]
            if 0 <= yy < self.player.dsize[1]:
                for x in range((self.SCREEN_SIZE[0] - 250) / 32):
                    xx = self.player.pos[0] + x - center[0]
                    if 0 <= xx < self.player.dsize[0]:
                        self._blit_tile((xx, yy), (x * 32, y * 32))
        # Blit the info bar                             
        self._blit_info()
        # Blit the messages
        self._blit_messages()
        # Blit the map
        self._blit_map()
        # Updates the screen   
        pygame.display.flip()
    
    def _deal_event(self, event):
        """
        Deal an event, on keyboard or in the keymovie
        """
        if event.type == pygame.QUIT:
            return True
        
        elif event.type == pygame.KEYDOWN:
            k = event.key
            self.player.record_history(k)
            keysPressed = pygame.key.get_pressed()
            round = False
            
            if k == pygame.K_ESCAPE:
                return True
                
            elif keysPressed[pygame.K_RETURN] and \
                    (keysPressed[pygame.K_RALT] or 
                     keysPressed[pygame.K_LALT]):
                pygame.display.toggle_fullscreen()
            
            elif self.PYGAME_DIRS.has_key(k):
                old_pos = (self.player.pos[0], self.player.pos[1])
                new_pos = (self.player.pos[0] + self.PYGAME_DIRS[k][0], 
                           self.player.pos[1] + self.PYGAME_DIRS[k][1])
                round = self.player.move(new_pos, 1, self.PYGAME_SOUND)
                if round:
                    self.player.update_dir(old_pos)
                self.player.do_fov(self.player.fov)
                
            elif k == pygame.K_d:
                # Drink a health potion
                round = self.player.drink(self.PYGAME_SOUND)
        
            elif k == pygame.K_r:
                # Rest and eat mushrooms
                round = self.player.rest(sound=self.PYGAME_SOUND)
                
            elif k == pygame.K_e:
                # Eat one mushroom
                round = self.player.rest(1, sound=self.PYGAME_SOUND)
                
            elif k == pygame.K_1 or k == pygame.K_KP1:
                round = self.player.change_active_weapon(moe.SPECIAL_SWORD)
                
            elif k == pygame.K_2 or k == pygame.K_KP2:
                round = self.player.change_active_weapon(moe.SPECIAL_AXE)
                
            elif k == pygame.K_3 or k == pygame.K_KP3:
                round = self.player.change_active_weapon(moe.SPECIAL_SPEAR)
                
            elif k == pygame.K_4 or k == pygame.K_KP4:
                round = self.player.change_active_weapon(moe.SPECIAL_WARHAMMER)
                
            else:
                if k == pygame.K_i:    
                    self.player.inventory()
                    
                elif k == pygame.K_h:
                    self.player.help()       
                                 
                elif k == pygame.K_F2:
                    self.player.help_f2()
                    
                elif k == pygame.K_F3:
                    self.player.help_f3()
                    
                elif k == pygame.K_F4:
                    self.player.help_f4()
            
            self.tile_player = rltile.playertile(self.tp, self.basetile_player,
                        RL_CLOAK[self.player.level-1],
                        RL_BOOTS[self.player.level-1],
                        None,
                        RL_GAUNTLETS[self.player.level-1],
                        RL_ARMOR[self.player.level-1],
                        RL_WEAPON[self.player.active_weapon]\
                        [self.player.weapon_flavor[self.player.active_weapon]],
                        None)
                    
            if round:
                self.player.increase_round()
                self.player.move_monsters(self.PYGAME_SOUND)
                     
            self.display_game()
            
            if self.player.exit:
                return True
            
        return False
    
    def play(self):
        """
        Plays a new game or continue an already started game
        """
        self.player.do_fov(self.player.fov)
        self.display_game()
        ########################################################################
        # Main loop
        ########################################################################
        exit = False
        while not exit:
            # Flag to count actions that cost a round and others that do not
            round = False
            
            if not self.replay:
                events = pygame.event.get()
            else:
                events = [self.history.pop(0)]
            
            for event in events:
                exit = self._deal_event(event)
            
            self.clock.tick(40)
            
            if self.player.event <> moe.EVENT_NONE:
                if self.music_channel.get_busy() or self.ambiance_channel.get_busy():
                    pygame.mixer.fadeout(1000)
                if len(self.PYGAME_MUSIC) > 0:
                    self.music_channel.queue(random.choice(self.PYGAME_MUSIC))
                self.player.init_event(moe.EVENT_NONE)
                
            elif random.randint(1, 400) == 1:
                if self.music_channel.get_busy() or self.ambiance_channel.get_busy():
                    pygame.mixer.fadeout(10000)
                else:
                    self.ambiance_channel.queue(random.choice(self.PYGAME_AMBIANCE))
        
        self.save()
        if self.player.exit:
            self.init_player()
            self.init_menu()
                        
    def save(self):
        """
        Exits game
        """
        # Pygame ending
        if self.player.exit:
            if self.player.exit == 1:
                self.player.add_message(self.player.last_word(), moe.COLOR_MAGENTA)            
            self.player.add_message(_("Press ESC to end the game."),
                                    moe.COLOR_WHITE | moe.COLOR_BOLD)
            self.display_game()
            exit = False
            while not exit:
                events = pygame.event.get()
                for event in events:          
                    if event.type == pygame.QUIT \
                    or (event.type == pygame.KEYDOWN and \
                        event.key == pygame.K_ESCAPE):
                        exit = True
        if not self.replay:
            if self.player.exit > 0:
                print _("Saving score...")
                self.player.save_score()
            else:
                self.player.add_message(_("Game saved."),
                                        moe.COLOR_WHITE | moe.COLOR_BOLD)
            self.player.save()
            #self.display_game()
        
        
################################################################################
# Main part
################################################################################

if __name__ == "__main__":
    
    try:
        import psyco
        psyco.full()
    except ImportError:
        pass
    
    game = Game()
    game.start()
    
    
                    