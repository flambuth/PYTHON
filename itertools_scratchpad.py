##grab the money

#make some counting tools to work with
class Repeater:
    def __init__(self, value):
        self.value = value
#includes the __iter__ dunder method.
    def __iter__(self):
        return RepeaterIterator(self)

#calling a different method for defining class objects
class RepeaterIterator:
    def __init__(self, source):
        self.source = source

    def __next__(self):
        return self.source.value

#I fell in the rabbit hole of learning what a for loop does
#when you use it. It's a while loop with a sentinel to break out of the loop.
#           SENTINELS. cool word. it is an intended end point of an iterating operation
#What are iterables, formally defined in Python
#The interplay between the dunder methods __iter__ and __next__
#What dunder methods. They might be relics.
#       next(x) is actually x.__next__
