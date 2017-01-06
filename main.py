#!/usr/bin/env python

# The first group of objects all use 'super' in their init.
class SuperFirst(object):
    def __init__(self):
        super(SuperFirst, self).__init__()
        print("Super First Init")

class SuperSecond(object):
    def __init__(self):
        super(SuperSecond, self).__init__()
        print("Super Second Init")

class SuperThird(SuperSecond, SuperFirst):
    def __init__(self):
        super(SuperThird, self).__init__()
        print("Super Third Init...done.")


# This group has 'super' commented out
class First(object):
    def __init__(self):
        super(First, self).__init__()
        print("First Init")

class Second(object):
    def __init__(self):
        #super(Second, self).__init__()
        print("Second Init")

class Third(Second, First):
    def __init__(self):
        #super(Third, self).__init__()
        print("Third Init....done.")


# All init called
mySuper = SuperThird()

# Some init not called
# Comment out 'super' in each class to see the effect
myNotSoSuper = Third()
