################################################################################
#                                                                              #
#                              MINES of ELDERLORE                              #
#                                                                              #
# An Ascii roguelike with :                                                    #
# * Permanent levels                                                           #
# * Simple and easy gameplay                                                   #
# * High scores that you can compare with others                               #
# http://landsof.elderlore.com                                                 #
#                                                                              #
# Released under the GNU General Public License                                #
# (see the file 'COPYING.txt' file for the complete licence description)       #
#                                                                              #
################################################################################


Here is the fourth beta release of the final 1.0 version of Mines of Elderlore.

This version is released for feedback and debugging.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
SUMMARY :
=========
1. INSTALL
    1.1 From the source file
    1.2 From the Windows binary

2. PLAY
    2.1 The game
        2.1.1 Synopsis
        2.1.2 Gameplay
        2.1.3 Death
        2.1.4 Scores
    2.2 The screen
        2.2.1 The Curses screen
        2.2.2 The Info bar
    2.3 The keys
    2.4 Fights
        2.4.1 Monsters
        2.4.2 The weapons: basics
        2.4.3 The weapons: advanced
    2.5 Frenziness
        2.5.1 Your mood
        2.5.2 The frenzy state
        2.5.3 The berzerk state
    2.6 Player advancement

3. STATISTICS
    3.1 The player
    3.2 Weapon damages
    3.3 Damage bonuses
    3.4 Monsters
    
4. FILES
    4.1 The 'moe.ini' file
        4.1.1 The [Movie] section
        4.1.2 The [Game] section
        4.1.3 The [Curses] section
        4.1.4 The [Pygame] section
    4.2 Savegames
    4.3 Keymovie files
    4.4 Morgue files
    
5. ABOUT
    5.1 Changelog
    5.2 Genesis of the game
    5.3 Credits
    5.4 Licence
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. INSTALL
==========
1.1 From the source file
~~~~~~~~~~~~~~~~~~~~~~~~
You need Python, Pygame and the Numeric module to launch the game from its 
source file (under Ubuntu, you need to install "python", "python-pygame" and
"python-numeric" with Synaptic). 

Once Python and Numeric installed, you can download this file: 
http://downloads.sourceforge.net/elderlore/moe_source.1.0b4.zip 
and extract it to a folder. Launch it under a terminal window with the command 
"python moe-pygame.py".

If you want to play the game with no graphics, you can launch the curses version
in a terminal with the command "python moe-curses.py". If you change the 
terminal size, the game will adjust accordingly to maximize the display area. 
The minimal size for the game to play is 80 columns by 25 rows.

1.2 From the Windows binary
~~~~~~~~~~~~~~~~~~~~~~~~~~~
To play Mines of Elderlore under Windows, download this file: 
http://downloads.sourceforge.net/elderlore/moe_windows.1.0b4.zip
 and extract it to a folder. Launch it by double-clicking on "moe-pygame.exe".
 
The game has also been ported under Windows by using Wcurses. To play the game 
with no graphics, double-click on "moe-curses.exe". The display size of the game
is fixed at 80 columns by 25 rows, and cannot be changed.



2. PLAY
=======
2.1 The game
~~~~~~~~~~~~
2.1.1 Synopsis
--------------
You are a young hero and to prove your strength, you decide to clean the mines 
in the forest nearby your native village. Only armed with your training sword, 
you enter the haunted forest...

2.1.2 Gameplay
--------------
This game is a roguelike. It is turn-based, so you can take all the time you 
want to chose your strategy. 

By moving in the four directions with the arrow keys, you attack monsters, open 
doors, collect equipment or use stairs (see § 2.3 to learn about all the keys in
the game). Your goal is to survive long enough in the mines, progressing by 
killing monsters and descending as deep as you can. 

As you wander through different levels of the mines, you may find different
weapons of different values. Each weapon has intrinsic qualities and drawbacks, 
and provide different gameplay. Be creative ! Only by chosing the proper weapon 
in the right situation will you progress deep enough in the game (see § 2.4 and
2.5 to know more about weapons).

2.1.3 Death
-----------
Once your character dies there is no loading back: death is permanent, and the
only way to go when your character is dead is to start another one.

Yet there is one advantage for following players: they inherit their ancestor's
memory, and all levels that were previously explored will be known by the new
character.

2.1.4 Scores
------------
A score is given when you die, that equals your XP points. If you are a winner, 
your score will appear on the top of the other scores, different winner scores 
being sorted by the number of rounds they took.

A board of scores and ranks is keeped, and since every dungeon is the same for 
every player, it should be easy to compare performance each other. If you want 
to explore another dungeon, just change the 'name' value in 'moe.ini'. If you 
set this 'name' value to 'random' (without quotes), a new different dungeon will
be generated each time, with a randomized name.


2.2 The screen
~~~~~~~~~~~~~~
2.2.1 The Curses screen
-----------------------
The following symbols are displayed on the Curses screen:

## : walls
.. : floor you can see
++ : a door; bump into it to open it
<< : descending stairs
>> : ascending stairs
M~ : monster sleeping; it will awake at your approach
Mn : monster level n
!  : a health potion; (d)rink it to recover all your Health Points
*  : a magic mushroom; when you (r)est, you can eat them to recover HP. Don't 
let monsters eat them !
/n : a sword of level n
Pn : an axe of level n
|n : a spear of level n
Tn : a warhammer of level n
&/ : you with your weapon ! (a sword)

2.2.2 The Info bar
------------------
The top of the screen displays some usefull information for the player :
Lvl 1 | HP 10/10 | XP 000 (030 for lvl 2) | !01 | *00 | 000 | M 00/40/120

- Lvl 1 : your current level
- HP 10/10 : your current Health Points amount and your max Health Points amount
- XP 000 (030 for lvl 2) : your experience points, and the number you need to 
reach next level (you start at level 1)
- !01 : the health potions you own (you start with one health potion)
- *00 : the mushrooms you own (you start with no mushroom)
- 000 : the rounds (each action equals one round)
- M 00/40/120 : your current mood, followed by the frenzy threshold (40) 
and the berzerk threshold (120).

2.3 The keys
~~~~~~~~~~~~
Here are the keys you can use in the game:

- h, F2, F3, F4 : help in-game
- keyboard arrows : move and attack North, South, East and West
- space : wait for a round
- d : drink a health potion
- r : rest to recover HP by eating mushroom
- e : rest and eat one mushroom
- 1 : equip your best sword
- 2 : equip your best axe
- 3 : equip your best spear
- 4 : equip your best warhammer
- i : list your weapons and their quality.
- esc : save and close the game.

2.4 Fights
~~~~~~~~~~
2.4.1 Monsters
--------------
Demons populate the game levels, and will awake and try to attack you at the
moment they see you. They can be of different levels, from 1 to 10:

Monster Lvl |              Name
~~~~~~~~~~~~+~~~~~~~~~~~~~~~~~~                       
          1 |        Homunculus
          2 |               Imp
          3 |      Lesser Demon
          4 |             Demon
          5 |     Greater Demon
          6 |     Lesser Balrog
          7 |            Balrog
          8 |    Greater Balrog
          9 |    Balrog captain
         10 |                 ?
         
The greater their level, the more they will have health points, and the more 
they will inflict damage.

They can move one square on each round. Balrogs, which are winged creatures, 
move differently than others (even you !), and can move and attack in the eight 
directions. Other weaker monsters only move and attack in the four directions 
(north, south, east and west).

If you manage to kill a monster, it will drop some mushrooms to the floor. If a 
monster manage to take such a mushroom on the floor:
* if injured, it will eat it and be fully healed;
* otherwise it will eat it and will gain a level, call another demon to help him
or eat the mushroom with no other consequences, depending on the level monster 
and the dungeon deepness.
         
2.4.2 The weapons: basics
--------------------------
Weapons are of 4 different kinds : swords, axes, spears and warhammers. They can
be of different quality : basic ones for training, or made of iron, steel, 
mithril, adamant or vorpal.

Every weapon, when used against a monster, provides the same basic damage, based
on your level and the weapon quality.

Axes and warhammers are bigger weapons than swords and spears, and as such if
you use them just after being hit, you will have a damage penalty, and the 
message: "You feel fuzzy while you use your weapon..." will be displayed.

2.4.3 The weapons: advanced
----------------------------
Every weapon has a special ability that you can use to multiply your
strikes, causing devastating wounds if you are a true master of arms !

* Sword charge
  You can charge with swords to increase the damage you inflict. To do so, you
  need to move in one direction for several turns with your sword, then hit a
  monster in the same direction.

  Sword charges, when succeeded, are indicated by the yellow blod message :
  "Sword charge #n!" where n is the charge amount.

* Axe whirlwind
  If you kill a monster with your axe, you will initiate a whirlwind attack, and
  attack every monster around you, the first at 2x damage, the second 4x, and so 
  on.

  Axe whirlwinds, when succeeded, are indicated by the yellow bold message :
  "Axe whirl #n!" where n is the damage multiplier.

* Spear charge
  If you kill a monster with a spear, you will charge in the same round on the 
  monster killed position, and if there is a monster next in the same direction,
  you will attack it with double damage. If you kill the second monster, you
  will charge and attack with 4x damage, and so on until there are no more 
  monsters aligned.

  Spear charges, when succeeded, are indicated by the yellow bold message :
  "Spear charge #n!" where n is the damage multiplier.

* Warhammer charge
  When you hit a monster with your warhammer, there is a chance that you succeed
  a warhammer charge (based on monster level and you warhammer quality). If you 
  do so, you will move one step ahead, and the monster will be pushed several 
  steps backwards. If the monster hits something or somebody while being pushed 
  back, it will be knocked for several rounds.

  Warhammer charges, when succeeded, are indicated by the yellow bold message :
  "Warhammer charge #n!" where n is the number of cells the monster is pushed 
  back.

2.5 Frenziness
~~~~~~~~~~~~~~
2.5.1 Your mood
---------------
Your mood points are displayed on the upper-right corner of the screen. They are
followed by the frenzy threshold and the berzerk threshold :

M 12/40/120
(12 mood points / frenzy threshold at 40 / berzerk threshold at 120)

Those mood points are affected by particular situations. You can gain mood 
points when:
- you suffer from wounds
- you kill a monster

And you loose mood points when:
- you rest for a while
- you drink a health potion
- time passes

When your mood points reach the frenzy threshold, you reach the frenzy state. 
And if it reaches the berzerk threshold, you reach the berzerk state.

2.5.2 The frenzy state
----------------------
When frenzy, you get damage bonuses with every weapon, and you can use axes and
warhammers with no penalties.

2.5.3 The berzerk state
-----------------------
When berzerk, you get the advantages you can have when frenzy, with even more
damage bonuses, but there is a price to pay: the thrust for blood overwhelm you,
to the point that it's impossible for you to drink a health potion.

The only solution for you to leave this state is to calm down or rest after all
the monsters around you are dead.

2.6 Player advancement
~~~~~~~~~~~~~~~~~~~~~~
Every time you kill a monster, you gain as much experience points (XP) as the 
monster has health points (see § 3.4).

You start your adventure at level 1, with zero XP. If you manage to kill enough
monsters to have 30 XP, you will reach level 2 and your Health Points will 
increase from 10 to 15 HP (see § 3.1).

Each time your XPs reach a new threshold, you will gain a new level and your HPs
will increase accordingly.

When you gain a level, you are automatically healed from all your wounds

3. STATISTICS
=============
3.1 The player
~~~~~~~~~~~~~~                                           
Player  Lvl |       XP         HP
~~~~~~~~~~~~+~~~~~~~~~~~~~~~~~~~~~                        
          1 |        0         10                                 
          2 |       30         15                                 
          3 |      114         22                                 
          4 |      296         33                                 
          5 |      632         49                                 
          6 |     1190         73                                 
          7 |     2050        109                                 
          8 |     3304        163                                 
          9 |     5056        244                                 
         10 |     7422        366

3.2 Weapon damages
~~~~~~~~~~~~~~~~~~
Player  Lvl | Training       Iron      Steel    Mithril    Adamant     Vorpal
~~~~~~~~~~~~+~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
          1 |      1-3        3-5        5-7        7-9       9-11      13-15
          2 |      1-5        3-7        5-9       7-11       9-13      15-19
          3 |      1-7        3-9       5-11       7-13       9-15      17-23
          4 |      1-9       3-11       5-13       7-15       9-17      19-27
          5 |     1-11       3-13       5-15       7-17       9-19      21-31
          6 |     1-13       3-15       5-17       7-19       9-21      23-35
          7 |     1-15       3-17       5-19       7-21       9-23      25-39
          8 |     1-17       3-19       5-21       7-23       9-25      27-43
          9 |     1-19       3-21       5-23       7-25       9-27      29-47
         10 |     1-21       3-23       5-25       7-27       9-29      31-51

3.3 Damage bonuses
~~~~~~~~~~~~~~~~~~

Frenzy damage bonus = 2 x level

Berzerk damage bonus = 4 x level

Player  Lvl |   Frenzy    Berzerk
~~~~~~~~~~~~+~~~~~~~~~~~~~~~~~~~~~                             
          1 |        2          4                                 
          2 |        4          8                                 
          3 |        6         12                                 
          4 |        8         16                                 
          5 |       10         20                                 
          6 |       12         24                                 
          7 |       14         28                                 
          8 |       16         32                                 
          9 |       18         36                                 
         10 |       20         40
         
Sword charge bonus = 2 x charge x level

            |   Charge
Player  Lvl |        1          2          3          4          5          6
~~~~~~~~~~~~+~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
          1 |        2          4          6          8         10         12
          2 |        4          8         12         16         20         24
          3 |        6         12         18         24         30         36
          4 |        8         16         24         32         40         48
          5 |       10         20         30         40         50         60
          6 |       12         24         36         48         60         72
          7 |       14         28         42         56         70         84
          8 |       16         32         48         64         80         96
          9 |       18         36         54         72         90        108
         10 |       20         40         60         80        100        120

3.4 Monsters
~~~~~~~~~~~~
Monster Lvl |       HP     Damage
~~~~~~~~~~~~+~~~~~~~~~~~~~~~~~~~~~
          1 |        3        1-4                                 
          2 |        7        1-7                                 
          3 |       13       1-10                                 
          4 |       21       4-13                                 
          5 |       31       7-16                                 
          6 |       43      10-19                                 
          7 |       57      13-22                                 
          8 |       73      16-25                                 
          9 |       91      19-28                                 
         10 |      150      22-31

4. FILES
========
4.1 The 'moe.ini' file
~~~~~~~~~~~~~~~~~~~~~~
The 'moe.ini' file is a text file containing parameters used by the game. Here 
is how it looks like by default:

[Movie]
record = True
speed = 500

[Game]
dirs = {32:(0, 0), 258:(0, 1), 259:(0, -1), 260:(-1, 0), 261:(1, 0), 350:(0, 0)}
width = 40
cols = 30
name = Moria
height = 40

If there is a problem with this file, just delete it and launch the game, a new
'moe.ini' file will be created with those default values.

4.1.1 The [Movie] section
-------------------------
* record = True / False : if True, a keymovie file is saved when the game is 
finished (see 4.3 for details).
* speed = 500 : when displaying a movie, speed of turns (in ms).

4.1.2 The [Game] section
-------------------------
* width = 40 : the width of the dungeon. If changed, will generate a different
dungeon, even with the same dungeon 'name'.
* name = Moria : the dungeon name. For a given name, width and height, the same
dungeon will always be created. If you change this name to 'random' (without the
quotes), a random name will be given to the dungeon when a new game starts.
* height = 40 : the width of the dungeon. If changed, will generate a different
dungeon, even with the same dungeon 'name'.

4.1.3 The [Curses] section
-------------------------
* dir = {} : a Python dictionary containing the Curses direction keys used in 
the game. You can change those values if you want to set other keys for moving.
* cols = 30 : the width of the messages display area.

4.1.4 The [Pygame] section
-------------------------
* dirs = {} : a Python dictionary containing the Pygame direction keys used in 
the game. 
* fullscreen = False : Change it 'True' to play the game fullscreen.
* tilesize = 12 : the size of font tiles.
* screenheight = 600 : The screen height.
* music = True : Change it to 'False' if you don't want the music to be played.
* screenwidth = 1024 : The screen width.



4.2 Savegames
~~~~~~~~~~~~~
After the first play, an 'moe.sav' file is created in the game folder to keep 
your progress. Launch again the game and it will continue where you previously 
stopped.

If you die, your score is stored in the savefile and a new game is initiated.

4.3 Keymovie files
~~~~~~~~~~~~~~~~~~
If you die, a keymovie file is created in the 'movies' folder. You can play it
with the command :
python moe.py movies/keymovie_name.moe
To exit the keymovie, hit CTRL+Z.

4.4 Morgue files
~~~~~~~~~~~~~~~~
If you die, a score is given and stored both in the savefile and in a morgue
file. Each dungeon has its morgue file, so that you can compare your score in a
dungeon with previous games.

Morgue files are stores in the 'morgue' folder.


5. ABOUT
========
5.1 Changelog
~~~~~~~~~~~~~
Version 1.0 beta 4:
- [Bug] It is now really possible to hit monsters with axes and warhammers while
in fuzzy mode.
- [Bug] In pygame mode, you can use '1' to '4' keys from the keypad to change
your equipped weapon.
- [Bug] No more crashing to desktop when hitting a wrong key under moe-pygame.
- [Feature] In pygame mode, a menu is displayed to play multiple games without
quitting each time.
- [Feature] In pygame mode, if 'random' dungeon selected in 'moe.ini', the same
random dungeon will be proposed from game to game.
- [Feature] On floor level 'n', monsters can only progress to level 'n + n-1'.

Version 1.0 beta 3:
- new pygame release with graphics
- if a mushroom is dropped on the player, he will grab it automatically
- weapons flavor bug corrected (first weapons found will be training ones 
instead of iron ones)
- fuzzy state of axes and warhammers only hinders damage (instead of prevents
player from hitting monsters)
- monsters cannot move on player position anymore

Version 1.0 beta 2:
- sword charge is now effective only if the player hits the monster in the
same direction of his charge
- inventory now displays te player active weapon min and max damage
- mushrooms cannot be dropped on stairs anymore
- player can rest and eat mushrooms while in berzerk mood
- weapon flavor names have been changed
- monsters are now different kinds of demons
- the status bar displays HP and mood in different colors 
- player can get higher than level 10
- monsters can move in 8 directions from level 6
- M9 can summon a friend when fully healed and eating a mushroom
- readme.txt file updated

Version 1.0 beta 1:
- new key 'h', 'F2', 'F3' and 'F4' for in-game help
- when a player dies, some last words are displayed and the 'ESC' key must be
pressed to exit
- frenzy and berzerk player state
- bumping in a wall, displaying inventory or hitting a wrong key does not cost 
a round anymore
- you can charge with swords
- you can push and knock with warhammers
- you can whirlwind with axes
- chaining monsters with special attacks enhance damage
- if wounded, a monster is healed when eating a mushroom; if at full HP, it 
gains a level
- player keeps memory of visited dungeons by ancestors
- a movie of every finished game is recorded in the 'movie' folder; to play it 
back, type "python moe.py movies/movie_name.moe" in shell, or 
"moe.exe movies\movie_name.moe" under Windows command line
- a morgue file is created for each different dungeon, filled with records from 
dead players

Version 0.9:
- new colors on the screen :
    * monsters are magenta
    * potions and mushrooms are green
    * player is white when healhty, yellow when hp < 2/3 hpmax, and red when 
    hp < hpmax/3
    * stairs are yellow
    * weapons are blue, and bold if usefull   
- new colors in messages
- some balancing in player advancement and monster damage
- Now there is a winning case; if you succeed, the least rounds it took you, 
the better.
- messages are displayed on the right for better reading.

Version 0.7:
- 7DRL release !

5.2 Genesis of the game
~~~~~~~~~~~~~~~~~~~~~~~
This game has been created for the 7 day roguelike challenge:

http://roguebasin.roguelikedevelopment.org/index.php?title=7DRL

The code was only one file: http://landsof.elderlore.com/files/moe/moe.py. I 
wanted it to be full GNU/GPL v2, so that it may be of some help for anyone 
interested.

I started developing it with simple needs in mind: I wanted to create a little 
roguelike around the new dungeon generator I had just created for Lands of 
Elderlore, my other roguelike. And I wanted to test how I could implement those 
simple features:

* Permanent levels; well, not only permanent levels on your computer, but on
  every computer of every player! So that when you provide (automatically or by
  player input) a dungeon name, the same levels will always be created.

  Python is a great language for this, and it is really easy to store dungeons
  in a dictionary and save games with the pickle module.
  
  A common risk when creating permanent levels is to reduce the amount of space
  to explore for the player: once every level crawled, what can he do ? So I
  decided to create two downing stairs for every level, each one leading to a
  different -and permanent- level.
  
  There are 9 floors in Mines of Elderlore. That may not seem a lot, but with 
  this 'two-stairs' design, you can have as much as :
  1 + 2 + 4 + 8 + 16 + 32 + 64 + 128 + 256 = 511 different floors!
  
  Having permanent levels provides a great advantage: player can compare their
  scores. I did not have time to implement it yet, but I plan to provide an
  online display of every player scores on landsof.elderlore.com. By sending
  their keymovie files, not only players will be able to compete with each 
  other, but when published online their movies will inspire other players and
  challenge them to perform better! Some kind of Massively Mutliplayer Offline
  Role Playing Game ;-).
  
* Easy gameplay; roguelikes can have a steep learning curve for new comers, and
  to my point of view every effort to ease their first roguelike experiment 
  should be sherished.
  
  First idea is to display symbols with two ascii characters. So that the player
  can see at a glance what weapon he is wearing, what level is the monster in
  front of him, and so on. Simple and effective. And with fonts twice as high as
  large, symbols are displayed perfectly squared!
  
  Then I tried to add weapon special attacks based on the player movements 
  rather than additional keys or over complicated RPG skills. Charging is maybe
  the simplest example: by moving in the same direction during several rounds,
  you increase your 'charge' amount, and if you manage to hit a monster at the
  end, you will inflict increased damages.
  
  I think this enhanced gameplay based on player movement can really be 
  developped very far; you can count on me to investigate further on this !
  

5.3 Credits
~~~~~~~~~~~
5.3.1 Code
----------
* Thanks to the Python community for all its modules and for this wonderfull
  language
* Thanks to Peter for his script on Markov Chains here under Public Domain:
  http://www.pick.ucam.org/~ptc24/mchain.html
* The Field of View algorithm is directly taken from this RogueBasin article:
  http://roguebasin.roguelikedevelopment.org/index.php?
  title=PythonShadowcastingImplementation

5.3.2 Tiles and background
--------------------------
* "Dungeon.png" contains tiles drawn by David Gervais
* "Tiles.png" contains some tiles drawn by David Gervais (weapons, potion, 
  mushroom and some demons), other tiles are drawn by me (numbers) or modified 
  by me from David Gervais original tiles (Balrogs).
* "player.png" is part of the rogeuelike tileset called "RLTiles". You can find 
  this tileset here : http://rltiles.sf.net 
* The right leather panel has been drawn by David Gervais
* "abstra_blue.png", The blue screen at the beginning, has been made by Xactive,
  and is available there : http://art4linux.org/node/48
* "title.png" is made by me, Emmanuel Dempuré, with the help of CoolText
  (http://cooltext.com/), and is release under the CC-BY-SA licence:
  http://creativecommons.org/licenses/by-sa/2.0/fr/

5.3.3 Sounds
------------
Sounds are all taken from The Battle for Wesnoth (http://www.wesnoth.org/), 
except "open_door.ogg" taken from The Freesound Project 
(http://freesound.iua.upf.edu/ ).

5.3.4 Music
-----------
Cellule.ogg/Silence/L'autre endroit
Dark Secrets.ogg/Celestial Aeon Project/Aeon 3
Elfman 01.ogg/Xcyril/Musiques pour films
Jester's Tear.ogg/Celestial Aeon Project/Aeon
La sixieme porte de Shanaaghar.ogg/Greg Baumont/Wood
Red Fields.ogg/Celestial Aeon Project/Aeon 2
Through the Dark Portal.ogg/Celestial Aeon Project

5.3.5 Ambiance
--------------
Ambiance sounds come from The Freesound Project:
http://freesound.iua.upf.edu/

5.4 Licence
~~~~~~~~~~~
This game is released under the GNU General Public License.




