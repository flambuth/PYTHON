from collections import namedtuple

BeltStats = namedtuple('BeltStats', 'score ninjas')

ninja_belts = {'yellow': BeltStats(50, 11),
               'orange': BeltStats(100, 7),
               'green': BeltStats(175, 1),
               'blue': BeltStats(250, 5)}


def get_total_points(belts=ninja_belts):
   total_points = 0
   for belt in ninja_belts.values():
      belt_points = belt[0] * belt[1]
      total_points += belt_points
   return total_points
