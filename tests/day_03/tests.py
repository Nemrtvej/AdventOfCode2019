from unittest import TestCase

from day_03.main import Point, Builder, Solver1, Solver2


class TestDay03(TestCase):

    def test_builder(self):
        origin = Point(0, 0)
        cases = [
            ('U1,R1', {origin, Point(0, 1), Point(1, 1)}),
        ]

        builder = Builder()

        for case in cases:
            instructions, expected_line = case
            actual_line = builder.build_line(instructions=instructions, origin=origin)
            self.assertEqual(expected_line, actual_line)

    def test_distance(self):
        cases = [
            (Point(2, 2), Point(2, 4), 2),
            (Point(2, 2), Point(2, 2), 0),
        ]

        for case in cases:
            first_point, second_point, expected_distance = case
            actual_distance = first_point.manhattan_distance(second_point)
            self.assertEqual(expected_distance, actual_distance)

    def test_solver_1(self):
        cases = [
            (['R8,U5,L5,D3', 'U7,R6,D4,L4'], 6),
            (['R75,D30,R83,U83,L12,D49,R71,U7,L72', 'U62,R66,U55,R34,D71,R55,D58,R83'], 159),
            (['R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51', 'U98,R91,D20,R16,D67,R40,U7,R15,U6,R7'], 135),
        ]
        builder = Builder()
        solver = Solver1(builder=builder)
        for case in cases:
            test_input, expected_result = case
            first_cable, second_cable = test_input
            actual_result = solver.solve(first_cable, second_cable)
            self.assertEqual(
                expected_result,
                actual_result,
                '%s should be %s but the actual result is %s' % (test_input, expected_result, actual_result)
            )

    def test_solver_2(self):
        cases = [
            (['R8,U5,L5,D3', 'U7,R6,D4,L4'], 30),
            (['R75,D30,R83,U83,L12,D49,R71,U7,L72', 'U62,R66,U55,R34,D71,R55,D58,R83'], 610),
            (['R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51', 'U98,R91,D20,R16,D67,R40,U7,R15,U6,R7'], 410),
        ]
        builder = Builder()
        solver = Solver2(builder=builder)
        for case in cases:
            test_input, expected_result = case
            first_cable, second_cable = test_input
            actual_result = solver.solve(first_cable, second_cable)
            self.assertEqual(
                expected_result,
                actual_result,
                '%s should be %s but the actual result is %s' % (test_input, expected_result, actual_result)
            )
