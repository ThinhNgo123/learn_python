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

import moe
import curses
import sys
import os
import time
import pickle

CURSES_DIRS = {curses.KEY_UP : (0, -1),     # North
               curses.KEY_DOWN : (0, 1),    # South
               curses.KEY_LEFT : (-1, 0),   # West
               curses.KEY_RIGHT : (1, 0),   # East
               ord(' ') : (0, 0),           # to wait
               curses.KEY_B2 : (0, 0)}
               
CURSES_DIRS8 = {curses.KEY_UP : (0, -1),     # North
                curses.KEY_DOWN : (0, 1),    # South
                curses.KEY_LEFT : (-1, 0),   # West
                curses.KEY_RIGHT : (1, 0),   # East
                ord(' ') : (0, 0),           # to wait
                curses.KEY_B2 : (0, 0),
                curses.KEY_A1 : (-1, -1),    # North West
                curses.KEY_A3 : (1, -1),     # North East
                curses.KEY_C1 : (-1, 1),     # South West
                curses.KEY_C3 : (1, 1)}      # South East


def update_display(s, player):
    """
    Display the dungeon floor on the given curses
    """
    # Screen init
    h, w = s.getmaxyx()
    n = player.cols + 1
    
    # Clear the screen
    for i in range(2, h - 1):
        s.addstr(i, 0, " " * (w - n - 1))
    
    for x in range(player.dsize[0]):
        xx = (x - player.pos[0] + (w - n)/ 4) * 2 + 1
        if 0 <= xx < w - n:
            for y in range(player.dsize[1]):
                yy = y - player.pos[1] + h / 2 - 2
                if 1 < yy < h - 1:
                    color = CURSES_COLOR[moe.COLOR_WHITE]
                    ch = "  "
                    if player.known[x, y] == 1:    
                        if x == player.pos[0] and y == player.pos[1]:
                            # Display the player
                            ch = player.tile()
                            if player.mood_state == moe.MOOD_BERZERK:
                                color = CURSES_COLOR[moe.COLOR_MAGENTA]
                            elif player.hp < player.hpmax / 3:
                                color = CURSES_COLOR[moe.COLOR_RED]
                            elif player.hp < 2 * player.hpmax / 3:
                                color = CURSES_COLOR[moe.COLOR_YELLOW]                               
                            else:
                                color = CURSES_COLOR[moe.COLOR_WHITE]
                            colorhp = color
                        else:
                            if player.lit((x, y)) and player.dungeon.monster.has_key((x, y)):
                                # Display a monster
                                ch = player.dungeon.monster[(x, y)].tile()
                                color = CURSES_COLOR[moe.COLOR_MAGENTA]
                                player.dungeon.monster[(x, y)].awake()
                                
                            elif player.dungeon.special[x, y] >= moe.SPECIAL_SWORD:
                                # Display a weapon
                                weap_flav, weap_type = player.dungeon.weapon_params((x, y))
                                ch = "%s%s" % (moe.WEAPON_TILE[weap_type], weap_flav)
                                color = CURSES_COLOR[moe.COLOR_BLUE]
                                if weap_flav > player.weapon_flavor[weap_type]:
                                    color = CURSES_COLOR[moe.COLOR_BLUE | moe.COLOR_BOLD]
                                
                            elif player.dungeon.has_special((x, y), moe.SPECIAL_DOOR):
                                ch = "++"
                                
                            elif player.dungeon.has_special((x, y), moe.SPECIAL_UPSTAIRS):
                                ch = "<<"
                                color = CURSES_COLOR[moe.COLOR_YELLOW]
                                
                            elif player.dungeon.has_special((x, y), moe.SPECIAL_DOWNSTAIRS1) or \
                                 player.dungeon.has_special((x, y), moe.SPECIAL_DOWNSTAIRS2):
                                ch = ">>"
                                color = CURSES_COLOR[moe.COLOR_YELLOW]
                                
                            elif player.dungeon.has_special((x, y), moe.SPECIAL_MUSHROOM):
                                ch = "* "
                                color = CURSES_COLOR[moe.COLOR_GREEN]
                                player.add_mushroom_seen((x, y))            
                                
                            elif player.dungeon.has_special((x, y), moe.SPECIAL_POTION):
                                ch = "! "
                                color = CURSES_COLOR[moe.COLOR_GREEN]  
                                                                 
                            elif player.dungeon.floor[x, y] == moe.DUNGEON_WALL:
                                ch = "##"
                                
                            else:
                                if player.lit((x, y)):
                                    ch = ". "
                    
                    s.addstr(yy, xx, ch, color)
    
    info = _("Lvl 0 | HP 000/000 | XP 0000/0000 for lvl 00 | !00 | *00 | 000 | M 000/000/000")
    s.addstr(0, 0, info, CURSES_COLOR[moe.COLOR_WHITE])
    s.addstr(0, 4, "%d" % player.deepness, CURSES_COLOR[moe.COLOR_WHITE])
    s.addstr(0, 11, "%03d" % player.hp, colorhp)
    s.addstr(0, 15, "%03d" % player.hpmax, CURSES_COLOR[moe.COLOR_WHITE])
    s.addstr(0, 24, "%04d" % player.xp, CURSES_COLOR[moe.COLOR_WHITE])
    s.addstr(0, 29, "%04d" % player.levels[player.level], CURSES_COLOR[moe.COLOR_WHITE])
    s.addstr(0, 42, "%02d" % (player.level+1), CURSES_COLOR[moe.COLOR_WHITE])
    s.addstr(0, 48, "%02d" % player.potion, CURSES_COLOR[moe.COLOR_WHITE])
    s.addstr(0, 54, "%02d" % player.mushroom, CURSES_COLOR[moe.COLOR_WHITE])
    s.addstr(0, 59, "%03d" % player.round, CURSES_COLOR[moe.COLOR_WHITE])
    if player.mood < player.mood_level[1]:
        color_mood = CURSES_COLOR[moe.COLOR_WHITE]
    elif player.mood < player.mood_level[2]:
        color_mood = CURSES_COLOR[moe.COLOR_YELLOW]
    else:
        color_mood = CURSES_COLOR[moe.COLOR_MAGENTA]
    s.addstr(0, 67, "%03d" % player.mood, color_mood)
    s.addstr(0, 71, "%03d" % player.mood_level[1], CURSES_COLOR[moe.COLOR_WHITE])
    s.addstr(0, 75, "%03d" % player.mood_level[2], CURSES_COLOR[moe.COLOR_WHITE])
    
    nb = min(h-4, len(player.message))
    for i in range(nb):
        s.addstr(i+3, w - n + 1, " " * n)
        s.addstr(i+3, w - n + 1, player.message[nb-i-1][0], CURSES_COLOR[player.message[nb-i-1][1]])
        
    s.refresh()
    
    


if __name__ == "__main__":
    
    try:
        import psyco
        psyco.full()
    except ImportError:
        pass
    
    ###############################################################################
    # Load config
    ###############################################################################
    #mine_name, dirs, w, h, cols, record, replay_speed = moe.load_config(CURSES_DIRS)
    conf_game, conf_movie, conf_curses, conf_pygame = moe.load_config()
    mine_name, w, h = conf_game
    record, replay_speed = conf_movie
    cols, dirs = conf_curses
    
    if len(sys.argv) == 2:
        ###############################################################################
        # Load movie
        ###############################################################################
        if os.path.isfile(sys.argv[1]):
            print _("Load movie %s...") % sys.argv[1]
            pkl_file = open(sys.argv[1], 'rb')
            desc = pickle.load(pkl_file)
            size = pickle.load(pkl_file)
            name = pickle.load(pkl_file)
            history = pickle.load(pkl_file)
            seed = pickle.load(pkl_file)
            known_dungeon = pickle.load(pkl_file)
            pkl_file.close()
            replay = True
            player = moe.Player(size, seed.pop(0), name, cols, {}, known_dungeon)
            
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
        ###############################################################################
        # Player init
        ###############################################################################
        replay = False
        seed = time.time()
        if os.path.isfile('moe.sav'):
            pkl_file = open('moe.sav', 'rb')
            player = pickle.load(pkl_file)
            pkl_file.close()
            if player.exit == 0:
                # the game continues
                print _("Game loaded...")
                player.update_seed(seed)
            else:
                # Let's start with a new player
                print _("New game initiated in the mines of %s...") % mine_name
                player = moe.Player((w, h), seed, mine_name, cols, player.scores, player.known_dungeon, record)
        else:
            # No save file yet
            player = moe.Player((w, h), seed, mine_name, cols, {}, {}, record)

    ###############################################################################
    # Curses init
    ###############################################################################
    
    s = curses.initscr()
    curses.start_color()
    curses.noecho()
    curses.cbreak()
    c = []
    for i in range(1, 16):
        curses.init_pair(i, i % 8, 0)
        if i < 8:
            c.append(curses.color_pair(i))
        else:
            c.append(curses.color_pair(i) | curses.A_BOLD)
    s.keypad(1)
    curses.curs_set(0)    
    
    CURSES_COLOR = (curses.color_pair(curses.COLOR_BLACK),
                    curses.color_pair(curses.COLOR_BLUE),
                    curses.color_pair(curses.COLOR_CYAN),
                    curses.color_pair(curses.COLOR_GREEN),
                    curses.color_pair(curses.COLOR_MAGENTA),
                    curses.color_pair(curses.COLOR_RED),
                    curses.color_pair(curses.COLOR_WHITE),
                    curses.color_pair(curses.COLOR_YELLOW),
                    curses.color_pair(curses.COLOR_BLACK) | curses.A_BOLD,
                    curses.color_pair(curses.COLOR_BLUE) | curses.A_BOLD,
                    curses.color_pair(curses.COLOR_CYAN) | curses.A_BOLD,
                    curses.color_pair(curses.COLOR_GREEN) | curses.A_BOLD,
                    curses.color_pair(curses.COLOR_MAGENTA) | curses.A_BOLD,
                    curses.color_pair(curses.COLOR_RED) | curses.A_BOLD,
                    curses.color_pair(curses.COLOR_WHITE) | curses.A_BOLD,
                    curses.color_pair(curses.COLOR_YELLOW) | curses.A_BOLD)

    try:
                 
        ###############################################################################
        # Screen init
        ###############################################################################
            
        if replay:
            player.add_message(_("Playing movie file '%s'.") % desc, moe.COLOR_CYAN)
        else:
            if player.round == 0:
                player.add_message(_("You enter the mines of %s.") % player.dname, moe.COLOR_WHITE)
                player.add_message(_("Hit 'h' anytime for in-game help."), moe.COLOR_CYAN)
                player.add_message(_("Good luck!"), moe.COLOR_WHITE)
        
        player.do_fov(player.fov)
        update_display(s, player)
        
        ###############################################################################
        # Main loop
        ###############################################################################

        while True:
            # Flag to count actions that cost a round and others that do not
            round = False
            # Input by keyboard or history of keys pressed
            if replay:
                k = history.pop(0)
            else:
                k = s.getch()
                player.record_history(k)
            # ESC hit
            if k == 27:
                if replay and len(seed) > 0:
                    # The movie continues
                    player.update_seed(seed.pop(0))
                else:
                    # Usual exit of the game
                    # When player hit 'Esc'
                    # or the end of the movie is reached
                    break
            
            elif CURSES_DIRS.has_key(k):
                # Moving
                old_pos = (player.pos[0], player.pos[1])
                new_pos = (player.pos[0] + dirs[k][0], player.pos[1] + dirs[k][1])
                round = player.move(new_pos)
                if round:
                    player.update_dir(old_pos)
                player.do_fov(player.fov)
            
            elif k == ord('d'):
                # Drink a health potion
                round = player.drink()
            
            elif k == ord('r'):
                # Rest and eat mushrooms
                round = player.rest()
                
            elif k == ord('e'):
                # Eat one mushroom
                round = player.rest(1)
                
            elif k == ord('1'):
                round = player.change_active_weapon(moe.SPECIAL_SWORD)
                
            elif k == ord('2'):
                round = player.change_active_weapon(moe.SPECIAL_AXE)
                
            elif k == ord('3'):
                round = player.change_active_weapon(moe.SPECIAL_SPEAR)
                
            elif k == ord('4'):
                round = player.change_active_weapon(moe.SPECIAL_WARHAMMER)
                
            else:
                if k == ord('i'):    
                    player.inventory()
                    
                elif k == ord('h'):
                    player.help()       
                                 
                elif k == curses.KEY_F2:
                    player.help_f2()
                    
                elif k == curses.KEY_F3:
                    player.help_f3()
                    
                elif k == curses.KEY_F4:
                    player.help_f4()
                    
            if round:
                player.increase_round()
                player.move_monsters()
                     
            update_display(s, player)
            
            if replay and k <> 27:
                time.sleep(replay_speed / 1000.)
                
            if player.exit:
                break
    
    ###############################################################################
    # Stop curses
    ###############################################################################
    finally:
        # Curses ending
        if player.exit:
            if player.exit == 1:
                player.add_message(player.last_word(), moe.COLOR_MAGENTA)            
            player.add_message("Press ESC to end the game.",
                               moe.COLOR_WHITE | moe.COLOR_BOLD)
            update_display(s, player)
            k = 0
            while k <> 27:
                k = s.getch()
        s.keypad(0)
        curses.echo()
        curses.nocbreak()
        curses.endwin()
    
    ###############################################################################
    # Exit with some words
    ###############################################################################
    print _("Last messages :")
    print _("---------------")
    n = min(20, len(player.message))
    for i in range(n):
        print player.message[n-i-1][0]
    print _("---------------")
    
    if not replay:
        if player.exit:
            player.save_score()
        player.save()


