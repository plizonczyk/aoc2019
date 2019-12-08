from collections import Counter


class Solver:
    def __init__(self):
        with open("../resources/d8/input") as f:
            self.data = f.readline().strip()

    def solveP1(self, width, height):
        layers = [self.data[i:i+width*height] for i in range(0, len(self.data), width*height)]
        min_layer = min(layers, key=lambda x: Counter(x).get('0', 0))
        print(Counter(min_layer))

    def solveP2(self, width, height):
        layers = [self.data[i:i+width*height] for i in range(0, len(self.data), width*height)]
        squashed = ''
        for i in range(width*height):
            pixel = ''.join(layer[i] for layer in layers).lstrip('2')[0]
            squashed += 'X' if pixel == '1' else ' '
        for i in range(height):
            print(squashed[i*width:(i+1)*width])


if __name__ == '__main__':
    print('P1')
    s = Solver()
    s.solveP1(25, 6)

    print('P2')
    s = Solver()
    s.solveP2(25, 6)

