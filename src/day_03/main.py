from typing import List, Optional

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
                new_point = Point(new_point.x, new_point.y + distance)
            elif direction == 'D':
                new_point = Point(new_point.x, new_point.y - distance)
            elif direction == 'R':
                new_point = Point(new_point.x + distance, new_point.y)
            elif direction == 'L':
                new_point = Point(new_point.x - distance, new_point.y)
            else:
                raise ValueError('Unknown instruction: %s', instruction)

            points.append(new_point)

        return points

class StackOverflowCalculator:
    def line_intersection(self, line1, line2):
        xdiff = (line1[0][0] - line1[1][0], line2[0][0] - line2[1][0])
        ydiff = (line1[0][1] - line1[1][1], line2[0][1] - line2[1][1])

        def det(a, b):
            return a[0] * b[1] - a[1] * b[0]

        div = det(xdiff, ydiff)
        if div == 0:
            return None

        d = (det(*line1), det(*line2))
        x = det(d, xdiff) / div
        y = det(d, ydiff) / div
        return x, y

    def poly_intersection(self, poly1, poly2):
        results = []
        for i, p1_first_point in enumerate(poly1[:-1]):
            p1_second_point = poly1[i + 1]

            for j, p2_first_point in enumerate(poly2[:-1]):
                p2_second_point = poly2[j + 1]

                result = self.line_intersection((p1_first_point, p1_second_point), (p2_first_point, p2_second_point))
                if result and result not in results:
                    results.append(result)

        return results

class IntersectionCalculator:

    def __init__(self):
        self.calculator = StackOverflowCalculator()

    def poly_intersection(self, poly1: List[Point], poly2: List[Point]):
        first_poly = list(map(lambda point: (point.x, point.y), poly1))
        second_poly = list(map(lambda point: (point.x, point.y), poly2))

        result = self.calculator.poly_intersection(first_poly, second_poly)
        return list(map(lambda entry: Point(entry[0], entry[1]), result))


class Solver:

    def __init__(self, builder: Builder, intersection_calculator: IntersectionCalculator):
        self.builder = builder
        self.intersection_calculator = intersection_calculator

    def solve(self, first_line: str, second_line: str):
        origin = Point(0, 0)
        first_polyline = self.builder.build_line(first_line, origin)
        second_polyline = self.builder.build_line(second_line, origin)

        intersections = self.intersection_calculator.poly_intersection(first_polyline, second_polyline)
        lowest_distance = 999999999
        for intersection in intersections:
            if intersection == origin:
                continue
            current_distance = intersection.manhattan_distance(origin)
            if current_distance < lowest_distance:
                lowest_distance = current_distance

        return lowest_distance


def main_part_1():
    pass


def main_part_2():
    pass

if __name__ == '__main__':
    main_part_1()
    main_part_2()