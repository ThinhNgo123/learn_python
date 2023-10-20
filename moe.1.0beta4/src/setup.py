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
Mines of Elderlore : Windows Binary creator
"""

from distutils.core import setup
import sys, os, shutil

nom = 'Mines of Elderlore'
ver = '1.0beta4'
#name of starting .PY
script = "moe-pygame.py"            
auteur = "Altefcat"
#ICO file for the .EXE
icon_file = "moe.ico"        
#extra files/dirs copied to game            
extra_data = ['COPYING.txt', 'moe.py', 'setup.py', 'rltile.py', 
'moe-curses.py', 'moe-pygame.py', 'readme.txt', 'data'] 
#extra python modules not auto found
extra_modules = ['Numeric', 'curses', 'pygame']   
# modules Python à ignorer
ignore_modules = ['Tkinter']


import py2exe

# If run without args, build executables, in quiet mode.
if len(sys.argv) == 1:
    sys.argv.append("py2exe")
    sys.argv.append("-q")
    sys.argv.append("-dmoe.%s" % ver)
    sys.argv.append("-i"+','.join(extra_modules))
    sys.argv.append("-e"+','.join(ignore_modules))

setup(options = {"py2exe": {"compressed": 1,
                            "optimize": 2,
                            "bundle_files": 2}},
      zipfile = None,
      name = nom,
      version = ver,
      author = auteur,
      windows = [{'script':script,
                  'icon_resources':[(1,icon_file)]}]
      )

#also need to hand copy the extra files here
def installfile(name):
    dst = "moe.%s" % ver
    print 'copying', name, '->', dst
    if os.path.isdir(name):
        dst = os.path.join(dst, name)
        if os.path.isdir(dst):
            shutil.rmtree(dst)
        shutil.copytree(name, dst)
    elif os.path.isfile(name):
        shutil.copy(name, dst)
    else:
        print 'Warning, %s not found' % name

#pygamedir = os.path.split(pygame.base.__file__)[0]
#installfile(os.path.join(pygamedir, pygame.font.get_default_font()))
#installfile(os.path.join(pygamedir, 'pygame_icon.bmp'))
for data in extra_data:
    installfile(data)