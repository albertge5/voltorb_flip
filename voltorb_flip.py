import random
import sys
class Card:
    def __init__(self):
        self.value = random.randint(0, 3)
        self.faceDown = True

    def __str__(self):
        if self.faceDown:
            return 'x'
        else:
            return str(self.value)

    def flip(self):
        self.faceDown = False
        return self.value

class Board:
    def  __init__(self, size):
        self.counter = 0
        self.size = size
        self.hit_voltorb = False
        self.board = []
        for i in range(size):
            self.board.append([])
            for j in range(size):
                c = Card()
                if c.value > 1:
                    self.counter += 1
                self.board[i].append(c)

    def printBoard(self):
        for row in self.board:
            print '-'*(2*self.size + 1)
            sys.stdout.write("|")
            for cell in row:
                sys.stdout.write(str(cell) + "|")
            print ""

    def revealBoard(self):
        print "Revealing..."
        for row in self.board:
            for cell in row:
                cell.flip()
                print cell,
            print ""

    def isVoltorb(self, value):
        return value == 0

    def chooseCard(self, i, j):
        if i <= 0 or j <= 0 or i > self.size or j > self.size:
            raise ValueError('Not a valid card location! Try again')
        print "Choosing card at row", i, "col", j
        value = self.board[i - 1][j - 1].flip()
        if self.isVoltorb(value):
            print "Boom! You lose.",
            self.hit_voltorb = True
            return
        elif value > 1:
            self.counter -= 1
        self.printBoard()

    def done(self):
        if self.counter == 0 or self.hit_voltorb is True:
            print "Done with game!"
            self.revealBoard()
            return True
        else:
            return False

if __name__ == '__main__':
    size = input('Enter board size:')
    print "Setting up board..."
    b = Board(size)
    b.printBoard()
    while not b.done():
        try:
            loc = [int(n) for n in raw_input('Choose the location:').split(" ")]
            b.chooseCard(loc[0], loc[1])
        except ValueError as e:
            print e
        except IndexError as e:
            print e

    # for i in range(5):
    #     b.chooseCard(i, 1)
