#Building Base
from turtle import width


class Building:
    def __init__(self, south, west, width_WE, width_NS, height=10):
        self.south=south
        self.west=west
        self.width_WE=width_WE
        self.width_NS=width_NS
        self.height=height

    def corners(self):
        s=self.south
        w=self.west
        we=self.width_WE
        ns=self.width_NS

        return {"north-west": [s+ns, w], "north-east": [s+ns, w+we], "south-west": [s, w], "south-east": [s, w+we]}

    def area(self):
        return self.width_WE*self.width_NS

    def volume(self):
        return self.width_WE*self.width_NS*self.height

    def __repr__(self):
        return f"Building({self.south}, {self.west}, {self.width_WE}, {self.width_NS}, {self.height})"


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    def json_dict(d):
        return dict((k, list(v)) for k, v in d.items())

    b = Building(1, 2, 2, 3)
    b2 = Building(1, 2, 2, 3, 5)
    assert json_dict(b.corners()) == {'north-east': [4, 4], 'south-east': [1, 4],
                                      'south-west': [1, 2], 'north-west': [4, 2]}, "Corners"
    assert b.area() == 6, "Area"
    assert b.volume() == 60, "Volume"
    assert b2.volume() == 30, "Volume2"
    assert str(b) == "Building(1, 2, 2, 3, 10)", "String"
    print (str(b))

'''
# Best "Clear" Solution
from itertools import product
class Building(object): # W to E: width, N to S: depth
    def __init__(self, south, west, width, depth, height=10):
        self.south, self.west = south, west
        self.width, self.depth, self.height = width, depth, height
        self.north, self.east = south + depth, west + width

    def corners(self):
        pairs = product(('south', 'north'), ('west', 'east'))
        return {'-'.join(p): [getattr(self, d) for d in p] for p in pairs}

    def area(self):
        return self.width * self.depth

    def volume(self):
        return self.width * self.depth * self.height

    def __repr__(self):
        txt = 'Building({0.south}, {0.west}, {0.width}, {0.depth}, {0.height})'
        return txt.format(self)

# Best "Creative" Solution
from collections import namedtuple
class Building(namedtuple("Base", "south west width_we width_ns height")):
    east = property(lambda I: I.west + I.width_we)
    north = property(lambda I: I.south + I.width_ns)
    corners = lambda I: {y + "-" + x: (getattr(I, y), getattr(I, x))
                        for x in ("west", "east") for y in ("north", "south")}
    area = lambda I: I.width_ns * I.width_we
    volume = lambda I: I.area() * I.height
    __repr__ = lambda I: I.__class__.__name__ + repr(tuple(I))
Building.__new__.__defaults__ = 10,

# Best "Speedy" Solution
class Building:
    def __init__(self, south, west, width_WE, width_NS, height=10):
        self.south = south
        self.west = west
        self.width_WE = width_WE
        self.width_NS = width_NS
        self.height = height        
        
        
    def corners(self):
        north = self.south + self.width_NS
        east = self.west + self.width_WE
        return {'north-west': [north, self.west], 'north-east': [north, east], "south-west": [self.south, self.west], "south-east": [self.south, east]}

    def area(self):
        return self.width_WE * self.width_NS

    def volume(self):
        return self.area() * self.height

    def __repr__(self):
        return 'Building(%s, %s, %s, %s, %s)' % (self.south, self.west, self.width_WE, self.width_NS, self.height)


# Best "3rd party" Solution

'''