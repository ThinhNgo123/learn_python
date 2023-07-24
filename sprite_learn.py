class Sprite:
	"""docstring for sprite"""
	def __init__(self, name, *groups):
		self.name = name
		self.__g = {}
		if groups:
			self.add(*groups)

	def print(self):
		print(self.__g)

	def add(self, *groups):
		has = self.__g.__contains__
		for group in groups:
			if hasattr(group, "_spritegroup"):
				if not has(group):
					group.add_internal(self)
					self.add_internal(group)
			else:
				self.add(*group)

	def add_internal(self, group):
		self.__g[group] = 0
		

class AbstractGroup(object):
    _spritegroup = True

    def __init__(self):
        self.spritedict = {}

    def print(self):
    	print(self.spritedict)

    def sprites(self):
        return list(self.spritedict)

    def add_internal(self, sprite, layer=None,):
        self.spritedict[sprite] = None

    def has_internal(self, sprite):
        return sprite in self.spritedict

    def add(self, *sprites):
        for sprite in sprites:
            if isinstance(sprite, Sprite):
                if not self.has_internal(sprite):
                    self.add_internal(sprite)
                    sprite.add_internal(self)
            else:
                try:
                    self.add(*sprite)
                except (TypeError, AttributeError):
                    if hasattr(sprite, "_spritegroup"):
                        for spr in sprite.sprites():
                            if not self.has_internal(spr):
                                self.add_internal(spr)
                                spr.add_internal(self)
                    elif not self.has_internal(sprite):
                        self.add_internal(sprite)
                        sprite.add_internal(self)

class Group(AbstractGroup):
    
    def __init__(self, *sprites):
        AbstractGroup.__init__(self)
        self.add(*sprites)

group = Group()

def main():
	a = Sprite("hinh 1", group)
	b = Sprite("hinh 2", group)
	# group.add(a, b)
	a.print()
	b.print()
	group.print()

if __name__ == '__main__':
	main()