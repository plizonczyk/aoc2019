class Solver:
    def __init__(self):
        with open("../resources/d5/input") as f:
            self.data = list(map(lambda x: int(x), f.readline().split(',')))

    def parse_opcode(self, opcode):
        code = int(opcode[-2:])
        flags = [0, 0, 0]
        for i, flag in enumerate(opcode[-3::-1]):
            flags[i] = int(flag)

        return code, flags

    def solve(self, prog_input):
        pc = 0
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
                self.data[arg1] = prog_input
                pc += 2
            elif method == 4:
                arg1 = pc+1 if imm[0] else self.data[pc+1]
                print(self.data[arg1])
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
                return

    #
    # def solveP2(self):
    #     print(self.minimum_steps(self.lines))


if __name__ == '__main__':
    # s = Solver()
    # s.data = list(map(lambda x: int(x), '1002,4,3,4,33'.split(',')))
    # s.solve(1)
    
    print('P1')
    s = Solver()
    s.solve(1)

    print('P2')
    s = Solver()
    s.solve(5)
