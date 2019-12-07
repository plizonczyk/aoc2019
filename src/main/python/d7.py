from itertools import permutations
from typing import List


class Solver:
    def __init__(self):
        with open("../resources/d7/input") as f:
            self.data = list(map(lambda x: int(x), f.readline().split(',')))

        self.state = []
        self.pcs = []
        self.last_outputs = []
        self.current_i = 0

    def parse_opcode(self, opcode):
        code = int(opcode[-2:])
        flags = [0, 0, 0]
        for i, flag in enumerate(opcode[-3::-1]):
            flags[i] = int(flag)

        return code, flags

    def solve(self, inputs):
        pc = 0
        output = None
        while pc < len(self.data):
            method, imm = self.parse_opcode(str(self.data[pc]))
            if method == 1:
                arg1 = self.data[pc+1] if imm[0] else self.data[self.data[pc+1]]
                arg2 = self.data[pc+2] if imm[1] else self.data[self.data[pc+2]]
                arg3 = pc+3 if imm[2] else self.data[pc+3]
                self.data[arg3] = arg1 + arg2
                pc += 4
            elif method == 2:
                arg1 = self.data[pc+1] if imm[0] else self.data[self.data[pc+1]]
                arg2 = self.data[pc+2] if imm[1] else self.data[self.data[pc+2]]
                arg3 = pc+3 if imm[2] else self.data[pc+3]
                self.data[arg3] = arg1 * arg2
                pc += 4
            elif method == 3:
                arg1 = pc+1 if imm[0] else self.data[pc+1]
                self.data[arg1] = inputs.pop(0)
                pc += 2
            elif method == 4:
                arg1 = pc+1 if imm[0] else self.data[pc+1]
                output = self.data[arg1]
                pc += 2
            elif method == 5:
                arg1 = pc+1 if imm[0] else self.data[pc+1]
                arg2 = pc+2 if imm[1] else self.data[pc+2]
                if self.data[arg1] != 0:
                    pc = self.data[arg2]
                else:
                    pc += 3
            elif method == 6:
                arg1 = pc+1 if imm[0] else self.data[pc+1]
                arg2 = pc+2 if imm[1] else self.data[pc+2]
                if self.data[arg1] == 0:
                    pc = self.data[arg2]
                else:
                    pc += 3
            elif method == 7:
                arg1 = pc+1 if imm[0] else self.data[pc+1]
                arg2 = pc+2 if imm[1] else self.data[pc+2]
                self.data[self.data[pc+3]] = 1 if self.data[arg1] < self.data[arg2] else 0
                pc += 4
            elif method == 8:
                arg1 = pc+1 if imm[0] else self.data[pc+1]
                arg2 = pc+2 if imm[1] else self.data[pc+2]
                self.data[self.data[pc+3]] = 1 if self.data[arg1] == self.data[arg2] else 0
                pc += 4
            elif method == 99:
                return output

    def chain(self, phase_settings):
        inp = 0
        out = None
        for sett in phase_settings:
            out = self.solve([sett, inp])
            inp = out
        return out

    def solve2(self, inputs, current_i):
        while self.pcs[current_i] < len(self.state[current_i]):
            method, imm = self.parse_opcode(str(self.state[current_i][self.pcs[current_i]]))
            if method == 1:
                arg1 = self.state[current_i][self.pcs[current_i]+1] if imm[0] else self.state[current_i][self.state[current_i][self.pcs[current_i]+1]]
                arg2 = self.state[current_i][self.pcs[current_i]+2] if imm[1] else self.state[current_i][self.state[current_i][self.pcs[current_i]+2]]
                arg3 = self.pcs[current_i]+3 if imm[2] else self.state[current_i][self.pcs[current_i]+3]
                self.state[current_i][arg3] = arg1 + arg2
                self.pcs[current_i] += 4
            elif method == 2:
                arg1 = self.state[current_i][self.pcs[current_i]+1] if imm[0] else self.state[current_i][self.state[current_i][self.pcs[current_i]+1]]
                arg2 = self.state[current_i][self.pcs[current_i]+2] if imm[1] else self.state[current_i][self.state[current_i][self.pcs[current_i]+2]]
                arg3 = self.pcs[current_i]+3 if imm[2] else self.state[current_i][self.pcs[current_i]+3]
                self.state[current_i][arg3] = arg1 * arg2
                self.pcs[current_i] += 4
            elif method == 3:
                arg1 = self.pcs[current_i]+1 if imm[0] else self.state[current_i][self.pcs[current_i]+1]
                self.state[current_i][arg1] = inputs.pop(0)
                self.pcs[current_i] += 2
            elif method == 4:
                arg1 = self.pcs[current_i]+1 if imm[0] else self.state[current_i][self.pcs[current_i]+1]
                output = self.state[current_i][arg1]
                self.last_outputs[current_i] = output
                self.pcs[current_i] += 2
                return output
            elif method == 5:
                arg1 = self.pcs[current_i]+1 if imm[0] else self.state[current_i][self.pcs[current_i]+1]
                arg2 = self.pcs[current_i]+2 if imm[1] else self.state[current_i][self.pcs[current_i]+2]
                if self.state[current_i][arg1] != 0:
                    self.pcs[current_i] = self.state[current_i][arg2]
                else:
                    self.pcs[current_i] += 3
            elif method == 6:
                arg1 = self.pcs[current_i]+1 if imm[0] else self.state[current_i][self.pcs[current_i]+1]
                arg2 = self.pcs[current_i]+2 if imm[1] else self.state[current_i][self.pcs[current_i]+2]
                if self.state[current_i][arg1] == 0:
                    self.pcs[current_i] = self.state[current_i][arg2]
                else:
                    self.pcs[current_i] += 3
            elif method == 7:
                arg1 = self.pcs[current_i]+1 if imm[0] else self.state[current_i][self.pcs[current_i]+1]
                arg2 = self.pcs[current_i]+2 if imm[1] else self.state[current_i][self.pcs[current_i]+2]
                self.state[current_i][self.state[current_i][self.pcs[current_i]+3]] = 1 if self.state[current_i][arg1] < self.state[current_i][arg2] else 0
                self.pcs[current_i] += 4
            elif method == 8:
                arg1 = self.pcs[current_i]+1 if imm[0] else self.state[current_i][self.pcs[current_i]+1]
                arg2 = self.pcs[current_i]+2 if imm[1] else self.state[current_i][self.pcs[current_i]+2]
                self.state[current_i][self.state[current_i][self.pcs[current_i]+3]] = 1 if self.state[current_i][arg1] == self.state[current_i][arg2] else 0
                self.pcs[current_i] += 4
            elif method == 99:
                return 'end'

    def chainP2(self, phase_settings):
        inp = 0
        self.current_i = 0
        self.state = [self.data.copy(), self.data.copy(), self.data.copy(), self.data.copy(), self.data.copy()]
        self.last_outputs = [0, 0, 0, 0, 0]
        self.pcs = [0, 0, 0, 0, 0]
        for sett in phase_settings:
            inp = self.solve2([sett, inp], self.current_i)
            self.current_i += 1

        while self.solve2([inp], self.current_i % 5) is not 'end':
            inp = self.last_outputs[self.current_i % 5]
            self.current_i += 1
        return self.last_outputs[-1]

    def solveP1(self):
        print(max(self.chain(phase_settings) for phase_settings in permutations([0, 1, 2, 3, 4])))

    def solveP2(self):
        print(max(self.chainP2(phase_settings) for phase_settings in permutations([5, 6, 7, 8, 9])))


if __name__ == '__main__':
    print('P1')
    s = Solver()
    s.solveP1()

    print('P2')
    s = Solver()
    s.solveP2()

