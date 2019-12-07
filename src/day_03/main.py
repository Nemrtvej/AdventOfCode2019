from typing import List, Optional, Set, Dict, Tuple


class Point:

    def __init__(self, x: float, y: float):
        self.x = int(x)
        self.y = int(y)

    def manhattan_distance(self, other: "Point") -> int:
        return abs(self.x - other.x) + abs(self.y - other.y)

    def __repr__(self):
        return '|X=%s Y=%s|' % (self.x, self.y)

    def __eq__(self, other):
        return isinstance(other, Point) and self.x == other.x and self.y == other.y

    def __hash__(self) -> int:
        return self.x * 10000 + self.y

class Line:

    def __init__(self, start: Point, end: Point):
        self.start = start
        self.end = end


class Builder:

    def build_line(self, instructions: str, origin: Point) -> List[Point]:
        new_point = origin
        points = [new_point]
        for instruction in instructions.split(','):
            direction = instruction[0]
            distance = int(instruction[1:])
            if direction == 'U':
                for i in range (0, distance):
                    new_point = Point(new_point.x, new_point.y + 1)
                    points.append(new_point)
            elif direction == 'D':
                for i in range (0, distance):
                    new_point = Point(new_point.x, new_point.y - 1)
                    points.append(new_point)
            elif direction == 'R':
                for i in range (0, distance):
                    new_point = Point(new_point.x + 1, new_point.y)
                    points.append(new_point)
            elif direction == 'L':
                for i in range (0, distance):
                    new_point = Point(new_point.x - 1, new_point.y)
                    points.append(new_point)
            else:
                raise ValueError('Unknown instruction: %s', instruction)

        return points


class Solver1:

    def __init__(self, builder: Builder):
        self.builder = builder

    def solve(self, first_line: str, second_line: str):
        origin = Point(0, 0)
        first_polyline = self.builder.build_line(first_line, origin)
        second_polyline = self.builder.build_line(second_line, origin)

        intersections = set(first_polyline).intersection(set(second_polyline))
        lowest_distance = 999999999
        for intersection in intersections:
            if intersection == origin:
                continue
            current_distance = intersection.manhattan_distance(origin)
            lowest_distance = min(current_distance, lowest_distance)

        return lowest_distance


class Solver2:

    def __init__(self, builder: Builder):
        self.builder = builder

    def solve(self, first_line, second_line):
        origin = Point(0, 0)
        first_polyline = self.builder.build_line(first_line, origin)
        second_polyline = self.builder.build_line(second_line, origin)

        intersections = set(first_polyline).intersection(set(second_polyline))
        first_distance_map = self._get_distance_map(first_polyline, intersections)
        second_distance_map = self._get_distance_map(second_polyline, intersections)

        lowest_distance = 99999999
        for intersection in intersections:
            if intersection == origin:
                continue
            current_distance = first_distance_map[intersection.__hash__()] + second_distance_map[intersection.__hash__()]
            lowest_distance = min(current_distance, lowest_distance)

        return lowest_distance


    def _get_distance_map(self, line: List[Point], intersections: Set[Point]) -> Dict[int, int]:
        distance_map = {}

        for distance, point in enumerate(line, start=0):
            if point in intersections and point.__hash__() not in distance_map.keys():
                distance_map[point.__hash__()] = distance

        return distance_map


def main_part_1():
    with open('input.txt') as fp:
        first_line = fp.readline()
        second_line = fp.readline()

    builder = Builder()
    solver = Solver1(builder=builder)

    print(solver.solve(first_line, second_line))


def main_part_2():
    with open('input.txt') as fp:
        first_line = fp.readline()
        second_line = fp.readline()

    builder = Builder()
    solver = Solver2(builder=builder)

    print(solver.solve(first_line, second_line))

if __name__ == '__main__':
    main_part_1()
    main_part_2()