# uncompyle6 version 3.7.4
# Python bytecode 3.8 (3413)
# Decompiled from: Python 2.7.17 (default, Sep 30 2020, 13:38:04) 
# [GCC 7.5.0]
# Warning: this version of Python has problems handling the Python 3 "byte" type in constants properly.

# Embedded file name: C:\Users\ACER\AppData\Local\Programs\Python\Python38\lib\site-packages\pygame\__init__.py
# Compiled at: 2022-11-05 18:10:26
# Size of source mod 2**32: 10287 bytes
"""Pygame is a set of Python modules designed for writing games.
It is written on top of the excellent SDL library. This allows you
to create fully featured games and multimedia programs in the python
language. The package is highly portable, with games running on
Windows, MacOS, OS X, BeOS, FreeBSD, IRIX, and Linux."""
import sys, os
if os.name == 'nt':
    pygame_dir = os.path.split(__file__)[0]
    os.environ['PATH'] = os.environ['PATH'] + ';' + pygame_dir
else:
    if 'DISPLAY' in os.environ:
        if 'SDL_VIDEO_X11_WMCLASS' not in os.environ:
            os.environ['SDL_VIDEO_X11_WMCLASS'] = os.path.basename(sys.argv[0])
        else:

            class MissingModule:
                _NOT_IMPLEMENTED_ = True

                def __init__(self, name, urgent=0):
                    self.name = name
                    exc_type, exc_msg = sys.exc_info()[:2]
                    self.info = str(exc_msg)
                    self.reason = f"{exc_type.__name__}: {self.info}"
                    self.urgent = urgent
                    if urgent:
                        self.warn()

                def __getattr__(self, var):
                    if not self.urgent:
                        self.warn()
                        self.urgent = 1
                    missing_msg = f"{self.name} module not available ({self.reason})"
                    raise NotImplementedError(missing_msg)

                def __nonzero__(self):
                    return False

                __bool__ = __nonzero__

                def warn(self):
                    msg_type = 'import' if self.urgent else 'use'
                    message = f"{msg_type} {self.name}: {self.info}\n({self.reason})"
                    try:
                        import warnings
                        level = 4 if self.urgent else 3
                        warnings.warn(message, RuntimeWarning, level)
                    except ImportError:
                        print(message)


            from pygame.base import *
            from pygame.constants import *
            from pygame.version import *
            from pygame.rect import Rect
            from pygame.rwobject import encode_string, encode_file_path
            import pygame.surflock, pygame.color
            Color = pygame.color.Color
            import pygame.bufferproxy
            BufferProxy = pygame.bufferproxy.BufferProxy
            import pygame.math
            Vector2 = pygame.math.Vector2
            Vector3 = pygame.math.Vector3
            __version__ = ver
            if get_sdl_version() < (2, 0, 0):
                try:
                    import pygame.cdrom
                except (ImportError, IOError):
                    cdrom = MissingModule('cdrom', urgent=1)

        try:
            import pygame.display
        except (ImportError, IOError):
            display = MissingModule('display', urgent=1)

        try:
            import pygame.draw
        except (ImportError, IOError):
            draw = MissingModule('draw', urgent=1)
        else:
            try:
                import pygame.event
            except (ImportError, IOError):
                event = MissingModule('event', urgent=1)

        try:
            import pygame.image
        except (ImportError, IOError):
            image = MissingModule('image', urgent=1)
        else:
            try:
                import pygame.joystick
            except (ImportError, IOError):
                joystick = MissingModule('joystick', urgent=1)

        try:
            import pygame.key
        except (ImportError, IOError):
            key = MissingModule('key', urgent=1)
        else:
            try:
                import pygame.mouse
            except (ImportError, IOError):
                mouse = MissingModule('mouse', urgent=1)

        try:
            import pygame.cursors
            from pygame.cursors import Cursor
        except (ImportError, IOError):
            cursors = MissingModule('cursors', urgent=1)
            Cursor = lambda : Missing_Function
        else:
            try:
                import pygame.sprite
            except (ImportError, IOError):
                sprite = MissingModule('sprite', urgent=1)

        try:
            import pygame.threads
        except (ImportError, IOError):
            threads = MissingModule('threads', urgent=1)
        else:
            try:
                import pygame.pixelcopy
            except (ImportError, IOError):
                pixelcopy = MissingModule('pixelcopy', urgent=1)
            else:

                def warn_unwanted_files():
                    """warn about unneeded old files"""
                    install_path = os.path.split(pygame.base.__file__)[0]
                    extension_ext = os.path.splitext(pygame.base.__file__)[1]
                    ext_to_remove = [
                     'camera']
                    py_to_remove = [
                     'color']
                    if os.name == 'e32':
                        py_to_remove = []
                    extension_files = [f"{x}{extension_ext}" for x in ext_to_remove]
                    py_files = [f"{x}{py_ext}" for py_ext in ('.py', '.pyc', '.pyo') for x in py_to_remove]
                    files = py_files + extension_files
                    unwanted_files = []
                    for f in files:
                        unwanted_files.append(os.path.join(install_path, f))
                    else:
                        ask_remove = []
                        for f in unwanted_files:
                            if os.path.exists(f):
                                ask_remove.append(f)
                        else:
                            if ask_remove:
                                message = 'Detected old file(s).  Please remove the old files:\n'
                                message += ' '.join(ask_remove)
                                message += '\nLeaving them there might break pygame.  Cheers!\n\n'
                                try:
                                    import warnings
                                    level = 4
                                    warnings.warn(message, RuntimeWarning, level)
                                except ImportError:
                                    print(message)


        try:
            from pygame.surface import Surface, SurfaceType
        except (ImportError, IOError):
            Surface = lambda : Missing_Function
        else:
            try:
                import pygame.mask
                from pygame.mask import Mask
            except (ImportError, IOError):
                mask = MissingModule('mask', urgent=0)
                Mask = lambda : Missing_Function

        try:
            from pygame.pixelarray import PixelArray
        except (ImportError, IOError):
            PixelArray = lambda : Missing_Function
        else:
            try:
                from pygame.overlay import Overlay
            except (ImportError, IOError):
                Overlay = lambda : Missing_Function

        try:
            import pygame.time
        except (ImportError, IOError):
            time = MissingModule('time', urgent=1)
        else:
            try:
                import pygame.transform
            except (ImportError, IOError):
                transform = MissingModule('transform', urgent=1)

        if 'PYGAME_FREETYPE' in os.environ:
            try:
                import pygame.ftfont as font
                sys.modules['pygame.font'] = font
            except (ImportError, IOError):
                pass

    else:
        try:
            import pygame.font, pygame.sysfont
            pygame.font.SysFont = pygame.sysfont.SysFont
            pygame.font.get_fonts = pygame.sysfont.get_fonts
            pygame.font.match_font = pygame.sysfont.match_font
        except (ImportError, IOError):
            font = MissingModule('font', urgent=0)

    try:
        import pygame.mixer_music
    except (ImportError, IOError):
        pass
    else:
        try:
            import pygame.mixer
        except (ImportError, IOError):
            mixer = MissingModule('mixer', urgent=0)

    try:
        import pygame.movie
    except (ImportError, IOError):
        movie = MissingModule('movie', urgent=0)
    else:
        try:
            import pygame.scrap
        except (ImportError, IOError):
            scrap = MissingModule('scrap', urgent=0)

    try:
        import pygame.surfarray
    except (ImportError, IOError):
        surfarray = MissingModule('surfarray', urgent=0)
    else:
        try:
            import pygame.sndarray
        except (ImportError, IOError):
            sndarray = MissingModule('sndarray', urgent=0)

    try:
        import pygame.fastevent
    except (ImportError, IOError):
        fastevent = MissingModule('fastevent', urgent=0)
    else:
        try:
            import pygame.imageext
            del pygame.imageext
        except (ImportError, IOError):
            pass
        else:

            def packager_imports():
                """some additional imports that py2app/py2exe will want to see"""
                import atexit, numpy, OpenGL.GL, pygame.macosx, pygame.colordict


            import copyreg

            def __rect_constructor(x, y, w, h):
                return Rect(x, y, w, h)


            def __rect_reduce(r):
                if not isinstance(r, Rect):
                    raise AssertionError
                return (
                 __rect_constructor, (r.x, r.y, r.w, r.h))


            copyreg.pickle(Rect, __rect_reduce, __rect_constructor)

            def __color_constructor(r, g, b, a):
                return Color(r, g, b, a)


            def __color_reduce(c):
                if not isinstance(c, Color):
                    raise AssertionError
                return (
                 __color_constructor, (c.r, c.g, c.b, c.a))


            copyreg.pickle(Color, __color_reduce, __color_constructor)
            if 'PYGAME_HIDE_SUPPORT_PROMPT' not in os.environ:
                print(('pygame {} (SDL {}.{}.{}, Python {}.{}.{})'.format)(ver, *get_sdl_version() + sys.version_info[0:3]))
                print('Hello from the pygame community. https://www.pygame.org/contribute.html')
            del pygame
            del os
            del sys
            del MissingModule
            del copyreg