class Solver:
    def __init__(self, inp):
        with open("../resources/d9/input") as f:
            data = map(lambda x: int(x), f.readline().split(','))
        self.data = dict(enumerate(data))
        self.relative_base = 0
        self.pc = 0
        self.input = inp
        self.flags = None

        self.opcode_funs = {
            1: self.addition,
            2: self.multiplication,
            3: self.read_input,
            4: self.print_output,
            5: self.jmp_notzero,
            6: self.jmp_zero,
            7: self.less_than,
            8: self.equals,
            9: self.set_relative_base
        }

    def parse_opcode(self, opcode):
        self.flags = [0, 0, 0]
        for i, flag in enumerate(opcode[-3::-1]):
            self.flags[i] = int(flag)

        return int(opcode[-2:])  # method code

    def get_ptr(self, arg_position):
        if self.flags[arg_position - 1] == 0:  # positional
            return self.data[self.pc + arg_position]
        elif self.flags[arg_position - 1] == 1:  # immediate
            return self.pc + arg_position
        else:  # relative
            return self.data[self.pc + arg_position] + self.relative_base

    def get_val(self, arg_position):
        return self.data[self.get_ptr(arg_position)]

    def solve(self):
        while self.pc < len(self.data):
            method = self.parse_opcode(str(self.data[self.pc]))
            if method == 99:  # halt
                return
            self.opcode_funs[method]()

    def addition(self):
        self.data[self.get_ptr(3)] = self.get_val(1) + self.get_val(2)
        self.pc += 4

    def multiplication(self):
        self.data[self.get_ptr(3)] = self.get_val(1) * self.get_val(2)
        self.pc += 4

    def read_input(self):
        self.data[self.get_ptr(1)] = self.input
        self.pc += 2

    def print_output(self):
        print(self.data[self.get_ptr(1)])
        self.pc += 2

    def jmp_notzero(self):
        if self.data[self.get_ptr(1)] != 0:
            self.pc = self.data[self.get_ptr(2)]
        else:
            self.pc += 3

    def jmp_zero(self):
        if self.data[self.get_ptr(1)] == 0:
            self.pc = self.data[self.get_ptr(2)]
        else:
            self.pc += 3

    def less_than(self):
        self.data[self.get_ptr(3)] = 1 if self.get_val(1) < self.get_val(2) else 0
        self.pc += 4

    def equals(self):
        self.data[self.get_ptr(3)] = 1 if self.get_val(1) == self.get_val(2) else 0
        self.pc += 4

    def set_relative_base(self):
        self.relative_base += self.get_val(1)
        self.pc += 2


if __name__ == '__main__':
    print('P1')
    Solver(1).solve()

    print('P2')
    Solver(2).solve()
