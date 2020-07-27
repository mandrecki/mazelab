from collections import namedtuple


VonNeumannMotionTuple = namedtuple('VonNeumannMotion', 
                              ['north', 'south', 'west', 'east'])

def VonNeumannMotion():
    return VonNeumannMotionTuple([-1, 0], [1, 0], [0, -1], [0, 1])


MooreMotionTuple = namedtuple('MooreMotion', 
                         ['north', 'south', 'west', 'east', 
                          'northwest', 'northeast', 'southwest', 'southeast'])

def MooreMotion():
    return MooreMotionTuple([-1, 0], [1, 0], [0, -1], [0, 1], 
                            [-1, -1], [-1, 1], [1, -1], [1,1])                                   
                            
