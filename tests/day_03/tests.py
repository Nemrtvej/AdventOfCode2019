from unittest import TestCase

from day_03.main import Line, Point, IntersectionCalculator, Builder, Solver


class TestDay03(TestCase):

    def test_distance(self):
        cases = [
            (Point(2, 2), Point(2, 4), 2),
            (Point(2, 2), Point(2, 2), 0),
        ]

        for case in cases:
            first_point, second_point, expected_distance = case
            actual_distance = first_point.manhattan_distance(second_point)
            self.assertEqual(expected_distance, actual_distance)

    def test_geometry(self):
        cases = [
            # ([Point(2, 2), Point(2, 4)], [Point(1, 3), Point(3, 3)], [Point(2, 3)]),
            # ([Point(2, 2), Point(2, 4), Point(2, 10)], [Point(1, 3), Point(3, 3), Point(10, 3)], [Point(2, 3)]),
            (
                [Point(0, 0), Point(8, 0), Point(8, 5), Point(3, 5), Point(3, 2)], # first polyline
                [Point(0, 0), Point(0, 7), Point(6, 7), Point(6, 3), Point(2, 3)], # second polyline
                [Point(0, 0), Point(3, 3), Point(6, 5)] # intersections
            ),
        ]

        geometry = IntersectionCalculator()
        for case in cases:
            first_polyline, second_polyline, expected_result = case
            actual_result = geometry.poly_intersection(first_polyline, second_polyline)
            self.assertEqual(expected_result, actual_result)

    def test_checker_first_version(self):
        cases = [
            (['R8,U5,L5,D3', 'U7,R6,D4,L4'], 6),
            (['R75,D30,R83,U83,L12,D49,R71,U7,L72', 'U62,R66,U55,R34,D71,R55,D58,R83'], 159),
            (['R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51', 'U98,R91,D20,R16,D67,R40,U7,R15,U6,R7'], 135),
        ]
        calculator = IntersectionCalculator()
        builder = Builder()
        solver = Solver(builder=builder, intersection_calculator=calculator)
        for case in cases:
            test_input, expected_result = case
            first_cable, second_cable = test_input
            actual_result = solver.solve(first_cable, second_cable)
            self.assertEqual(
                expected_result,
                actual_result,
                '%s should be %s but the actual result is %s' % (test_input, expected_result, actual_result)
            )

    def test_checker_second_version(self):
        pass