from random import randint


class Die(object):

    """docstring for Die"""

    def __init__(self, sides=6):

        self.sides = sides

    def roll_die(self):
        return (randint(1, self.sides))


x = Die(20)
for i in range(10):
    print(str(i) + ':' + str(x.roll_die()))
