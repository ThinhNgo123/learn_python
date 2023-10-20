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
Mines of Elderlore
"""

import random
import time
import Numeric as N
import ConfigParser
import pickle
import os
import sys
import locale
import gettext

gettext.install('moe')

###############################################################################
# Constants
###############################################################################
# from http://www.geocities.com/anvrill/names/cc_goth.html
PLACES = ['Adara', 'Adena', 'Adrianne', 'Alarice', 'Alvita', 'Amara', 'Ambika',
           'Antonia', 'Araceli', 'Balandria', 'Basha', 'Beryl', 'Bryn', 
           'Callia', 'Caryssa', 'Cassandra', 'Casondrah', 'Chatha', 'Ciara', 
           'Cynara', 'Cytheria', 'Dabria', 'Darcei', 'Deandra', 'Deirdre', 
           'Delores', 'Desdomna', 'Devi', 'Dominique', 'Drucilla', 'Duvessa', 
           'Ebony', 'Fantine', 'Fuscienne', 'Gabi', 'Gallia', 'Hanna', 'Hedda',
           'Jerica', 'Jetta', 'Joby', 'Kacila', 'Kagami', 'Kala', 'Kallie', 
           'Keelia', 'Kerry', 'Kerry-Ann', 'Kimberly', 'Killian', 'Kory', 
           'Lilith', 'Lucretia', 'Lysha', 'Mercedes', 'Mia', 'Maura', 'Perdita',
           'Quella', 'Riona', 'Safiya', 'Salina', 'Severin', 'Sidonia', 
           'Sirena', 'Solita', 'Tempest', 'Thea', 'Treva', 'Trista', 'Vala', 
           'Winta']

# Multipliers for transforming coordinates to other octants:
MULT = [[1,  0,  0, -1, -1,  0,  0,  1],
        [0,  1, -1,  0,  0, -1,  1,  0],
        [0,  1,  1,  0,  0, -1, -1,  0],
        [1,  0,  0,  1, -1,  0,  0, -1]]

# Directions
DIRS8 = [(-1,0), (-1,-1), (0,-1), (1,-1), (1,0), (1,1), (0,1), (-1,1)]
DIRS = [(-1,0), (0,-1), (1,0), (0,1)]

# Colors
COLOR_BLACK = 0
COLOR_BLUE = 1
COLOR_CYAN = 2
COLOR_GREEN = 3
COLOR_MAGENTA = 4
COLOR_RED = 5
COLOR_WHITE = 6
COLOR_YELLOW = 7

COLOR_BOLD = 8

# Special items on the floor
SPECIAL_NONE        = 0
SPECIAL_DOOR        = 1
SPECIAL_UPSTAIRS    = 2
SPECIAL_DOWNSTAIRS1 = 3
SPECIAL_DOWNSTAIRS2 = 4
SPECIAL_MUSHROOM    = 5
SPECIAL_POTION      = 6
SPECIAL_SWORD       = 10
SPECIAL_AXE         = 20
SPECIAL_SPEAR       = 30
SPECIAL_WARHAMMER   = 40

DUNGEON_FLOOR       = 0
DUNGEON_WALL        = 1

# Weapon constants
WEAPON_SWORD        = 0
WEAPON_AXE          = 1
WEAPON_SPEAR        = 2
WEAPON_WARHAMMER    = 3

WEAPON_NONE         = -1
WEAPON_FLAVOR0      = 0
WEAPON_FLAVOR1      = 1
WEAPON_FLAVOR2      = 2
WEAPON_FLAVOR3      = 3
WEAPON_FLAVOR4      = 4
WEAPON_FLAVOR5      = 5

WEAPON_NAME = (_("sword"), _("axe"), _("spear"), _("warhammer"))
WEAPON_TILE = ("/", "P", "|", "T")
WEAPON_FLAVOR = (_("training"), _("iron"), _("steel"), _("mithril"), 
                 _("adamantite"), _("vorpal"))

# Mood constants
MOOD_QUIET          = 0
MOOD_FRENZY         = 1
MOOD_BERZERK        = 2

# Mood triggers
TRIGGER_SUFFER      = 0
TRIGGER_KILL        = 1
TRIGGER_REST        = 2
TRIGGER_HEAL        = 3
TRIGGERS = (5, 10, -2, -40)

# Monster names
MONSTER = (_("Homunculus"), 
           _("Imp"),
           _("Lesser Demon"),
           _("Demon"),
           _("Greater Demon"),
           _("Lesser Balrog"),
           _("Balrog"),
           _("Greater Balrog"),
           _("Balrog captain"),
           _("Gothmog, lord of balrogs"))

# Sound channels
CHANNEL_SOUNDS = 0

# Sounds
SOUND_PLAYER_ATTACK = 11
SOUND_PLAYER_KILL = 12
SOUND_MONSTER_ATTACK = 13
SOUND_MONSTER_KILL = 14
SOUND_OPEN_DOOR = 15
SOUND_GRAB_STUFF = 16
SOUND_DRINK = 17
SOUND_REST = 18
SOUND_PLAYER_LEVELUP = 19
SOUND_MONSTER_LEVELUP = 20
SOUND_MONSTER_SUMMON = 21

# Events
EVENT_NONE = 0
EVENT_LEVELUP = 1
EVENT_STAIRSDOWN = 2
EVENT_STAIRSUP = 3
EVENT_BERZERK = 4
EVENT_DEATH = 5
EVENT_START = 6


###############################################################################
# Markov Name model
# A random name generator, by Peter Corbett
# http://www.pick.ucam.org/~ptc24/mchain.html
# This script is hereby entered into the public domain
###############################################################################
class Mdict:
    def __init__(self):
        self.d = {}
    def __getitem__(self, key):
        if self.d.has_key(key):
            return self.d[key]
        else:
            raise KeyError(key)
    def add_key(self, prefix, suffix):
        if self.d.has_key(prefix):
            self.d[prefix].append(suffix)
        else:
            self.d[prefix] = [suffix]
    def get_suffix(self,prefix):
        l = self[prefix]
        return random.choice(l)

class MName:
    """
    A name from a Markov chain
    """
    def __init__(self, chainlen = 2):
        """
        Building the dictionary
        """
        if chainlen > 10 or chainlen < 1:
            print "Chain length must be between 1 and 10, inclusive"
            sys.exit(0)
    
        self.mcd = Mdict()
        oldnames = []
        self.chainlen = chainlen
    
        for l in PLACES:
            l = l.strip()
            oldnames.append(l)
            s = " " * chainlen + l
            for n in range(0,len(l)):
                self.mcd.add_key(s[n:n+chainlen], s[n+chainlen])
            self.mcd.add_key(s[len(l):len(l)+chainlen], "\n")
    
    def New(self):
        """
        New name from the Markov chain
        """
        prefix = " " * self.chainlen
        name = ""
        suffix = ""
        while True:
            suffix = self.mcd.get_suffix(prefix)
            if suffix == "\n" or len(name) > 9:
                break
            else:
                name = name + suffix
                prefix = prefix[1:] + suffix
        return name.capitalize()
    
###############################################################################
# Monster class
###############################################################################

class Monster:
    ASLEEP = 0
    AWAKEN = 1
    def __init__(self, pos, level):
        self.pos = pos
        self.level_start = level
        self.level = level
            
        if self.level < 10:
            self.levelmax = min(level + level-1, 9)
            while random.randint(1, 5) == 1 and self.level < self.levelmax:
                self.level +=1
            #self.level = min(self.level, 9)
            self.hp = 1 + self.level * (self.level + 1)
            self.state = Monster.ASLEEP
        else:
            self.levelmax = 10
            self.hp = 150
            self.state = Monster.AWAKEN
            
        self.hpmax = self.hp
            
        
    def name(self):
        """
        the true name of the monster
        """
        if self.level_start < 10:
            return "%s the %s" % (self.tile(), MONSTER[self.level-1])
        else:
            return MONSTER[self.level-1]
         
    def is_awake(self):
        return self.state == Monster.AWAKEN
    
    def awake(self):
        """
        Change state to aggressive
        """
        self.state = min(self.state + 1, Monster.AWAKEN)
        
    def tile(self):
        """
        Monster tile on two characters
        """
        if self.is_awake():
            if self.level < 10:
                return "M%s" % self.level
            else:
                return "ME"
        else:
            return "M~"
    
    def move(self, pos):
        """
        Moves to a new pos
        """
        self.pos = pos
        
    def heal(self):
        """
        The monster is healed from its wounds
        """
        self.hp = self.hpmax
        
    def upgrade(self):
        """
        The monster gains a level
        """
        if self.level < self.levelmax:
            self.level += 1
            self.hpmax = 1 + self.level * (self.level + 1)
            self.hp = self.hpmax
        
    def damage(self):
        """
        How much damage the monster inflicts
        """
        l2 = self.level
        l1 = max(0, l2 - 3)
        return 1 + random.randint(l1, l2) + random.randint(l1, l2) + random.randint(l1, l2)
    
    def stun(self, n):
        """
        Stun the monster
        """
        self.state = -n
        

###############################################################################
# Dungeon class
###############################################################################

class Dungeon:
    def __init__(self, size = (32, 32), ratio = 60, name = None, level = 1):
        """
        Initialization of a dungeon floor
        size   : (width, height)
        ratio  : ratio of rooms compared to the full surface (in %)
                 from 10 to 60
        name   : random seed in a string
        """
        self.size = size
        self.name = name
        self.level = level
        # Set the seed
        state = random.getstate()
        random.seed(name)
            
        # Creating the floor array
        # 0: the floor
        # 1: the walls
        self.floor = N.ones(size) * DUNGEON_WALL
        # rooms array
        self.rooms = N.ones(size)
        # number of cells rooms occupy
        self.surf_rooms = 0
        # doors, stairs, ... array
        self.special = N.ones(size) * SPECIAL_NONE
        # Dead end list
        self.list_de = []
        # Monsters dictionary
        self.monster = {}
        # Flag to know if ME added
        self.me_added = False
        
        self.corridor_v(False)
        
        r = self.size[0] * self.size[1] * ratio / 100
        n = 0
        nmax = r * 10
        
        while n < r:
            n += 1
            self.corridor_h()
            self.corridor_v()
            if self.surf_rooms < r:
                self.room()
        # Addition of doors to rooms
        self.special *= (1 - self.floor) * SPECIAL_DOOR
        # Addition of stairs and treasures to dead ends
        self.dead_end()
        # Restore random generator state
        random.setstate(state)
        
    
    def corridor_h(self, test = True):
        """
        A horizontal corridor
        """
        l = random.randint(2, 6) * 2 + 1
        x = (random.randint(2, self.size[0] - l - 2) / 2) * 2 + 1
        y = (random.randint(6, self.size[1] - 6) / 2) * 2 + 1
        if l / 5 > N.sum(N.sum(1 - self.floor[x:x+l, y])) > 0 or not test:
            self.floor[x:x+l, y] = DUNGEON_FLOOR
            self.list_de.append((x, y))
            self.list_de.append((x+l-1, y))
            return True
        return False
        
        
    def corridor_v(self, test = True):
        """
        A vertical corridor
        """
        l = random.randint(2, 6) * 2 + 1
        x = (random.randint(6, self.size[0] - 6) / 2) * 2 + 1
        y = (random.randint(2, self.size[1] - l - 2) / 2) * 2 + 1
        if l / 5 > N.sum(N.sum(1 - self.floor[x, y:y+l])) > 0 or not test:
            self.floor[x, y:y+l] = DUNGEON_FLOOR
            self.list_de.append((x, y))
            self.list_de.append((x, y+l-1))
            return True
        return False
        
    def room(self, pos = None, test = True):
        """
        A room
        """
        lx = random.randint(2, 5) * 2 + 1
        ly = random.randint(2, 5) * 2 + 1
        if pos is None:
            x = (random.randint(0, self.size[0] - lx - 2) / 2) * 2 + 1
            y = (random.randint(0, self.size[1] - ly - 2) / 2) * 2 + 1
        else:
            x, y = pos
        if (N.sum(N.sum(1 - self.floor[x:x+lx, y:y+ly])) > 0 \
            and N.sum(N.sum(1 - self.rooms[x:x+lx, y:y+ly])) == 0) \
            or not test:  
            # The room is above one corridor or more
            # but not above another room
            self.surf_rooms += lx * ly
            self.floor[x:x+lx, y:y+ly] = DUNGEON_FLOOR
            self.rooms[x:x+lx, y:y+ly] = 0
            self.special[x-1:x+lx+1, y-1:y+ly+1] = SPECIAL_DOOR
            self.special[x:x+lx, y:y+ly] = SPECIAL_NONE
            n = random.randint(1, 5 + self.level)
            posn = (x+random.randint(1, lx-1), y+random.randint(1, ly-1))
            if n == 1:
                self.add_special(posn, SPECIAL_POTION)
            elif n < 4:
                self.add_special(posn, SPECIAL_MUSHROOM)
            else:
                self.add_monster(posn, self.level)
            return True
        return False
    
    
    def weapon_params(self, pos):
        """
        Returns flavor and num of a weapon at pos in the dungeon
        """
        weap_flav = int(self.special[pos] % 10)
        weap_type = int((self.special[pos] - weap_flav) / 10 - 1)
        return weap_flav, weap_type
    
    
    def add_mushroom(self, pos, nb):
        """
        add mushrooms around pos after a monster is killed
        """
        l = list(DIRS8)
        random.shuffle(l)
        n = 0
        for i in range(len(l)):
            p = (pos[0] + l[i][0], pos[1] + l[i][1])
            if self.is_reachable(p) and self.special[p] == SPECIAL_NONE:
                n += 1
                self.add_special(p, SPECIAL_MUSHROOM)
                if n == nb:
                    break
        return n
                
    
    def add_special(self, pos, type):
        """
        Add something special to pos
        """
        if self.special[pos] == SPECIAL_NONE:
            self.special[pos] = type
            
    def has_special(self, pos, type):
        """
        True is there is a special type at pos, False either
        """
        return self.special[pos] == type
    
    def grab_special(self, pos, type):
        """
        Gets the special type at pos
        """
        if self.has_special(pos, type):
            self.special[pos] = SPECIAL_NONE
            return 1
        return 0

    def add_monster(self, pos, level):
        """
        Add a monster at pos
        """
        if self.is_reachable(pos):
            if level == 10:
                if self.me_added:
                    self.monster[pos] = Monster(pos, 9)
                else:
                    self.me_added = True
                    self.monster[pos] = Monster(pos, 10)
            else:
                self.monster[pos] = Monster(pos, level)
                
    
    def has_monster(self, pos):
        """
        True is there is a monster at pos, False either
        """
        return self.monster.has_key(pos)
    
    def bash_monster(self, pos, n):
        """
        Remove n points to monster health points
        """
        if self.has_monster(pos):
            if self.monster[pos].hp <= n:
                xp = self.monster[pos].hpmax
                self.monster.pop(pos)
                return xp
            else:
                self.monster[pos].hp -= n
                return 0
        
    def dead_end(self):
        """
        Dealing dead ends
        """
        nb_sp = 1
        for i in range(len(self.list_de)):
            x, y = self.list_de[i]
            if N.sum(N.sum(self.floor[x-1:x+2, y-1:y+2])) <> 7:
                # Add one potion every 3 monster
                if i % 3 == 0:
                    self.add_special((x, y), SPECIAL_POTION)
                else:
                    self.add_monster((x, y), self.level)
            else:
                # It is a real dead end
                nb_sp += 1
                if nb_sp < 5:
                    if nb_sp not in (SPECIAL_DOWNSTAIRS1, SPECIAL_DOWNSTAIRS2) or self.level < 9:
                        # Down stairs only before level 9
                        self.special[x, y] = nb_sp
                    # Record starting position
                    if nb_sp == 2:
                        self.pos_start = self.list_de[i]
                else:
                    # Add a weapon
                    if self.level == 9:
                        weap_type = SPECIAL_SWORD
                        weap_flav = WEAPON_FLAVOR5
                    else:
                        weap_type = random.choice((SPECIAL_SWORD, SPECIAL_AXE, SPECIAL_SPEAR, SPECIAL_WARHAMMER))
                        weap_flav = random.randint(max(0, self.level / 2 - 2), self.level / 2)
                    self.special[x, y] = weap_type + weap_flav
                    if self.level == 1:
                        l = 1
                    else:
                        l = self.level + 1
                    self.add_monster((x-1, y), l)
                    self.add_monster((x+1, y), l)
                    self.add_monster((x, y-1), l)
                    self.add_monster((x, y+1), l)
                        
        if nb_sp == 1:
            # No dead ends found
            # We add stairs manually
            self.special[self.list_de[0]] = SPECIAL_UPSTAIRS
            # Record starting position
            self.pos_start = self.list_de[0]
            if self.level < 9:
                self.special[self.list_de[1]] = SPECIAL_DOWNSTAIRS1
        elif nb_sp == 2:
            #print "Bottom reached !"
            pass

        
    def is_reachable(self, pos):
        """
        Return True is pos can be accessed
        False either
        """
        if self.has_special(pos, SPECIAL_DOOR):
            return False
        else:
            return self.floor[pos[0], pos[1]] == DUNGEON_FLOOR and \
                   not self.monster.has_key(pos)
 
###############################################################################
# Player class
###############################################################################

class Player:
    def __init__(self, size, seed, dungeon_name = "Elderlore", cols = 30, 
                 scores = {}, known_dungeon = {}, record = True):
        
        self.dsize = size
        
        ###############################################################################
        # Player Health
        ###############################################################################
        self.xp = 0
        self.level = 1
        self.levels = self.levels()
        """
        self.hp, self.hpmax = 10, 10
        self.deepness = 1
        self.deepness_max = 1
        """
        self.hp, self.hpmax = 10, 10
        self.deepness = 1
        self.deepness_max = 1
        self.mushroom = 0
        # List of mushroom pos seen by the player
        self.mush_seen = {}
        self.potion = 1
        # Mood to have a gore mode
        self.mood = 0
        self.mood_state = MOOD_QUIET
        self.mood_level = self.moods()
        # Flag to decide if we remove 1 mood point at the end of the turn
        # We do so only if mood has not been updated during the round
        self.mood_updated = False
        
        ###############################################################################
        # Player Weapons
        ###############################################################################
        # List of owned weapons
        self.weapon_flavor = [WEAPON_FLAVOR0, WEAPON_NONE, WEAPON_NONE, WEAPON_NONE]
        self.active_weapon = 0
        # Dir the player is facing (used in swords charges)
        self.dir = [0, 0]
        # Power of the sword charge
        self.charge = 0
        # Flag for axe
        self.hit_by_monster = False
        
        ###############################################################################
        # Player Memory
        ###############################################################################
        self.fov = max(size[0], size[1])        
        # Random seed and random state
        self.seed = []
        self.update_seed(seed)        
        self.record = record        
        # Key history
        self.history = []
        
        if dungeon_name == "random" or dungeon_name == "Random":
            self.dname = MName().New()
        else:
            self.dname = dungeon_name
        self.dname_full = "%s (%s, %s)" % (self.dname, self.dsize[0], self.dsize[1])
        self.cols = cols        
        # Dictionary of visited floors
        self.dict_dungeon = {}
        # Dictionary of know floors from ancestors
        self.known_dungeon = known_dungeon.copy()
        # List of starting pos in levels
        self.start_pos = [(0, 0)]
        # Loading the first floor
        self.load_dungeon_floor(self.start_pos[-1], False)
        self.pos = self.dungeon.pos_start
        self.known[self.pos] = 1
        # Messages of (text, color)
        self.message = []
        # Flag to test the end of the program
        # 0 : in game
        # 1 : killed
        # 2 : exited the mines
        self.exit = 0
        
        # A dictionary where key is dungeon name, and value is a tuple
        # each tuple contains all scores for one dungeon
        self.scores = scores        
        # Number of rounds (for the WINNER case)
        self.round = 0
        self.winner = False
        # Events
        self.init_event(EVENT_START)
        
        
    def init_event(self, event=EVENT_NONE):
        """
        Events for music
        """
        self.event = event
        
        
    def update_seed(self, seed):
        """
        Updates the random seed value
        """
        self.seed.append(seed)
        random.seed(seed)
        
        
    def record_history(self, key):
        """
        Records keys pressed by the player
        """
        self.history.append(key)
        
        
    def clean_history(self):
        """
        Removes Esc key at the end of history when continuing to play
        """
        if self.history[-1] == 27:
            self.history.pop(-1)
            
        
    def moods(self):
        """
        Compute mood thresholds to increase player mood
        """
        n = self.dsize[0] + self.dsize[1]
        return 0, n/2, 3*n/2
    
    
    def update_mood(self, trigger):
        """
        Updates player mood with mood triggers
        the more the player is wounded the most it is increased
        """
        mult = 1
        if trigger > 0 and self.hp < self.hpmax/3:
            mult = 4
        elif trigger > 0 and self.hp < 2*self.hpmax/3:
            mult = 2
        self.mood = max(0, self.mood + TRIGGERS[trigger] * mult)
        self.mood_updated = True
        
        
    def analyse_mood(self):
        """
        Analyse mood at the end of the turn
        """
        # Player calms down every turn
        if not self.mood_updated:
            self.mood = max(self.mood - 1, 0)
        self.mood_updated = False
        if self.mood >= self.mood_level[MOOD_BERZERK]:
            new_mood_state =  MOOD_BERZERK
            self.event = EVENT_BERZERK
        elif self.mood >= self.mood_level[MOOD_FRENZY]:
            new_mood_state =  MOOD_FRENZY
        else:
            new_mood_state =  MOOD_QUIET
        
        if new_mood_state < self.mood_state:
            # You calm down
            if self.mood_state == MOOD_BERZERK:
                self.add_message(_("You are not berzerk anymore."), COLOR_YELLOW)
            elif self.mood_state == MOOD_FRENZY:
                self.add_message(_("You calm down."), COLOR_YELLOW)
        elif new_mood_state > self.mood_state:
            # You get frenzier
            if self.mood_state == MOOD_FRENZY:
                self.add_message(_("You become berzerk!!!"), COLOR_YELLOW)
            elif self.mood_state == MOOD_QUIET:
                self.add_message(_("You become frenzy!"), COLOR_YELLOW)
                
        self.mood_state = new_mood_state
                
             
    def levels(self):
        """
        Compute xp amounts to increase player level
        for level 2 : player must kill 10 monster level 1 when 40 x 40
        for level 3 : player must kill 12 monster level 2 when 40 x 40
        for level 4 : player must kill 14 monster level 3 when 40 x 40
        ...
        """
        l = [0,]
        # n is the number of monsters to kill at dungeon level to reach next player level
        n = (self.dsize[0] + self.dsize[1]) / 10
        for level in range(1, 21):
            l.append(l[-1] + (n + 2 * level) * (1 +  level * (level + 1)))
        return l
    
    def increase_round(self):
        """
        One more round
        """
        self.round += 1
        self.analyse_mood()
        
        
    def change_active_weapon(self, type):
        """
        change the active weapon of the player
        """
        n = type / 10 - 1
        if self.weapon_flavor[n] <> WEAPON_NONE:
            if self.active_weapon == n:
                self.add_message(_("You already hold your %s %s.") % (WEAPON_FLAVOR[self.weapon_flavor[n]], WEAPON_NAME[n]),
                                 COLOR_BLUE)
                return False
            else:
                self.active_weapon = n
                self.add_message(_("You take your %s %s.") % (WEAPON_FLAVOR[self.weapon_flavor[n]], WEAPON_NAME[n]),
                                 COLOR_BLUE)
                return True
        else:
            self.add_message(_("You have no %s in your equipment.") % WEAPON_NAME[n],
                             COLOR_BLUE)
            return False
            
            
    def weapon_name(self, weap_num, weap_flav):
        """
        Returns the name of the weapon
        """
        if WEAPON_FLAVOR[weap_flav][0] in "aeiou":
            return _("an %s %s") % (WEAPON_FLAVOR[weap_flav], WEAPON_NAME[weap_num])
        else:
            return _("a %s %s") % (WEAPON_FLAVOR[weap_flav], WEAPON_NAME[weap_num])
        
        
    def help(self):
        """
        Help in game
        """
        help = (_("General help :"),
                _("--------------"),
                _("You are a young hero and to prove your strength, you decide to explore the mines nearby your native village."),
                _("But beware! It is said that those mines are haunted by dangerous monsters."),
                _("Only armed with your training sword and a health potion, you enter a maze of rooms and corridors."),
                "",
                _("- 'F2' : how to play"),
                _("- 'F3' : the tiles on screen"),
                _("- 'F4' : the keys"),
                _("--------"),
                _("(More to read in the readme.txt file)"))
        for mess in help:
            self.add_message(mess, COLOR_CYAN)
        
    def help_f2(self):
        """
        Help in game
        """
        help = (_("How to play ?"),
                _("-------------"),
                _("This game is a roguelike. It is turn-based, and once your character dies there is no loading back."),
                _("By moving in the four directions, you attack monsters, open doors, collect equipment or use stairs."),
                _("Your goal is to survive long enough in the mines, progressing by killing monsters and descending as deep as you can."),
                _("It is said that your true nemesis awaits for you at the bottom..."))
        for mess in help:
            self.add_message(mess, COLOR_CYAN)
            
    
    def help_f3(self):
        """
        Help in game : the tiles
        """
        help = (_("The tiles in the game"),
                _("---------------------"),
                _("## : walls"),
                _(".  : floor you can see"),
                _("++ : a door; bump into it to open it"),
                _("<< : descending stairs"),
                _(">> : ascending stairs"),
                _("M~ : monster sleeping; it will awake at your approach"),
                _("Mn : monster level n"),
                _("!  : a potion you (d)rink to recover Health Points"),
                _("*  : a magic mushroom you can eat while (r)esting"),
                _("/n : a sword of level n"),
                _("Pn : an axe of level n"),
                _("|n : a spear of level n"),
                _("Tn : a warhammer of level n"),
                _("&/ : you with your weapon"))
        for mess in help:
            self.add_message(mess, COLOR_CYAN)
        
    def help_f4(self):
        """
        Help in game : the keys
        """
        help = (_("The keys of the game"),
                _("--------------------"),
                _("- h, F2, F3, F4 : in-game help"),
                _("- keyboard arrows: to move and attack North, South, East and West"),
                _("- space : wait for a round"),
                _("- d : drink a health potion"),
                _("- r : rest to recover HP by eating mushrooms"),
                _("- e : rest and eat one mushroom"),
                _("- 1, 2, 3, 4 : equip your best sword, axe, spear, warhammer"),
                _("- i : weapons in your inventory"),
                _("- esc : save and close the game"))
        for mess in help:
            self.add_message(mess, COLOR_CYAN)
                    
    def inventory(self):
        """
        List all the player belongings
        """
        mess = _("You have")
        for n in range(len(self.weapon_flavor)):
            if self.weapon_flavor[n] <> WEAPON_NONE:
                if n == self.active_weapon:
                    mess = "%s %s (%s-%s)," % (mess, 
                                               self.weapon_name(n, self.weapon_flavor[n]),
                                               self.damage_min(n),
                                               self.damage_max(n))
                else:
                    mess = "%s %s," % (mess, self.weapon_name(n, self.weapon_flavor[n]))
        self.add_message("%s." % mess[:-1], COLOR_BLUE)
        
    
    def dist(self, pos1, pos2, dir4 = True):
        """
        calculate the distance between pos1 and pos2
        """
        dx = abs(pos1[0] - pos2[0])
        dy = abs(pos1[1] - pos2[1])
        if dir4:
            return dx + dy
        else:
            return max(dx, dy)
    
    
    def blocked(self, pos):
        """
        True is (x, y) cannot be accessed, False either
        """
        if self.dsize[0] >= pos[0] >= 0 and self.dsize[1] >= pos[1] >= 0:
            return self.dungeon.floor[pos] == DUNGEON_WALL \
                or self.dungeon.has_special(pos, SPECIAL_DOOR)
        return False
                
                
    def lit(self, pos):
        """
        True if cell at pos is lit, False either
        """
        return self.seen[pos] == 1
        
        
    def set_lit(self, pos):
        """
        Light the cell at pos
        """
        if 0 <= pos[0] <= self.dsize[0] and 0 <= pos[1] <= self.dsize[1]:
            self.seen[pos] = 1
            self.known[pos] = 1
    
    
    def _cast_light(self, cx, cy, row, start, end, radius, xx, xy, yx, yy, id):
        """
        Recursive lightcasting function
        """
        if start < end:
            return
        radius_squared = radius*radius
        for j in range(row, radius+1):
            dx, dy = -j-1, -j
            blocked = False
            while dx <= 0:
                dx += 1
                # Translate the dx, dy coordinates into map coordinates:
                X, Y = cx + dx * xx + dy * xy, cy + dx * yx + dy * yy
                # l_slope and r_slope store the slopes of the left and right
                # extremities of the square we're considering:
                l_slope, r_slope = (dx-0.5)/(dy+0.5), (dx+0.5)/(dy-0.5)
                if start < r_slope:
                    continue
                elif end > l_slope:
                    break
                else:
                    # Our light beam is touching this square; light it:                    
                    if dx*dx + dy*dy < radius_squared:
                        self.set_lit((X, Y))
                    if blocked:
                        # we're scanning a row of blocked squares:
                        if self.blocked((X, Y)):
                            new_start = r_slope
                            continue
                        else:
                            blocked = False
                            start = new_start
                    else:
                        if self.blocked((X, Y)) and j < radius:
                            # This is a blocking square, start a child scan:
                            blocked = True
                            self._cast_light(cx, cy, j+1, start, l_slope,
                                             radius, xx, xy, yx, yy, id+1)
                            new_start = r_slope
            # Row is scanned; do next row unless last square was blocked:
            if blocked:
                break
    
    
    def do_fov(self, radius):
        """
        Calculate lit squares from the given location and radius
        """
        self.seen = N.zeros(self.dsize)
        self.seen[self.pos] = 1
        x, y = self.pos
        for oct in range(8):
            self._cast_light(x, y, 1, 1.0, 0.0, radius,
                             MULT[0][oct], MULT[1][oct],
                             MULT[2][oct], MULT[3][oct], 0)
        
                
    def last_word(self):
        """
        Directly from Angband
        Found there : http://www.thangorodrim.net/humor.html
        """
        l = (_("It did HOW MUCH damage?!"),
             _("Just one more round before I use that health potion."),
             _("I'd sure get a lot of XP if I could beat that guy..."),
             _("Either he's going to kill me or I'm going to kill him."),
             _("Hey, I'm stunned, what's that?"),
             _("I think I've finally gotten the hang of this."),
             _("Wonder what that is?"),
             _("I'll be safe down these stai....arrrgh!"),
             _("Argh! Get of the keyboard you bloody cat... Oh No!"),
             _("Just one more turn..."),
             _("What's it doing this high in the dungeon?"),
             _("Aaargh!"))
        return random.choice(l)
    
    
    def deal_damage(self, tile, n, sound = None):
        """
        The player suffers n HPs of damage
        """
        self.hp -= n
        hit = random.choice((_("bites"), _("claws"), _("slashes"), _("scratches"), _("chomps"), \
                             _("gnaws"), _("gnarls"), _("kicks"), _("tears"), _("rips"), _("stings")))
        self.add_message(_("%s %s you for %s point(s) of damage !") % (tile, hit, n),
                         COLOR_MAGENTA)
        if self.hp > 0:
            if sound is not None:
                sound[CHANNEL_SOUNDS].queue(sound[SOUND_MONSTER_ATTACK])
            self.update_mood(TRIGGER_SUFFER)
        else:
            if sound is not None:
                sound[CHANNEL_SOUNDS].queue(sound[SOUND_MONSTER_KILL])
            self.exit = 1  
            self.event = EVENT_DEATH
            
    
    def add_mushroom_seen(self, pos):
        """
        Remembers a mushroom seen by the player
        """
        self.mush_seen[pos] = 1
        
            
    def remove_mushroom_seen(self, pos):
        """
        Removes a mushroom from the list self.mush_seen
        """
        if self.mush_seen.has_key(pos):
            del self.mush_seen[pos]
    
    def closest_mushroom(self, pos, dir4 = True):
        """
        Finds the closest mushroom to the pos of a monster
        """
        if len(self.mush_seen) == 0:
            # No mushroom seen
            return (1000, 1000), 1000
        else:
            d_mush = 1000
            for pos_found in self.mush_seen:
                d = self.dist(pos_found, pos, dir4)
                if d < d_mush:
                    d_mush = d
                    pos_mush = pos_found
            return pos_mush, d_mush
        
    
    def move_monsters(self, sound = None):
        """
        Browse all monsters and move awaken ones
        """
        # Temporary dictionary
        monsters = {}
        # Flag for axe fight
        flag_hit = False
        # New monsters to add
        add_monster = []
        
        for pos, monster in self.dungeon.monster.items():
            move = False
            if monster.is_awake():
                # Choose the closest between closest mushroom and player
                pos_mush, d_mush = self.closest_mushroom(pos, monster.level < 6)
                d_player = self.dist(pos, self.pos, monster.level < 6)
                if d_player < d_mush:
                    spos, d = self.pos, d_player
                else:
                    spos, d = pos_mush, d_mush
                
                if d == 1 and d_player < d_mush:
                    flag_hit = True
                    self.deal_damage(monster.name(), monster.damage(), sound)
                    
                elif d == 0 and not d_player < d_mush:
                    self.dungeon.grab_special(pos_mush, SPECIAL_MUSHROOM)
                    self.remove_mushroom_seen(pos_mush)
                    monster_name = monster.name()
                    if monster.hp == monster.hpmax:
                        if monster.level < monster.levelmax:
                            if sound is not None:
                                sound[CHANNEL_SOUNDS].queue(sound[SOUND_MONSTER_LEVELUP])
                            monster.upgrade()
                            self.add_message(_("%s eats a mushroom and transforms into %s!") % (monster_name, monster.name()),
                                     COLOR_MAGENTA)
                        elif monster.level < 4:
                            self.add_message(_("%s eats a mushroom.") % monster_name,
                                         COLOR_MAGENTA)
                        else:
                            # Invoke a new monster by adding it to the list 'add_monster'
                            dirs = DIRS8
                            random.shuffle(dirs)
                            for j in range(len(dirs)):
                                pos_test = (pos[0] + dirs[j][0], pos[1] + dirs[j][1])
                                if self.dungeon.is_reachable(pos_test) and \
                                (pos_test[0] <> self.pos[0] or pos_test[1] <> self.pos[1]):
                                    if sound is not None:
                                        sound[CHANNEL_SOUNDS].queue(sound[SOUND_MONSTER_SUMMON])
                                    l = random.randint(1, monster.level)
                                    add_monster.append((pos_test, l))
                                    self.add_message(_("%s invokes a friend!") % monster_name, COLOR_MAGENTA)
                                    if monster.level < 10:
                                        break
                    else:
                        if sound is not None:
                            sound[CHANNEL_SOUNDS].queue(sound[SOUND_REST])
                        monster.heal()
                        self.add_message(_("%s eats a mushroom and is fully healed!") % monster_name,
                                         COLOR_MAGENTA)
                else:
                    # The monster moves to the target
                    d_new = d
                    pos_alt = pos
                    if monster.level < 6:
                        dirs = DIRS
                    else:
                        dirs = DIRS8
                    random.shuffle(dirs)
                    for dir in dirs:
                        pos_temp = (pos[0] + dir[0], pos[1] + dir[1])
                        if self.dungeon.is_reachable(pos_temp) and \
                        (pos_temp[0] <> self.pos[0] or pos_temp[1] <> self.pos[1]) and \
                        not monsters.has_key(pos_temp):
                            pos_alt = pos_temp
                            d_temp = self.dist(pos_temp, spos, monster.level < 6)
                            if d_temp <= d_new:
                                d_new, pos_new = d_temp, pos_temp
                    move = d_new < d or pos_alt <> pos
                    if pos_alt <> pos and d_new == d:
                        # It is better to move further than not to move
                        pos_new = pos_alt
            if move:
                monsters[pos_new] = monster
            else:
                monsters[pos] = monster
        # Hack (cannot change dict while browsing it)        
        self.dungeon.monster = monsters
        
        # Adding new monsters
        for pos_test, l in add_monster:
            self.dungeon.add_monster(pos_test, l)
        
        if flag_hit:
            self.hit_by_monster = True
        else:
            self.hit_by_monster = False
            
    
    def tile(self):
        """
        Player tile on the screen
        """
        return "&%s" % WEAPON_TILE[self.active_weapon]
        
    
    def load_dungeon_floor(self, pos, save = True):
        """
        Loads a dungeon from its name, its level and a position
        """
        self.mush_seen = {}
        
        if save:
            # We save the information of the dungeon
            self.dict_dungeon[self.dungeon.name] = self.dungeon #(self.dungeon, self.known)
            self.known_dungeon[self.dungeon.name] = self.known
            
        name = "%s-%s (%s, %s)" % (self.dname, self.deepness, pos[0], pos[1])
        
        if self.dict_dungeon.has_key(name):
            # This floor has already been visited
            self.dungeon = self.dict_dungeon[name]
        else:
            self.dungeon = Dungeon(self.dsize, 45, name, self.deepness)
            
        if self.known_dungeon.has_key(name):
            # Player already knows this floor by his ancestors memory
            self.known = self.known_dungeon[name]
            """ * (self.dungeon.special <> SPECIAL_POTION) \
                * (self.dungeon.special <> SPECIAL_MUSHROOM)"""
        else:
            self.known = N.zeros(self.dsize)
            
        
    def add_message(self, message, color = None):
        """
        Add a message
        """
        if color is None:
            color = COLOR_WHITE
        list = []
        elt = ""
        for word in message.split(' '):
            if len(elt) + len(word) < self.cols:
                elt += " " + word
            else:
                list.append(elt[1:])
                elt = " " + word
        list.append(elt[1:])
        for mess in list:
            self.message.insert(0, (mess, color))
            if len(self.message) > 100:
                self.message.pop()
        
    
    def progress(self, xp, sound = None):
        """
        Player gets xp
        """
        self.xp += xp
        if self.xp >= self.levels[self.level]:
            self.event = EVENT_LEVELUP
            if sound is not None:
                sound[CHANNEL_SOUNDS].queue(sound[SOUND_PLAYER_LEVELUP])
            self.level += 1
            self.hpmax += self.hpmax / 2
            self.hp = self.hpmax
            self.add_message(_("You gain %s XP points and progress to level %s !") % (xp, self.level),
                             COLOR_YELLOW | COLOR_BOLD)
        else:
            self.add_message(_("You gain %s XP.") % xp)
            
        if xp == 150:
            self.winner = True
            self.add_message(_("Congratulations!!! You have slayed ME. You are a ** WINNER ** !"),
                             COLOR_YELLOW | COLOR_BOLD)
            self.add_message(_("Send me the movie file (edempure@gmail.com) and I'll publish it on http://landsof.elderlore.com."),
                             COLOR_YELLOW)
            self.exit = 2

        
    def drink(self, sound = None):
        """
        drinks a potion
        """
        if self.potion > 0:
            if self.mood_state < MOOD_BERZERK:
                if sound is not None:
                    sound[CHANNEL_SOUNDS].queue(sound[SOUND_DRINK])
                self.potion -= 1
                self.add_message(_("You drink a health potion and recover all your health points !"),
                                 COLOR_GREEN)
                self.hp = self.hpmax
                self.update_mood(TRIGGER_HEAL)
                return True
            else:
                mess = (_("Your berzerk mood prevents you from healing yourself."),
                        _("Blood! Blood! Blood!"),
                        _("You don't want to take care of yourself."),
                        _("Kill! Kill! Kill!"))
                self.add_message(random.choice(mess))
                return False
        else:
            self.add_message(_("You have no health potion to drink."))
            return False
            
    
    def rest(self, n = 1000, sound = None):
        """
        rest to recover HP by eating mushrooms
        """
        for pos, monster in self.dungeon.monster.items():
            if monster.is_awake():
                self.add_message(_("You cannot rest and eat while there are awaken monsters around."))
                return False
            
        if self.hp == self.hpmax: 
            self.add_message(_("You are already at full health points."))
            return False
        
        hp_rest = min(n, self.mushroom, self.hpmax - self.hp)
        if hp_rest == 0:
            self.add_message(_("You recover no health points. You need mushrooms!"))
            return False
        
        if sound is not None:
            sound[CHANNEL_SOUNDS].queue(sound[SOUND_REST])
                
        self.hp += hp_rest
        self.round += hp_rest
        self.mushroom -= hp_rest
        for i in range(hp_rest):
            self.update_mood(TRIGGER_REST)
                
        if self.hp == self.hpmax: 
            self.add_message(_("You rest for a while and eat enough mushrooms to recover all your health points."),
                             COLOR_GREEN)
        else:
            self.add_message(_("You rest and eat %s, recovering %s.") \
                             % (self._plural(hp_rest, _("mushroom")), self._plural(hp_rest, _("health point"))), \
                             COLOR_GREEN)
        return True

    
    def damage(self):
        """
        How much damage the player inflicts
        """
        l1 = self.weapon_flavor[self.active_weapon] + (self.charge + self.mood_state) * self.level
        if l1 == WEAPON_FLAVOR5:
            l1 += self.level
        if self.hit_by_monster and \
            (self.active_weapon == WEAPON_AXE or self.active_weapon == WEAPON_WARHAMMER) \
            and self.mood_state == MOOD_QUIET:
            l2 = l1 + self.level / 2
        else:
            l2 = l1 + self.level
        return 1 + random.randint(l1, l2) + random.randint(l1, l2)
    
    
    def damage_min(self, n):
        """
        How much damage the player inflicts at min with weapon n
        """
        l1 = self.weapon_flavor[n] + (self.charge + self.mood_state) * self.level
        if l1 == WEAPON_FLAVOR5:
            l1 += self.level
        return 1 + l1 + l1
    
    
    def damage_max(self, n):
        """
        How much damage the player inflicts at max with weapon n
        """
        l1 = self.weapon_flavor[n] + (self.charge + self.mood_state) * self.level
        if l1 == WEAPON_FLAVOR5:
            l1 += self.level
        if self.hit_by_monster and \
            (self.active_weapon == WEAPON_AXE or self.active_weapon == WEAPON_WARHAMMER) \
            and self.mood_state == MOOD_QUIET:
            l2 = l1 + self.level / 2
        else:
            l2 = l1 + self.level
        return 1 + l2 + l2
    
    
    def save(self):
        """
        save to a file
        """
        self.known_dungeon[self.dungeon.name] = self.known
        output = open('moe.sav', 'wb')
        # Pickle the player
        pickle.dump(self, output, pickle.HIGHEST_PROTOCOL)
        output.close()
    
    
    def save_movie(self, score, desc):
        """
        After die or exit, saves actions to a file
        """
        if not os.path.isdir('movies'):
            os.mkdir('movies')
        i = 0
        while True:
            name = '%s-%sx%s-%03d.moe' % (self.dname, self.dsize[0], self.dsize[1], i)
            if os.path.isfile(os.path.join('movies', name)):
                i += 1
            else:
                break
        output = open(os.path.join('movies', name), 'wb')
        # Pickle the data
        pickle.dump(desc, output, pickle.HIGHEST_PROTOCOL)        
        pickle.dump(self.dsize, output, pickle.HIGHEST_PROTOCOL)
        pickle.dump(self.dname, output, pickle.HIGHEST_PROTOCOL)
        pickle.dump(self.history, output, pickle.HIGHEST_PROTOCOL)
        pickle.dump(self.seed, output, pickle.HIGHEST_PROTOCOL)        
        pickle.dump(self.known_dungeon, output, pickle.HIGHEST_PROTOCOL)        
        output.close()
    
    def save_score(self):
        """
        Save score in dictionary
        """
        if self.winner:
            print _("You are a winner !")
            # Hack : when winner, the least rounds the better (for sorting ranks)
            score = 1000000 - self.round
            new_entry = _("** WINNER ** in %s rounds - Max depth %s - Char. lvl %s (%s)") \
            % (self.round, self.deepness_max, self.level, time.strftime("%c"))
        else:
            print _("You scored %s.") % self.xp
            score = self.xp
            new_entry = _("Score %04d - Max depth %s - Char. lvl %s (%s)") \
            % (score, self.deepness_max, self.level, time.strftime("%c"))
        print "------------------"
        
        if not os.path.isdir('morgue'):
            os.mkdir('morgue')
        morguefile = "%s-%sx%s.txt" % (self.dname, self.dsize[0], self.dsize[1])
        file = open(os.path.join('morgue', morguefile), "a")
        file.write(new_entry + "\n")
        file.close()
        
        if not self.scores.has_key(self.dname_full):
            # This is the first score in this dungeon
            self.scores[self.dname_full] = []
            
        self.scores[self.dname_full].append((score, new_entry))
        self.scores[self.dname_full].sort(lambda x, y: cmp(y[0],x[0]))
        
        print _("%s ranks :") % self.dname_full
        print "-" * (len(self.dname_full) + 8)
        for i in range(len(self.scores[self.dname_full])):
            print "%03d : %s" % (i+1, self.scores[self.dname_full][i][1])
        
        if self.record:
            self.save_movie(score, new_entry)
            
            
    def grab_mushroom(self, pos, sound = None):
        """
        Grab a mushroom when you to it
        or when you stay over one
        """ 
        if sound is not None:
            sound[CHANNEL_SOUNDS].queue(sound[SOUND_GRAB_STUFF])
        self.add_message(_("You grab a mushroom."))
        self.mushroom += self.dungeon.grab_special(pos, SPECIAL_MUSHROOM)
        self.remove_mushroom_seen(pos)
        
                    
    def update_dir(self, pos):
        """
        Updates the direction the player is facing
        """
        dir = (self.pos[0] - pos[0], self.pos[1] - pos[1])
        if self.dir == dir and self.dir <> (0, 0) and self.active_weapon == WEAPON_SWORD:
            self.charge += 1
        else:
            self.charge = 0
        self.dir = (self.pos[0] - pos[0], self.pos[1] - pos[1])        
    
    
    def _plural(self, n, text):
        if n > 1:
            return "%s %ss" %(n, text)
        else:
            return "%s %s" %(n, text)
        
    
    def move(self, pos, coef = 1, sound = None):
        """
        Tries to move the player to the new pos
        s is the curses screen object
        coef is an XP multiplier when you combo monsters (1, 2, 4, 8, ...)
        """
        
        if pos[0] == self.pos[0] and pos[1] == self.pos[1]:
            if self.dungeon.has_special(pos, SPECIAL_MUSHROOM):
                # mushroom
                self.grab_mushroom(pos, sound)
            else:
                self.add_message(_("You wait..."))
            
        elif self.dungeon.has_monster(pos):
            
            monster_name = self.dungeon.monster[pos].name()
            
            if self.hit_by_monster and \
            (self.active_weapon == WEAPON_AXE or self.active_weapon == WEAPON_WARHAMMER) \
            and self.mood_state == MOOD_QUIET:
                self.add_message(_("You feel fuzzy while you use your weapon..."))
            
            if self.active_weapon == WEAPON_SWORD \
            and self.charge > 0:
                if self.dir == (pos[0] - self.pos[0], pos[1] - self.pos[1]):
                    self.add_message(_("Sword charge #%d !") % self.charge,
                                     COLOR_YELLOW | COLOR_BOLD)
                else:
                    self.charge = 0
                
            n = self.damage() * coef
            l = self.dungeon.monster[pos].level
            xp = self.dungeon.bash_monster(pos, n) * coef
            
            if xp > 0:
                
                if sound is not None:
                    sound[CHANNEL_SOUNDS].queue(sound[SOUND_PLAYER_KILL])
            
                if self.active_weapon == WEAPON_AXE:
                    if coef > 1:
                        self.add_message(_("Axe whirl #%d !") % coef, COLOR_YELLOW | COLOR_BOLD)
                    self.add_message(_("You slash %s for %s of damage, killing him.") % (monster_name, self._plural(n, _("point"))),
                                     COLOR_YELLOW)
                    if coef == 1:
                        random.shuffle(DIRS8)
                        for dir in DIRS8:
                            pos_next = (self.pos[0] + dir[0], self.pos[1] + dir[1])
                            if pos_next <> pos and self.dungeon.has_monster(pos_next):
                                time.sleep(.1)
                                #self.display(s)
                                self.move(pos_next, coef * 2, sound)
                    
                elif self.active_weapon == WEAPON_SPEAR:
                    # Spear
                    self.add_message(_("Spear charge #%d !") % coef, COLOR_YELLOW | COLOR_BOLD)
                    self.add_message(_("You charge %s for %s of damage, killing him.") % (monster_name, self._plural(n, _("point"))),
                                 COLOR_YELLOW)
                    pos_next = (2 * (pos[0] - self.pos[0]) + self.pos[0],
                                2 * (pos[1] - self.pos[1]) + self.pos[1])
                    self.pos = (pos[0], pos[1])
                    #self.display(s)
                    time.sleep(.1)
                    self.move(pos_next, coef * 2, sound)
                
                elif self.active_weapon == WEAPON_WARHAMMER:
                    self.add_message(_("You bash %s for %s of damage, killing him.") % (monster_name, self._plural(n, _("point"))),
                                 COLOR_YELLOW)
                    
                else:
                    self.add_message(_("You hit %s for %s of damage, killing him.") % (monster_name, self._plural(n, _("point"))),
                                 COLOR_YELLOW)
                    
                self.progress(xp, sound)
                n = self.dungeon.add_mushroom(pos, l + 1)
                self.add_message(_("%s drops %s on the floor.") % (monster_name, self._plural(n, _("mushroom"))))
                if self.dungeon.has_special(self.pos, SPECIAL_MUSHROOM):
                    # mushroom
                    self.grab_mushroom(self.pos, sound)
                self.update_mood(TRIGGER_KILL)
                
            else:
                if sound is not None:
                    sound[CHANNEL_SOUNDS].queue(sound[SOUND_PLAYER_ATTACK])
            
                if self.active_weapon == WEAPON_WARHAMMER:
                    m = self.weapon_flavor[self.active_weapon] + 1
                    if random.randint(0, m + self.dungeon.monster[pos].level) <= m:
                        # Push or knock ?
                        knock = False
                        self.add_message(_("Warhammer charge #%d !") % m,
                                         COLOR_YELLOW | COLOR_BOLD)
                        pos_monster = pos
                        for i in range(m+1):
                            pos_next = ((2 + i) * (pos[0] - self.pos[0]) + self.pos[0],
                                        (2 + i) * (pos[1] - self.pos[1]) + self.pos[1])
                            if self.dungeon.is_reachable(pos_next):
                                # Push monster
                                self.dungeon.monster[pos_next] = self.dungeon.monster.pop(pos_monster)
                                pos_monster = pos_next
                                time.sleep(.1)
                                #self.display(s)
                            else:
                                # Knock monster
                                knock = True
                                self.dungeon.monster[pos_monster].stun(m)
                                # Break door behind
                                if self.dungeon.has_special(pos_next, SPECIAL_DOOR):
                                    self.dungeon.grab_special(pos_next, SPECIAL_DOOR)
                                # Stun monster behind
                                elif self.dungeon.has_monster(pos_next):
                                    self.dungeon.monster[pos_next].stun(m)
                                time.sleep(.1)
                                #self.display(s)
                                self.add_message(_("You bash %s for %s and stun him for %s.") % \
                                                 (monster_name, self._plural(n, _("point")), self._plural(m, _("round"))),
                                                 COLOR_YELLOW)
                                break
                        if not knock:
                            # Push monster
                            self.add_message(_("You bash %s for %s of damage.") % (monster_name, self._plural(n, _("point"))),
                                      COLOR_YELLOW)
                        # Move player
                        if self.dungeon.is_reachable(pos):
                            self.pos = (pos[0], pos[1])                                
                            
                    else:
                        self.add_message(_("You bash %s for %s of damage.") % (monster_name, self._plural(n, _("point"))),
                                      COLOR_YELLOW)
                        
                else:
                    self.add_message(_("You hit %s for %s of damage.") % (monster_name, self._plural(n, _("point"))),
                                      COLOR_YELLOW)
                         
        elif self.dungeon.has_special(pos, SPECIAL_DOOR):
            if sound is not None:
                    sound[CHANNEL_SOUNDS].queue(sound[SOUND_OPEN_DOOR])
            self.add_message(_("You open the door."))
            self.dungeon.grab_special(pos, SPECIAL_DOOR)
            
        elif self.dungeon.is_reachable(pos):
            
            self.pos = (pos[0], pos[1])
            
            if self.dungeon.special[pos] >= SPECIAL_SWORD:
                weap_flav, weap_num = self.dungeon.weapon_params(pos)
                if weap_flav > self.weapon_flavor[weap_num]:
                    if sound is not None:
                        sound[CHANNEL_SOUNDS].queue(sound[SOUND_GRAB_STUFF])
                    self.add_message(_("You grab %s.") % self.weapon_name(weap_num, weap_flav),
                                     COLOR_BLUE)
                    self.weapon_flavor[weap_num] = weap_flav
                    self.dungeon.special[pos] = 0
                elif weap_flav < self.weapon_flavor[weap_num]:
                    self.add_message(_("You already have a better %s.") % WEAPON_NAME[weap_num])
                else:                    
                    self.add_message(_("You already have %s.") % self.weapon_name(weap_num, weap_flav))
            
            elif self.dungeon.has_special(pos, SPECIAL_MUSHROOM):
                # mushroom
                self.grab_mushroom(pos, sound)
            
            elif self.dungeon.has_special(pos, SPECIAL_POTION):
                # potion
                if sound is not None:
                    sound[CHANNEL_SOUNDS].queue(sound[SOUND_GRAB_STUFF])
                self.add_message(_("You grab a health potion."))
                self.potion += self.dungeon.grab_special(pos, SPECIAL_POTION)

            elif self.dungeon.has_special(pos, SPECIAL_DOWNSTAIRS1) or \
                 self.dungeon.has_special(pos, SPECIAL_DOWNSTAIRS2):
                # Stairs down
                self.add_message(_("You go down the stairs."))
                self.deepness += 1
                self.deepness_max = max(self.deepness_max, self.deepness)
                self.load_dungeon_floor(pos, True)
                self.pos = self.dungeon.pos_start
                self.start_pos.append(pos)
                self.known[self.pos] = 1
                self.event = EVENT_STAIRSDOWN
                
            elif self.dungeon.has_special(pos, SPECIAL_UPSTAIRS):
                # Stairs up
                if self.deepness == 1:
                    self.add_message(_("You know there is no turning back, don't you?"))
                    #self.exit = 2
                else:
                    self.add_message(_("You go up the stairs."))
                    self.deepness -= 1
                    self.pos = self.start_pos[-1]
                    self.start_pos.pop()
                    self.load_dungeon_floor(self.start_pos[-1], True)
                    self.known[self.pos] = 1               
                    self.event = EVENT_STAIRSUP
        else:
            self.add_message(_("You cannot go there."))
            return False
    
        return True

            
###############################################################################
# Main
###############################################################################
def load_config():
    """
    Loads moe.ini file
    """
    CURSES_DIRS = "{32: (0, 0), 258: (0, 1), 259: (0, -1), 260: (-1, 0), 261: (1, 0), 350: (0, 0)}"
    PYGAME_DIRS = "{32: (0, 0), 273: (0, -1), 274: (0, 1), 275: (1, 0), 276: (-1, 0)}"
    
    if not os.path.isfile('moe.ini'):
        conf_new = ConfigParser.ConfigParser()
        
        conf_new.add_section('Game')
        conf_new.set('Game', 'Name', 'Random')
        conf_new.set('Game', 'Width', 40)
        conf_new.set('Game', 'Height', 40)
        
        conf_new.add_section('Movie')
        conf_new.set("Movie", 'Record', True)
        conf_new.set("Movie", 'Speed', 500)
        
        conf_new.add_section('Curses')
        conf_new.set('Curses', 'Cols', 30)
        conf_new.set('Curses', 'Dirs', CURSES_DIRS)
        
        conf_new.add_section("Pygame")
        conf_new.set('Pygame', 'TileSize', 12)
        conf_new.set('Pygame', 'Dirs', PYGAME_DIRS)
        conf_new.set('Pygame', 'ScreenWidth', 1024)
        conf_new.set('Pygame', 'ScreenHeight', 600)
        conf_new.set('Pygame', 'Fullscreen', False)
        conf_new.set('Pygame', 'Music', True)
        
        # Save the config file
        conf_new.write(open('moe.ini', 'w'))
        
    conf = ConfigParser.ConfigParser()
    conf.read('moe.ini')
    
    name = conf.get("Game", "Name")
    width = conf.getint("Game", "Width")
    height = conf.getint("Game", "Height")
    conf_game = (name, width, height)
    
    record = conf.getboolean("Movie", "Record")
    replay_speed = conf.getint("Movie", "Speed")
    conf_movie = (record, replay_speed)
    
    cols = conf.getint("Curses", "Cols")
    dirs = conf.get("Curses", "Dirs")
    conf_curses = (cols, eval(dirs))
    
    #return name, eval(dirs), width, height, cols, record, replay_speed
    tilesize = conf.getint("Pygame", "TileSize")
    dirs = conf.get("Pygame", "Dirs")
    screenwidth = conf.getint("Pygame", "ScreenWidth")
    screenheight = conf.getint("Pygame", "ScreenHeight")
    fullscreen = conf.getboolean("Pygame", "Fullscreen")
    music = conf.getboolean("Pygame", "Music")
    conf_pygame = (tilesize, eval(dirs), screenwidth, screenheight, fullscreen, music)
    
    return conf_game, conf_movie, conf_curses, conf_pygame
    
    
