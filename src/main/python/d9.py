from collections import defaultdict


class Solver:
    def __init__(self):
        self.data = defaultdict(int)
        with open("../resources/d9/input") as f:
            data = map(lambda x: int(x), f.readline().split(','))
        self.data.update({i: value for i, value in enumerate(data)})
        self.relative_base = 0
        self.pc = 0
        self.flags = None

    def parse_opcode(self, opcode):
        code = int(opcode[-2:])
        flags = [0, 0, 0]
        for i, flag in enumerate(opcode[-3::-1]):
            flags[i] = int(flag)

        return code, flags

    def get_ptr(self, arg_position):
        if self.flags[arg_position - 1] == 0:  # positional
            return self.data[self.pc + arg_position]
        elif self.flags[arg_position - 1] == 1:  # immediate
            return self.pc + arg_position
        else:  # relative
            return self.data[self.pc + arg_position] + self.relative_base

    def get_val(self, arg_position):
        return self.data[self.get_ptr(arg_position)]

    def solve(self, inp):
        while self.pc < len(self.data):
            method, self.flags = self.parse_opcode(str(self.data[self.pc]))
            if method == 1:  # addition
                self.data[self.get_ptr(3)] = self.get_val(1) + self.get_val(2)
                self.pc += 4
            elif method == 2:  # multiplication
                self.data[self.get_ptr(3)] = self.get_val(1) * self.get_val(2)
                self.pc += 4
            elif method == 3:  # read input
                self.data[self.get_ptr(1)] = inp
                self.pc += 2
            elif method == 4:  # print output
                print(self.data[self.get_ptr(1)])
                self.pc += 2
            elif method == 5:  # jmp if not zero
                if self.data[self.get_ptr(1)] != 0:
                    self.pc = self.data[self.get_ptr(2)]
                else:
                    self.pc += 3
            elif method == 6:  # jmp if zero
                if self.data[self.get_ptr(1)] == 0:
                    self.pc = self.data[self.get_ptr( 2)]
                else:
                    self.pc += 3
            elif method == 7:  # arg1 less than arg2
                self.data[self.get_ptr(3)] = 1 if self.get_val(1) < self.get_val(2) else 0
                self.pc += 4
            elif method == 8:  # arg1 equals arg2
                self.data[self.get_ptr(3)] = 1 if self.get_val(1) == self.get_val(2) else 0
                self.pc += 4
            elif method == 9:  # set relative base
                self.relative_base += self.get_val(1)
                self.pc += 2
            elif method == 99:  # halt
                return

    #
    # def solveP2(self):
    #     print(self.minimum_steps(self.lines))


if __name__ == '__main__':
    print('P1')
    s = Solver()
    s.solve(1)

    print('P2')
    s = Solver()
    s.solve(2)
