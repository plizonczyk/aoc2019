class Solver:
    def __init__(self):
        with open("../resources/d3/input") as f:
            self.lines = f.readlines()

    def solveP1(self):
        print(self.closest_intersection(self.lines))

    def solveP2(self):
        print(self.minimum_steps(self.lines))

    def closest_intersection(self, lines):
        meshes = []
        for line in lines:
            mesh = set()
            current_point = 0, 0
            for x in line.split(','):
                direction, length = x[0], int(x[1:])
                offset = self.get_offset(direction)

                for _ in range(length):
                    current_point = current_point[0] + offset[0], current_point[1] + offset[1]
                    mesh.add(current_point)

            meshes.append(mesh)

        return min(self.manhattan(pt) for pt in meshes[0] & meshes[1])

    def manhattan(self, point):
        return abs(point[0]) + abs(point[1])

    def minimum_steps(self, lines):
        meshes = []
        for line in lines:
            mesh = {}
            current_point = 0, 0
            steps_taken = 0
            for x in line.split(','):
                direction, length = x[0], int(x[1:])
                offset = self.get_offset(direction)

                for _ in range(length):
                    current_point = current_point[0] + offset[0], current_point[1] + offset[1]
                    steps_taken += 1
                    if current_point not in mesh:
                        mesh[current_point] = steps_taken

            meshes.append(mesh)

        intersections = set(meshes[0].keys()) & set(meshes[1].keys())
        return min(meshes[0][pt] + meshes[1][pt] for pt in intersections)

    def get_offset(self, direction):
        if direction == 'R':
            offset = 1, 0
        if direction == 'L':
            offset = -1, 0
        if direction == 'U':
            offset = 0, 1
        if direction == 'D':
            offset = 0, -1
        return offset


if __name__ == '__main__':
    s = Solver()
    assert s.closest_intersection(["R75,D30,R83,U83,L12,D49,R71,U7,L72", "U62,R66,U55,R34,D71,R55,D58,R83"]) == 159
    assert s.closest_intersection(["R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51",
                                   "U98,R91,D20,R16,D67,R40,U7,R15,U6,R7"]) == 135

    assert s.minimum_steps(["R75,D30,R83,U83,L12,D49,R71,U7,L72", "U62,R66,U55,R34,D71,R55,D58,R83"]) == 610
    assert s.minimum_steps(["R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51",
                            "U98,R91,D20,R16,D67,R40,U7,R15,U6,R7"]) == 410

    s.solveP1()
    s.solveP2()
