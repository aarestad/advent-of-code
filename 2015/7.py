class Connection(object):
    def __init__(self, output):
        self.output = output

class OrConnection(object):
    def __init__(self, x, y, output):
        self.x = x
        self.y = y
        self.output = output



with open('input_7.txt') as input:
